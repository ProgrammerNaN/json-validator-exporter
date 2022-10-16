from sys import modules
import yaml
import logging

class Settings:

    def __init__(self, all_settings):
        self.all_settings = all_settings

    def get_modules(self):
        logging.info('Getting all modules from settings')
        keys = list(self.all_settings['modules'].keys())
        logging.info('Found modules: %s' % keys)
        return keys

    def get_metrics_for_module(self, module):
        if (module in self.get_modules()):
            logging.info('Getting metrics for module %s' % module)
            metrics = self.all_settings['modules'][module]['metrics']
            logging.info('For module %s found metrics: %s' % (module, [metric['name'] for metric in metrics]))
            return metrics
        else:
            logging.error('Unknown module %s' % module)

    def __str__(self) -> str:
        return self.all_settings


def load_settings(path='./config.yml'):
    stream = open(path, 'r').read()
    return Settings(yaml.safe_load(stream))
