from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from app.models.product_model import ProductModel
from app.models.transaction_model import TransactionModel

class CartController(QObject):
    data_changed = Signal()

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.cart = []

        self.view.btn_checkout.clicked.connect(self.open_checkout_dialog)

    def add_to_cart(self, product_data, qty):
        """Add product to cart from catalog"""
        try:
            if qty <= 0 or qty > product_data["stock"]:
                raise ValueError

            subtotal = product_data["price"] * qty

            self.cart.append({
                "product_id": product_data["id"],
                "name": product_data["name"],
                "price": product_data["price"],
                "quantity": qty,
                "subtotal": subtotal
            })

            self.refresh_table()
            
            QMessageBox.information(
                self.view, "Sukses",
                f"{product_data['name']} ditambahkan ke keranjang"
            )

        except:
            QMessageBox.warning(
                self.view, "Error",
                "Jumlah tidak valid atau stok tidak cukup"
            )

    def refresh_table(self):
        self.view.table.setRowCount(len(self.cart))
        total = 0

        for row, item in enumerate(self.cart):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(item["product_id"])))
            self.view.table.setItem(row, 1, QTableWidgetItem(item["name"]))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(item["price"])))
            self.view.table.setItem(row, 3, QTableWidgetItem(str(item["quantity"])))
            self.view.table.setItem(row, 4, QTableWidgetItem(str(item["subtotal"])))
            total += item["subtotal"]

        self.view.label_total.setText(f"Total: {total}")

    def open_checkout_dialog(self):
        if not self.cart:
            QMessageBox.warning(self.view, "Error", "Keranjang masih kosong")
            return

        total_amount = sum(item["subtotal"] for item in self.cart)
        
        from app.views.checkout_dialog import CheckoutDialog
        dialog = CheckoutDialog(total_amount, self.view)
        
        if dialog.exec():
            self.save_transaction(dialog.payment_amount, dialog.change_amount)

    def save_transaction(self, payment, change):
        TransactionModel.create_transaction(self.cart)

        QMessageBox.information(
            self.view, "Sukses",
            f"Transaksi berhasil disimpan\nKembalian: Rp {change:,.0f}"
        )

        self.cart.clear()
        self.refresh_table()
        self.load_products()

        self.data_changed.emit()   # 🚀 INI KUNCINYA
