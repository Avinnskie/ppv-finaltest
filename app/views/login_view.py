from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt
from app.controllers.login_controller import LoginController

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Sistem Penjualan Desa")
        self.setFixedSize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("login_container")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(15)

        self.label_title = QLabel("Login")
        self.label_title.setObjectName("title")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Login")
        self.btn_login.setObjectName("primary_btn")

        layout.addStretch()
        layout.addWidget(self.label_title)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)
        layout.addStretch()

        self.setLayout(layout)
        self.controller = LoginController(self)
