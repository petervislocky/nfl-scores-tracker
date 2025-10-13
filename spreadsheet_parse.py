from typing import Any

from openpyxl import load_workbook


class ParseSpreadsheet:

    def __init__(self, spreadsheet_path: str=r"./spreadsheet/NFL_Poop_Picks_2025-26.xlsx", sheet: str="Week 1"):
        self.path = spreadsheet_path
        self.workbook = load_workbook(spreadsheet_path)
        self.sheet = self.workbook[sheet]

    def get_cell(self, cell_ref: str) -> str:
        """Get value stored in given cell.

        Args
            `cell_ref`: The cell to get the value of, must be in Excel format
                Example: 'B2', 'C5', ..."""
        return self.sheet[cell_ref].value

    def set_cell(self, cell_ref: str, value: Any) -> None:
        self.sheet[cell_ref] = value

ps = ParseSpreadsheet()
print(ps.get_cell("B2"))
