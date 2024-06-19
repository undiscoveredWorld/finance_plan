from openpyxl import load_workbook


def read_range(path_to_file: str, sheet_name: str, range_: str) -> list[list[str]]:
    """Read rows from range in sheet in file and return it.

    Args:
        range_: as like as excel (A1:E5)
    Returns:
        List of rows in the form list of strings
    """
    sheet = open_sheet(path_to_file, sheet_name)
    return read_range_from_sheet(sheet, range_)


def open_sheet(path_to_file: str, sheet_name: str):
    wb = load_workbook(path_to_file, read_only=True)
    return wb[sheet_name]


def read_range_from_sheet(sheet, range_):
    range_split = range_.split(":")

    result = []
    for row in sheet[range_split[0]:range_split[1]]:
        result.append([])
        for cell in row:
            if cell.value is None:
                result[-1].append("")
                continue
            result[-1].append(str(cell.value))

    return result
