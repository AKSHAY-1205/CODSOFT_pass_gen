import sys
import string
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")

        # Length Input
        self.length_label = QLabel('Password Length:')
        self.length_spinbox = QSpinBox(self)
        self.length_spinbox.setRange(4, 100)
        self.length_spinbox.setValue(12)

        # Checkbox for character types
        self.uppercase_checkbox = QCheckBox('Include Uppercase Letters', self)
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox = QCheckBox('Include Lowercase Letters', self)
        self.lowercase_checkbox.setChecked(True)
        self.digits_checkbox = QCheckBox('Include Digits', self)
        self.digits_checkbox.setChecked(True)
        self.special_chars_checkbox = QCheckBox('Include Special Characters', self)
        self.special_chars_checkbox.setChecked(True)

        # Generate Button
        self.generate_button = QPushButton('Generate Password', self)
        self.generate_button.clicked.connect(self.generate_password)

        # Result Display
        self.result_label = QLabel('Generated Password:', self)
        self.password_display = QLineEdit(self)
        self.password_display.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.length_label)

        length_layout = QHBoxLayout()
        length_layout.addWidget(self.length_spinbox)
        layout.addLayout(length_layout)

        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.lowercase_checkbox)
        layout.addWidget(self.digits_checkbox)
        layout.addWidget(self.special_chars_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.password_display)

        self.setLayout(layout)

    def generate_password(self):
        length = self.length_spinbox.value()

        characters = ''
        if self.uppercase_checkbox.isChecked():
            characters += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            characters += string.ascii_lowercase
        if self.digits_checkbox.isChecked():
            characters += string.digits
        if self.special_chars_checkbox.isChecked():
            characters += string.punctuation

        if not characters:
            QMessageBox.warning(self, 'Input Error', 'Please select at least one character type')
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGeneratorApp()
    ex.show()
    sys.exit(app.exec_())
