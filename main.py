import sys
from PySide6.QtWidgets import QApplication
from app.views.login_view import LoginView

def main():
    app = QApplication(sys.argv)
    
    # Load QSS stylesheet
    with open("app/styles.qss", "r") as f:
        app.setStyleSheet(f.read())
    
    window = LoginView()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
