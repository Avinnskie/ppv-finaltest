from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem
)

class CategoryView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        form_layout = QHBoxLayout()
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nama Kategori")

        self.btn_add = QPushButton("Tambah")
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Hapus")

        form_layout.addWidget(self.input_name)
        form_layout.addWidget(self.btn_add)
        form_layout.addWidget(self.btn_update)
        form_layout.addWidget(self.btn_delete)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Kategori"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addLayout(form_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)
