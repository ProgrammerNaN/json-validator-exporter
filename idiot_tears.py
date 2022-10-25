import yaml



class SettingsForExp:


    def __init__(self, settings): # dict из config.yml
        self.settings = settings # свойства, которыми обладает объект класса

    def get_modules(self): 
        module = self.settings['modules'] #вытащить то что внутри modules
        print(module)
        return module

    def get_restriction(self, module_for):
        modules = self.get_modules() # вытащит default и not_default
        current_module = modules[module_for]  #вытащить то что укажем при вызове функции в параметрах ('defalt') например
        metrics = current_module['metrics'] #вытащить метрики
        m1 = metrics[0] # получили содержимое первого элемента в списке
        restrict = m1['restrictions']
        print(restrict)
        return restrict


    
    
def path_settings(path='./config.yml'):
    conf = open(path, 'r') # r-Open for text file for reading text (конфиг стал читаем)
    data = conf.read() #чтение 
    return yaml.safe_load(data) # Чтение из YAML, возаращет ключ:значение


config_dict = path_settings() # config_dict это обработанный конфиг, приведенный к словарю
config = SettingsForExp(config_dict) # в качестве экземпляра функции settings=словарь из config_dict
# modules = config.get_modules() # вытащит default и not_default и все внутри них и сделает принт и вернет значения
config.get_restriction('default')
     
