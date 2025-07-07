# basic_app.py
import pandas as pd
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QComboBox

class BasicApp(QWidget):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        # --- clean the DataFrame FIRST -----------------------------
        df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
        self.df = df

        # --- build the product list --------------------------------
        safe_items = {
            str(item)                              # cast to str
            for item in list(df.index) + list(df.columns)
            if pd.notna(item)                      # skip NaN
        }
        products = sorted(safe_items)

        self.setWindowTitle("Sanitation Library")
        self.resize(400, 400)

        products = sorted(set(df.index) | set(df.columns))

        self.current_product = QComboBox()
        self.current_product.addItems(products)
        self.current_product.setCurrentIndex(-1)          # start blank

        self.next_product = QComboBox()
        self.next_product.addItems(products)
        self.next_product.setCurrentIndex(-1)

        # self.current_product = QLineEdit(placeholderText="Enter Current Product")
        # self.next_product    = QLineEdit(placeholderText="Enter Next Product")

        self.button          = QPushButton("Submit")
        self.output_label    = QLabel()

        layout = QVBoxLayout(self)
        for w in (self.current_product, self.next_product, self.button, self.output_label):
            layout.addWidget(w)

        self.button.clicked.connect(self.on_submit)

    def on_submit(self):
        curr_product = self.current_product.currentText()
        nxt_product  = self.next_product.currentText()
        df = df.dropna(axis=0, how="all")
        df = df.dropna(axis=1, how="all")

        if not curr_product or not nxt_product:
            self.output_label.setText("Please fill both fields.")
            return

        try:
            # example lookup
            result = self.df.loc[curr_product, nxt_product]
            self.output_label.setText(f"Value in CSV: {result}")
        except KeyError:
            self.output_label.setText("Combination not found in CSV.")
