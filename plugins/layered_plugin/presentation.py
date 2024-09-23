from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from .business import BusinessLogic

class PluginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.business_logic = BusinessLogic()

        self.button_execute = QPushButton('Add product')
        self.button_execute.clicked.connect(self.add_product_click_handler)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID', 'Product'])

        layout = QVBoxLayout()
        layout.addWidget(self.button_execute)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def add_product_click_handler(self):
        self.business_logic.add_product()
        products = self.business_logic.get_all_products()
        self.redraw_table(products)

    def redraw_table(self, products):
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(products):
            self.table.insertRow(row_number)
            for column_number, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table.setItem(row_number, column_number, item)

    def get_products(self):
        products = self.business_logic.get_all_products()
        return products
