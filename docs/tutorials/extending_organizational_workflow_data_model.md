# FA-ZTP Tutorials: Extending Organizational Workflow Data Model

[Back to README](../../README.md#table-of-contents)

[Back to Tutorials](TUTORIALS.md)

## Extending the Organizational Workflow Data Model

At times, it may be necessary to extend the spreadsheet to include new columns or even new sheets/tables.

### Adding New Columns to an Existing Sheet

A majority of the worksheets are dynamically consumed by the Python script ![](/roles/fortigate.ztp/files/python/consume_branch_spreadsheet.py).

* The "FortiGates" worksheet is typically the only sheet with some kind of hard-coded column mapping in the Python script.
* All other worksheets are dynamically consumed so when a column is added it gets automatically added to the dataset.
* All columns are set to lowercase, and all spaces are turned into underscores.
  * i.e. "FortiGate Name" becomes "fortigate_name"
  
### Adding New Sheets
New worksheets are automatically consumed, but the relationships must be added to ![the Python conversion script.](/roles/fortigate.ztp/files/python/consume_branch_spreadsheet.py)

To see why new sheets are automatically consumed:

```python
def convert_whole_workbook_to_dict(workbook_path=None):
    wb = openpyxl.load_workbook(workbook_path)
    workbook_dict = dict()
    sheet_names = wb.sheetnames
    for sheet in sheet_names:
        try:
            print("Reading: " + sheet.replace(" ", "_"))
            worksheet_dict = convert_worksheet_to_dict(worksheet=sheet,
                                                       workbook_path=workbook_path)
            workbook_dict[sheet.replace(" ", "_")] = worksheet_dict
        except Exception as e:
            str(e)
            raise
    return workbook_dict

```

For a closer look of how we relate a worksheet to a FortiGate take a look at how we associate IPSec rows to a FortiGate:

```python
fgt_dict["ipsec"] = []
for ipsec in sheets['IPSec']:
    if fgt_dict['fgt_name'] == ipsec['FortiGate Name']:
        fgt_dict['ipsec'].append(format_excel_columns(ipsec))

```

When we talk about manually coding the relationships into the Python conversion script this is what we're talking about.

[Back to Top](#table-of-contents)


