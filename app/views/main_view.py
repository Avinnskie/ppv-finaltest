from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget
)

from app.views.cart_view import CartView
from app.controllers.cart_controller import CartController

from app.views.product_catalog_view import ProductCatalogView
from app.controllers.product_catalog_controller import ProductCatalogController

from app.views.admin_panel_view import AdminPanelView
from app.controllers.admin_panel_controller import AdminPanelController

from app.views.report_view import ReportView
from app.controllers.report_controller import ReportController

class MainView(QMainWindow):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.setWindowTitle(f"Sistem Penjualan Desa - {user_data['username']}")
        self.setMinimumSize(1000, 600)

        self.setup_ui()

    def setup_ui(self):
        container = QWidget()
        main_layout = QHBoxLayout(container)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        self.btn_catalog = QPushButton("Produk")
        self.btn_catalog.setObjectName("sidebar_btn")
        sidebar_layout.addWidget(self.btn_catalog)

        self.btn_cart = QPushButton("Keranjang")
        self.btn_cart.setObjectName("sidebar_btn")
        sidebar_layout.addWidget(self.btn_cart)

        sidebar_layout.addStretch()

        if self.user_data['role'] == 'admin':
            self.btn_admin = QPushButton("Admin Panel")
            self.btn_admin.setObjectName("sidebar_btn")
            sidebar_layout.addWidget(self.btn_admin)

        if self.user_data['role'] == 'admin':
            self.btn_report = QPushButton("Laporan")
            self.btn_report.setObjectName("sidebar_btn")
            sidebar_layout.addWidget(self.btn_report)

        content_widget = QWidget()
        content_widget.setObjectName("content_area")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)

        self.stack = QStackedWidget()

        self.catalog_view = ProductCatalogView()

        self.cart_view = CartView()
        self.cart_controller = CartController(self.cart_view)

        self.catalog_controller = ProductCatalogController(self.catalog_view, self.cart_controller)

        self.stack.addWidget(self.catalog_view)
        self.stack.addWidget(self.cart_view)

        if self.user_data['role'] == 'admin':
            self.report_view = ReportView()
            self.report_controller = ReportController(self.report_view)
            self.stack.addWidget(self.report_view)
            self.btn_report.clicked.connect(self.show_report)

        if self.user_data['role'] == 'admin':
            self.admin_panel_view = AdminPanelView()
            self.admin_panel_controller = AdminPanelController(self.admin_panel_view)
            self.stack.addWidget(self.admin_panel_view)

            self.admin_panel_controller.data_changed.connect(self.refresh_all_data)
            self.btn_admin.clicked.connect(self.show_admin_panel)

        content_layout.addWidget(self.stack)

        self.btn_catalog.clicked.connect(self.show_catalog)
        self.btn_cart.clicked.connect(self.show_cart)

        self.cart_controller.data_changed.connect(self.refresh_all_data)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_widget, 1)

        self.setCentralWidget(container)

    def show_catalog(self):
        self.catalog_controller.load_products()
        self.stack.setCurrentIndex(0)

    def show_cart(self):
        self.stack.setCurrentIndex(1)

    def show_report(self):
        if self.user_data['role'] == 'admin':
            self.report_controller.load_data()
            self.stack.setCurrentIndex(2)

    def show_admin_panel(self):
        if self.user_data['role'] == 'admin':
            self.stack.setCurrentIndex(3)

    def refresh_all_data(self):
        self.catalog_controller.load_products()
        if self.user_data['role'] == 'admin':
            self.report_controller.load_data()
