from openpyxl import load_workbook
class Excel_Reader:

    @staticmethod
    def get_data(filename,sheetname):
        workbook = load_workbook(filename)
        sheet = workbook[sheetname]

        data = []
        rows = sheet.iter_rows(min_row=2,
            max_row=3,
            max_col=2,
            values_only=True)
        for row in rows:
            data.append(row)

        return data