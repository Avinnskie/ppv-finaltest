from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget
)
from app.views.category_view import CategoryView
from app.views.product_view import ProductView

class AdminPanelView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        self.tabs = QTabWidget()
        
        self.category_view = CategoryView()
        self.tabs.addTab(self.category_view, "Kelola Kategori")
        
        self.product_view = ProductView()
        self.tabs.addTab(self.product_view, "Kelola Produk")
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
