from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from app.models.category_model import CategoryModel

class CategoryController(QObject):
    data_changed = Signal()
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.selected_id = None

        self.load_data()

        self.view.btn_add.clicked.connect(self.add_category)
        self.view.btn_update.clicked.connect(self.update_category)
        self.view.btn_delete.clicked.connect(self.delete_category)
        self.view.table.cellClicked.connect(self.select_row)

    def load_data(self):
        data = CategoryModel.get_all()
        self.view.table.setRowCount(len(data))

        for row, item in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.view.table.setItem(row, 1, QTableWidgetItem(item["name"]))

    def select_row(self, row, column):
        self.selected_id = int(self.view.table.item(row, 0).text())
        name = self.view.table.item(row, 1).text()
        self.view.input_name.setText(name)

    def add_category(self):
        name = self.view.input_name.text()
        if not name:
            QMessageBox.warning(self.view, "Error", "Nama kategori wajib diisi")
            return

        CategoryModel.create(name)
        self.view.input_name.clear()
        self.load_data()
        self.data_changed.emit()

    def update_category(self):
        if not self.selected_id:
            QMessageBox.warning(self.view, "Error", "Pilih data terlebih dahulu")
            return

        name = self.view.input_name.text()
        CategoryModel.update(self.selected_id, name)
        self.view.input_name.clear()
        self.selected_id = None
        self.load_data()
        self.data_changed.emit()

    def delete_category(self):
        if not self.selected_id:
            QMessageBox.warning(self.view, "Error", "Pilih data terlebih dahulu")
            return

        CategoryModel.delete(self.selected_id)
        self.view.input_name.clear()
        self.selected_id = None
        self.load_data()
        self.data_changed.emit()
