from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from app.models.product_model import ProductModel

class ProductCatalogController(QObject):
    def __init__(self, view, cart_controller):
        super().__init__()
        self.view = view
        self.cart_controller = cart_controller
        
        self.load_products()
        
    def load_products(self):
        """Load all products and display in catalog"""
        products = ProductModel.get_all()
        self.view.display_products(products)
        
        # Connect each product card's add_to_cart signal
        for i in range(self.view.products_layout.count()):
            widget = self.view.products_layout.itemAt(i).widget()
            if widget and hasattr(widget, 'add_to_cart'):
                widget.add_to_cart.connect(self.handle_add_to_cart)
    
    def handle_add_to_cart(self, product_id, quantity):
        """Handle add to cart from product card"""
        products = ProductModel.get_all()
        product = next((p for p in products if p["id"] == product_id), None)
        
        if product:
            self.cart_controller.add_to_cart(product, quantity)
            # Reload products to update stock display
            self.load_products()
