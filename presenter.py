from PyQt5.QtWidgets import QMessageBox

class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # setup event listeners
        self.view.button_execute_console_log_plugin.clicked.connect(self.execute_console_log_plugin)
        self.view.button_execute_communication_between_plugins_example.clicked.connect(self.execute_read_from_layered_and_pass_to_textbox_click_handler)

    def execute_console_log_plugin(self):
        self.model.execute_plugin('console_log_plugin')

    def execute_read_from_layered_and_pass_to_textbox_click_handler(self):
        data = self.model.get_products_from_layered_plugin()
        if data is not None:
            self.model.send_data_to_textbox_plugin(data)
        else:
            QMessageBox.warning(self.view, 'Error', 'Something went wrong...')
