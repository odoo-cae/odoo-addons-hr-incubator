# Copyright 2020 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Event(models.Model):
    _inherit = "event.event"

    show_button_create_user_for_all_participants = fields.Boolean(
        string="Show Button Create User For All Participants",
        compute="_compute_show_button_create_user_for_all_participants",
    )

    @api.multi
    @api.depends("seats_expected")
    def _compute_show_button_create_user_for_all_participants(self):
        for event in self:
            event.show_button_create_user_for_all_participants = (
                event.seats_expected != 0
            ) and (
                event.event_type_id
                == self.env.ref(
                    "coopaname_custom.event_type_accounting_workshop"
                )
            )

    def button_create_user_for_all_participants(self):
        self.ensure_one()
        for registration in self.registration_ids:
            if (
                registration.employee_id
                and registration.employee_id.work_email
            ):
                registration.employee_id.create_user_portal_access()
            elif registration.partner_id and registration.partner_id.email:
                registration.partner_id.create_user_portal_access()

    @api.multi
    def sync_organizer_registrations(self, new_organizer_id):
        self.ensure_one()
        attendees = list(
            filter(None, self.registration_ids.mapped("partner_id").ids)
        )

        # cancel previous organizer registration
        if self.organizer_id.id in attendees:
            old_organizer_reg = self.registration_ids.filtered(
                lambda r: r.partner_id == self.organizer_id
            )
            old_organizer_reg.is_organizer = False
            old_organizer_reg.button_reg_cancel()

        # create or update new organizer registration
        if new_organizer_id in attendees:
            new_organizer_reg = self.registration_ids.filtered(
                lambda r: r.partner_id == self.organizer_id
            )
            new_organizer_reg.is_organizer = True
            new_organizer_reg.confirm_registration()
        else:
            new_registration = self.registration_ids.create(
                {
                    "event_id": self.id,
                    "partner_id": new_organizer_id,
                    "is_organizer": True,
                }
            )
            new_registration.confirm_registration()

    @api.multi
    def sync_co_organizer_registrations(self, new_co_organizer_id):
        self.ensure_one()
        attendees = list(
            filter(None, self.registration_ids.mapped("partner_id").ids)
        )

        # cancel previous oco_rganizer registration
        if self.co_organizer_id.id in attendees:
            old_co_organizer_reg = self.registration_ids.filtered(
                lambda r: r.partner_id == self.co_organizer_id
            )
            old_co_organizer_reg.is_co_organizer = False
            old_co_organizer_reg.button_reg_cancel()

        # create or update new co_organizer registration
        if new_co_organizer_id in attendees:
            new_co_organizer_reg = self.registration_ids.filtered(
                lambda r: r.partner_id == self.co_organizer_id
            )
            new_co_organizer_reg.is_co_organizer = True
            new_co_organizer_reg.confirm_registration()
        else:
            new_registration = self.registration_ids.create(
                {
                    "event_id": self.id,
                    "partner_id": new_co_organizer_id,
                    "is_co_organizer": True,
                }
            )
            new_registration.confirm_registration()

    @api.model
    def create(self, vals):
        event = super(Event, self).create(vals)
        if "organizer_id" in vals:
            event.sync_organizer_registrations(vals["organizer_id"])
        if "co_organizer_id" in vals:
            event.sync_co_organizer_registrations(vals["co_organizer_id"])
        return event

    @api.multi
    def write(self, vals):
        if "organizer_id" in vals:
            self.sync_organizer_registrations(vals["organizer_id"])
        if "co_organizer_id" in vals:
            self.sync_co_organizer_registrations(vals["co_organizer_id"])
        res = super(Event, self).write(vals)
        return res
