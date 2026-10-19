import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMenu,
    QSystemTrayIcon,
    QWidget,
)


class CrosshairOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        screen = QApplication.primaryScreen()
        if screen is None:
            raise RuntimeError("Primary screen is unavailable")
        geometry = screen.geometry()
        self.setGeometry(geometry)

        size = 10
        self.label = QLabel(self)
        self.label.setGeometry(
            geometry.width() // 2 - size // 2,
            geometry.height() // 2 - size // 2,
            size,
            size,
        )
        self.label.setStyleSheet(
            "background-color: #ff3b30; border-radius: 5px;"
        )

        self.show()
        self._create_tray_icon()

    def _create_tray_icon(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            return

        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#ff3b30"))
        painter.drawEllipse(11, 11, 10, 10)
        painter.end()

        self.tray_icon = QSystemTrayIcon(QIcon(pixmap), self)
        self.tray_icon.setToolTip("Desktop Crosshair Overlay")
        menu = QMenu()
        quit_action = QAction("Çıkış", menu)
        quit_action.triggered.connect(QApplication.instance().quit)
        menu.addAction(quit_action)
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = CrosshairOverlay()
    sys.exit(app.exec_())

