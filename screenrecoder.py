import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import pyautogui
import cv2
import threading

class LoginSignupApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login and Signup")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.signup_button)

        self.record_button = QPushButton("Record Screen")
        self.record_button.clicked.connect(self.start_recording)
        layout.addWidget(self.record_button)

        self.central_widget.setLayout(layout)

        self.recording = False

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Implement your login logic here, e.g., check credentials against a database

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Implement your signup logic here, e.g., add user to a database

    def start_recording(self):
        if not self.recording:
            self.recording = True
            recording_thread = threading.Thread(target=self.record_screen)
            recording_thread.start()
            self.record_button.setText("Stop Recording")
        else:
            self.recording = False
            self.record_button.setText("Record Screen")

    def record_screen(self):
        codec = cv2.VideoWriter_fourcc(*"XVID")
        output_file = "recorded_screen.avi"
        screen_size = (1920, 1080)

        out = cv2.VideoWriter(output_file, codec, 20.0, screen_size)

        while self.recording:
            img = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginSignupApp()
    window.show()
    sys.exit(app.exec_())
