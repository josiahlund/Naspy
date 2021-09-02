# Naspy

This tools suite provides an API-like interface to MSC.Nastran input and output files.

The recommended format for any operation is [HDF5](https://portal.hdfgroup.org/display/HDF5/HDF5). This is the primary 
format for all tools, any other data format used must go through an additional conversion process.

The MSC.Natran Quick Reference Guide (QRG) can be found on the MSC simcompanion site. Newer versions require a license,
but the 2013 QRG is publically available [here](https://simcompanion.mscsoftware.com/infocenter/index?page=content&id=DOC10351&actp=RSS).

## Functionality

- read_bdf()
  - When called from command line, will open a file dialog to select file to read
  - When called as function, will take a path to a bulk data file
  - Skips all pre-bulk entries (lines preceeding "BEGIN BULK") such as case control entries
  - Reads bulk data entries, card by card (supports both short and long format), breaking them into fields
  - Creates a class instance for each supported card (found in BulkDataEntries.py)
