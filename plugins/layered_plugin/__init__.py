from .presentation import PluginWidget

class Plugin:
    def __init__(self):
        self.widget = None

    def init(self):
        self.widget = PluginWidget()
        return self.widget 
