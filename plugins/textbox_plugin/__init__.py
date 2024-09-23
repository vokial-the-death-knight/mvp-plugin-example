from .presentation import TextboxPluginWidget

class Plugin:
    def __init__(self):
        self.widget = None

    def init(self):
        self.widget = TextboxPluginWidget()
        return self.widget  
