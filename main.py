import sys
from PyQt5.QtWidgets import QApplication
from model import Model
from view import View
from presenter import Presenter
from plugin_loader import PluginLoader

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # load plugins
    plugin_loader = PluginLoader(plugin_directory='plugins')
    plugin_loader.load_plugins()

    # create mvp
    model = Model(plugin_loader)
    view = View()
    presenter = Presenter(model, view)

    # add and draw `layered_plugin`
    plugin_widget = model.execute_plugin('layered_plugin')
    if plugin_widget:
        view.add_plugin_widget(plugin_widget)

    # add and draw `textbox_plugin`
    textbox_plugin_widget = model.execute_plugin('textbox_plugin')
    if textbox_plugin_widget:
        view.add_plugin_widget(textbox_plugin_widget)

    view.show()
    sys.exit(app.exec_())
