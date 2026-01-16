from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QPushButton
)

class ReportView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label_title = QLabel("Laporan Penjualan")
        self.label_total = QLabel("Total Penjualan: 0")

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["ID Transaksi", "Tanggal", "Total"]
        )

        self.btn_detail = QPushButton("Lihat Detail Transaksi")
        self.btn_export = QPushButton("Export ke Excel")

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_total)
        layout.addWidget(self.table)
        layout.addWidget(self.btn_detail)
        layout.addWidget(self.btn_export)

        self.setLayout(layout)
