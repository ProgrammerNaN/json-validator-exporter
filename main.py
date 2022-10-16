import logging
import settings
import sys

def configure():
    if (len(sys.argv) == 2):
        return settings.load_settings(sys.argv[1])
    else:
        return settings.load_settings()

def main():
    logging.basicConfig(level=logging.INFO)
    config = configure() 
    print(config.get_metrics_for_module('default'))

if __name__ == "__main__":
    main()