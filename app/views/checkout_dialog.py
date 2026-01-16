from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt

class CheckoutDialog(QDialog):
    def __init__(self, total_amount, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Checkout")
        self.setFixedSize(300, 400)
        self.total_amount = total_amount
        self.payment_amount = 0
        self.change_amount = 0

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Total Label
        self.lbl_total = QLabel(f"Total Belanja: Rp {self.total_amount:,.0f}")
        self.lbl_total.setObjectName("total_display")
        layout.addWidget(self.lbl_total)

        # Payment Input
        layout.addWidget(QLabel("Uang Bayar:"))
        self.input_pay = QLineEdit()
        self.input_pay.setPlaceholderText("Masukkan jumlah uang")
        self.input_pay.textChanged.connect(self.calculate_change)
        layout.addWidget(self.input_pay)

        # Change Label
        self.lbl_change = QLabel("Kembalian: Rp 0")
        self.lbl_change.setObjectName("change_display")
        layout.addWidget(self.lbl_change)

        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_confirm = QPushButton("Konfirmasi")
        self.btn_confirm.setObjectName("primary_btn")
        self.btn_confirm.clicked.connect(self.handle_confirm)
        self.btn_confirm.setEnabled(False)  # Disabled until enough payment
        
        self.btn_cancel = QPushButton("Batal")
        self.btn_cancel.setObjectName("danger_btn")
        self.btn_cancel.clicked.connect(self.reject)

        btn_layout.addWidget(self.btn_confirm)
        btn_layout.addWidget(self.btn_cancel)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def calculate_change(self):
        try:
            text = self.input_pay.text().replace(".", "").replace(",", "")
            if not text:
                self.payment_amount = 0
            else:
                self.payment_amount = int(text)

            self.change_amount = self.payment_amount - self.total_amount
            
            self.lbl_change.setText(f"Kembalian: Rp {self.change_amount:,.0f}")

            if self.change_amount >= 0:
                self.lbl_change.setStyleSheet("font-size: 16px; font-weight: bold; color: green; background-color: #e8f8f5; padding: 10px; border-radius: 6px;")
                self.btn_confirm.setEnabled(True)
            else:
                self.lbl_change.setStyleSheet("font-size: 16px; font-weight: bold; color: red; background-color: #fadbd8; padding: 10px; border-radius: 6px;")
                self.btn_confirm.setEnabled(False)

        except ValueError:
            self.lbl_change.setText("Input tidak valid")
            self.btn_confirm.setEnabled(False)

    def handle_confirm(self):
        if self.payment_amount >= self.total_amount:
            self.accept()
        else:
            QMessageBox.warning(self, "Peringatan", "Uang bayar kurang!")
