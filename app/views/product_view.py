from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem,
    QComboBox
)

class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        form = QHBoxLayout()

        self.cb_category = QComboBox()
        self.input_name = QLineEdit()
        self.input_price = QLineEdit()
        self.input_stock = QLineEdit()

        self.input_name.setPlaceholderText("Nama Produk")
        self.input_price.setPlaceholderText("Harga")
        self.input_stock.setPlaceholderText("Stok")

        self.btn_add = QPushButton("Tambah")
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Hapus")

        form.addWidget(self.cb_category)
        form.addWidget(self.input_name)
        form.addWidget(self.input_price)
        form.addWidget(self.input_stock)
        form.addWidget(self.btn_add)
        form.addWidget(self.btn_update)
        form.addWidget(self.btn_delete)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Kategori", "Nama", "Harga", "Stok"]
        )
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addLayout(form)
        layout.addWidget(self.table)
        self.setLayout(layout)
