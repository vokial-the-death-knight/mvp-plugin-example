import sys
import os
import importlib

class PluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.plugins = {}

    def load_plugins(self):
        sys.path.insert(0, self.plugin_directory)

        for item in os.listdir(self.plugin_directory):
            path = os.path.join(self.plugin_directory, item)
            if item == '__pycache__':
                continue  
            if os.path.isdir(path):
                module_name = item
            elif item.endswith('.py') and item != '__init__.py':
                # just .py file (sample plugin)
                module_name = item[:-3]
            else:
                continue

            try:
                module = importlib.import_module(module_name)
                plugin_class = getattr(module, 'Plugin')
                plugin_instance = plugin_class()
                self.plugins[module_name] = plugin_instance
            except Exception as e:
                print(f"Could not load plugin {module_name}: {e}")

        sys.path.pop(0)

    def execute_plugin(self, plugin_name):
        plugin = self.plugins.get(plugin_name)
        if plugin:
            return plugin.init()
        else:
            print(f"Plugin {plugin_name} not found.")
            return None