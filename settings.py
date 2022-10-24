from sys import modules
import yaml
import logging
"""
Класс конфигурации, который хранит в себе файл конфигурации в виде словаря
в поле all_settings
"""
class Settings:

    """
    Инициирующий метод, который задает состояние объекта класса Settings
    В поле объекта self.all_settings записывается значение передаваемого параметра all_settings
    """
    def __init__(self, all_settings):
        self.all_settings = all_settings

    """
    Метод get_modeules возвращает список имен модулей, описанных в файле конфигурации
    """
    def get_modules(self):
        logging.info('Getting all modules from settings')
        keys = list(self.all_settings['modules'].keys())
        logging.info('Found modules: %s' % keys)
        return keys

    """
    Метод get_metrics_for_module позволяет по названию модуля ('default' из примера конфигурации)
    получить список метрик, описанных для этого модуля в конфигурации
    """
    def get_metrics_for_module(self, module):
        #Проверяем, что модуль, для которого ищем метрики существует
        if (module in self.get_modules()):
            logging.info('Getting metrics for module %s' % module)
            #Получаем метрики для модуля с помощью работы со словарями из поля self.all_settings объекта класса Settings
            metrics = self.all_settings['modules'][module]['metrics']
            logging.info('For module %s found metrics: %s' % (module, [metric['name'] for metric in metrics]))
            return metrics
        else:
            #Возвращаем ошибку, если искомый модуль не описан в конфигурации
            logging.error('Unknown module %s' % module)

    """
    Метод __str__ позволяет представлять объект класса Settings в строковом виде
    """
    def __str__(self) -> str:
        return self.all_settings


"""
Метод load_settings поизводит чтение файла конфигурации, с помощью библиотеки pyyaml 
конвертирует его в словарь и передает полученный словарь в инициирующий метод класса Settings.
Результатом выполнения инициирующего метода является объект класса Settings.
"""
def load_settings(path='./config.yml'):
    stream = open(path, 'r').read()
    return Settings(yaml.safe_load(stream))
