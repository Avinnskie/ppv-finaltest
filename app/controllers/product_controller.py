from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from app.models.product_model import ProductModel
from app.models.category_model import CategoryModel

class ProductController(QObject):
    data_changed = Signal()
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.selected_id = None
        self.categories = []

        self.load_categories()
        self.load_data()

        self.view.btn_add.clicked.connect(self.add_product)
        self.view.btn_update.clicked.connect(self.update_product)
        self.view.btn_delete.clicked.connect(self.delete_product)
        self.view.table.cellClicked.connect(self.select_row)

    def load_categories(self):
        self.categories = CategoryModel.get_all()
        self.view.cb_category.clear()

        for cat in self.categories:
            self.view.cb_category.addItem(cat["name"], cat["id"])

    def load_data(self):
        data = ProductModel.get_all()
        self.view.table.setRowCount(len(data))

        for row, item in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.view.table.setItem(row, 1, QTableWidgetItem(item["category_name"] or "-"))
            self.view.table.setItem(row, 2, QTableWidgetItem(item["name"]))
            self.view.table.setItem(row, 3, QTableWidgetItem(str(item["price"])))
            self.view.table.setItem(row, 4, QTableWidgetItem(str(item["stock"])))

    def select_row(self, row, col):
        self.selected_id = int(self.view.table.item(row, 0).text())
        self.view.input_name.setText(self.view.table.item(row, 2).text())
        self.view.input_price.setText(self.view.table.item(row, 3).text())
        self.view.input_stock.setText(self.view.table.item(row, 4).text())

    def add_product(self):
        name = self.view.input_name.text()
        price = self.view.input_price.text()
        stock = self.view.input_stock.text()
        category_id = self.view.cb_category.currentData()

        if not name or not price or not stock:
            QMessageBox.warning(self.view, "Error", "Semua field wajib diisi")
            return

        ProductModel.create(category_id, name, float(price), int(stock))
        self.clear_form()
        self.load_data()
        self.data_changed.emit()

    def update_product(self):
        if not self.selected_id:
            QMessageBox.warning(self.view, "Error", "Pilih produk terlebih dahulu")
            return

        ProductModel.update(
            self.selected_id,
            self.view.cb_category.currentData(),
            self.view.input_name.text(),
            float(self.view.input_price.text()),
            int(self.view.input_stock.text())
        )
        self.clear_form()
        self.load_data()
        self.data_changed.emit()

    def delete_product(self):
        if not self.selected_id:
            QMessageBox.warning(self.view, "Error", "Pilih produk terlebih dahulu")
            return

        ProductModel.delete(self.selected_id)
        self.clear_form()
        self.load_data()
        self.data_changed.emit()

    def clear_form(self):
        self.selected_id = None
        self.view.input_name.clear()
        self.view.input_price.clear()
        self.view.input_stock.clear()
