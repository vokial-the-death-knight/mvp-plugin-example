class Model:
    def __init__(self, plugin_loader):
        self.plugin_loader = plugin_loader
        self.plugins = {} 

    def execute_plugin(self, plugin_name):
        plugin_widget = self.plugin_loader.execute_plugin(plugin_name)
        if plugin_widget:
            self.plugins[plugin_name] = plugin_widget
        return plugin_widget

    def get_products_from_layered_plugin(self):
        layered_plugin_widget = self.plugins.get('layered_plugin')
        if layered_plugin_widget:
            products = layered_plugin_widget.get_products()
            return products
        else:
            return None

    def send_data_to_textbox_plugin(self, data):
        textbox_plugin_widget = self.plugins.get('textbox_plugin')
        if textbox_plugin_widget:
            textbox_plugin_widget.display_data(data)
