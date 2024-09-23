from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

class TextboxPluginWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def display_data(self, data):
        # [(id, product), ...]
        if data:
            text = ''
            for row in data:
                text += f"ID: {row[0]}, Product: {row[1]}\n"
            self.text_edit.setText(text)
        else:
            self.text_edit.setText("No data.")
