import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import cv2


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel("Label Text")
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()
        self.Worker1.start()

        self.setLayout(self.VBL)


class Worker1(QThread):
    ImageUpdate = Signal(QImage)

    def run(self):
        self.ThreadActive = True
        cap = cv2.VideoCapture(0)
        while self.ThreadActive:
            _, frame = cap.read()
            if _:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flipped = cv2.flip(img, 1)
                q_image = QImage(flipped.data, flipped.shape[1], flipped.shape[0], QImage.Format_RGB888)
                pic = q_image.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




