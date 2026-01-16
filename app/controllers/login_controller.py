from PySide6.QtWidgets import QMessageBox
from app.models.user_model import UserModel
from app.views.main_view import MainView

class LoginController:
    def __init__(self, view):
        self.view = view
        self.view.btn_login.clicked.connect(self.login)

    def login(self):
        username = self.view.input_username.text()
        password = self.view.input_password.text()

        if not username or not password:
            QMessageBox.warning(
                self.view,
                "Login Gagal",
                "Username dan password harus diisi."
            )
            return

        user = UserModel.authenticate(username, password)

        if user:
            self.main_window = MainView(user)
            self.main_window.show()
            self.view.close()
        else:
            QMessageBox.critical(
                self.view,
                "Login Gagal",
                "Username atau password salah."
            )
