from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget

class View(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MVP + plugins app')

        self.button_execute_console_log_plugin = QPushButton('Execute console log plugin')
        self.button_execute_communication_between_plugins_example = QPushButton('Execute communication between plugins example')

        self.layout = QVBoxLayout()

        # buttons
        self.layout.addWidget(self.button_execute_console_log_plugin)
        self.layout.addWidget(self.button_execute_communication_between_plugins_example)

        # layout for plugins with own views
        self.plugin_widgets_layout = QVBoxLayout()
        self.layout.addLayout(self.plugin_widgets_layout)

        self.setLayout(self.layout)

    def add_plugin_widget(self, widget):
        # draw widget on layout
        self.plugin_widgets_layout.addWidget(widget)
