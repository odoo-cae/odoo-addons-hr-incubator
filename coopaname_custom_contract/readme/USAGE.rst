Customize a report
~~~~~~~~~~~~~~~~~~

- the report templates are in :code:`/coopaname_custom_contract/report`
- edit the xml using qweb language, refer to `Odoo documentation <https://www.odoo.com/documentation/12.0/reference/reports.html>`_
- to add style, edit the :code:`coopaname_custom_contact.css` stylesheet and add this line to your report

  - :code:`<link href="/coopaname_custom_contract/static/src/css/coopaname_custom_contact.css" rel="stylesheet"/>`
- :code:`hr_contract_cdi.xml` is a good example

Add a report
~~~~~~~~~~~~~~~~~~

- create a xml template and add the file to the :code:`__manifest__.py`
- add the template id to the REFERENCE variable in :code:`reference.py`
- add the report case to :code:`create_document` function in :code:`hr_contract.py`
- add the required fields for this report to :code:`required_fields.py`
