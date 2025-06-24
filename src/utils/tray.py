import sys
from PyQt6.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, 
                           QDialog, QVBoxLayout, QLabel, QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtGui import QIcon, QFont, QColor
from PyQt6.QtCore import Qt, QPoint

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ProcSPY Hakkında")
        self.setFixedSize(450, 400)
        self.setStyleSheet("""
            QDialog {
                background-color: #1A1A2E;
                border-radius: 15px;
                border: 1px solid #16213E;
            }
            QLabel {
                color: #E2E2E2;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)
        layout = QVBoxLayout()
        layout.setSpacing(16)
        layout.setContentsMargins(30, 30, 30, 30)
        # Logo ve başlık container'ı
        logo_title_container = QVBoxLayout()
        logo_title_container.setSpacing(6)
        logo_title_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo = QLabel("🔍")
        logo.setFont(QFont("Segoe UI Emoji", 48))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title = QLabel("ProcSPY")
        title_font = QFont("Segoe UI", 28)
        title_font.setWeight(QFont.Weight.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #4E9EFD; margin-top: 0px;")
        logo_title_container.addWidget(logo)
        logo_title_container.addWidget(title)
        # Alt başlık
        subtitle = QLabel("Sistem İzleme Aracı")
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #7B8AB8;")
        # Ayırıcı çizgi
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("background-color: #16213E; margin: 10px 40px;")
        # Açıklama
        description = QLabel(
            "ProcSPY, sisteminizde çalışan uygulamaları\n"
            "izlemenize ve yönetmenize olanak sağlayan\n"
            "güçlü ve modern bir sistem izleme aracıdır."
        )
        desc_font = QFont("Segoe UI", 11)
        description.setFont(desc_font)
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description.setStyleSheet("color: #B4BEE0;")
        # Widget'ları layout'a ekle
        layout.addLayout(logo_title_container)
        layout.addWidget(subtitle)
        layout.addWidget(line)
        layout.addWidget(description)
        self.setLayout(layout)

class SystemTrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon.fromTheme("computer"))
        self.menu = QMenu()
        self.menu.addAction('Hakkında', self.about)
        self.menu.addSeparator()
        self.menu.addAction('Çıkış', self.quit)
        self.menu.setStyleSheet("""
            QMenu {
                background-color: #1A1A2E;
                border: 1px solid #16213E;
                border-radius: 8px;
                padding: 5px;
            }
            QMenu::item {
                color: #E2E2E2;
                padding: 8px 25px;
                margin: 2px;
            }
            QMenu::item:selected {
                background-color: #16213E;
                border-radius: 4px;
            }
            QMenu::separator {
                height: 1px;
                background-color: #16213E;
                margin: 5px 15px;
            }
        """)
        self.tray.setContextMenu(self.menu)
        self.tray.show()
        self.tray.activated.connect(self.tray_activated)
        self.about_dialog = None  # Dialog referansı

    def about(self):
        if self.about_dialog is None:
            self.about_dialog = AboutDialog()
            self.about_dialog.finished.connect(self.clear_about_dialog)
        self.about_dialog.show()
        self.about_dialog.activateWindow()

    def clear_about_dialog(self):
        self.about_dialog = None

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.about()

    def quit(self):
        self.tray.hide()
        self.app.quit()

    def run(self):
        return self.app.exec()

if __name__ == '__main__':
    app = SystemTrayApp()
    sys.exit(app.run())