from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QScrollArea, QFrame, QSpinBox
)
from PySide6.QtCore import Qt, Signal

class ProductCard(QFrame):
    add_to_cart = Signal(int, int)  # product_id, quantity
    
    def __init__(self, product_data):
        super().__init__()
        self.product_data = product_data
        self.setup_ui()
        
    def setup_ui(self):
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        name_label = QLabel(self.product_data["name"])
        name_label.setObjectName("product_name")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        
        category_label = QLabel(f"Kategori: {self.product_data['category_name']}")
        category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        category_label.setStyleSheet("font-size: 11px; color: #7f8c8d;")
        
        price_label = QLabel(f"Rp {self.product_data['price']:,.0f}")
        price_label.setObjectName("product_price")
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        price_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #27ae60;")
        
        stock_label = QLabel(f"Stok: {self.product_data['stock']}")
        stock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        stock_label.setStyleSheet("font-size: 12px; color: #34495e;")
        
        qty_layout = QHBoxLayout()
        qty_label = QLabel("Jumlah:")
        self.qty_spin = QSpinBox()
        self.qty_spin.setMinimum(1)
        self.qty_spin.setMaximum(self.product_data['stock'])
        self.qty_spin.setValue(1)
        qty_layout.addWidget(qty_label)
        qty_layout.addWidget(self.qty_spin)
        
        self.btn_add = QPushButton("Tambah ke Keranjang")
        self.btn_add.setObjectName("primary_btn")
        self.btn_add.clicked.connect(self.on_add_to_cart)
        
        if self.product_data['stock'] <= 0:
            self.btn_add.setEnabled(False)
            self.btn_add.setText("Stok Habis")
            self.qty_spin.setEnabled(False)
        
        layout.addWidget(name_label)
        layout.addWidget(category_label)
        layout.addWidget(price_label)
        layout.addWidget(stock_label)
        layout.addLayout(qty_layout)
        layout.addWidget(self.btn_add)
        layout.addStretch()
        
        self.setLayout(layout)
        
    def on_add_to_cart(self):
        qty = self.qty_spin.value()
        self.add_to_cart.emit(self.product_data["id"], qty)


class ProductCatalogView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Title
        title = QLabel("Katalog Produk")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Scroll Area for Products
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        # Container for product grid
        self.products_container = QWidget()
        self.products_layout = QGridLayout(self.products_container)
        self.products_layout.setSpacing(15)
        
        scroll.setWidget(self.products_container)
        layout.addWidget(scroll)
        
        self.setLayout(layout)
        
    def display_products(self, products):
        # Clear existing products
        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add products to grid (3 columns)
        row = 0
        col = 0
        for product in products:
            card = ProductCard(product)
            self.products_layout.addWidget(card, row, col)
            
            col += 1
            if col >= 3:
                col = 0
                row += 1
        
        # Add stretch to push cards to top
        self.products_layout.setRowStretch(row + 1, 1)
