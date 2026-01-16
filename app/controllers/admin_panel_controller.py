from PySide6.QtCore import QObject, Signal
from app.controllers.category_controller import CategoryController
from app.controllers.product_controller import ProductController

class AdminPanelController(QObject):
    data_changed = Signal()
    
    def __init__(self, view):
        super().__init__()
        self.view = view
        
        # Initialize controllers for each tab
        self.category_controller = CategoryController(self.view.category_view)
        self.product_controller = ProductController(self.view.product_view)
        
        # Connect data changed signals
        self.category_controller.data_changed.connect(self.on_data_changed)
        self.product_controller.data_changed.connect(self.on_data_changed)
    
    def on_data_changed(self):
        """Emit signal when data changes"""
        self.data_changed.emit()
