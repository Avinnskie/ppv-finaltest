from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt

class CartView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Title
        title = QLabel("Keranjang Belanja")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Produk", "Harga", "Qty", "Subtotal"]
        )

        total_layout = QHBoxLayout()
        self.label_total = QLabel("Total: 0")
        self.label_total.setObjectName("total_label")
        self.btn_checkout = QPushButton("Checkout")
        self.btn_checkout.setObjectName("primary_btn")

        total_layout.addWidget(self.label_total)
        total_layout.addStretch()
        total_layout.addWidget(self.btn_checkout)

        layout.addWidget(self.table)
        layout.addLayout(total_layout)

        self.setLayout(layout)
