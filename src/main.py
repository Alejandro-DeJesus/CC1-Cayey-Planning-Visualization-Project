# main.py
import sys
from pathlib import Path
import pandas as pd
from PySide6.QtWidgets import QApplication
from basic_app import BasicApp

HERE = Path(__file__).resolve().parent
# project root  …/
ROOT = HERE.parent
CSV_PATH = ROOT / "Sanitation_Matrix.csv"

if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH, index_col=0)
    app = QApplication(sys.argv)
    window = BasicApp(df)   # pass DataFrame in
    window.show()
    # sys.exit(app.exec())

