import logging
import settings
import sys
import requests

def configure():
    if (len(sys.argv) == 3):
        return settings.load_settings(sys.argv[1])
    else:
        return settings.load_settings()

def main():
    link()
    logging.basicConfig(level=logging.INFO)
    config = configure() 
    print(config.get_metrics_for_module('default'))

def link():
    logging.basicConfig(level=logging.INFO)
    req = requests.get(sys.argv[2])
    if req.status_code == 200:
        print(req.json())
    else:
        print(req.status_code)

if __name__ == "__main__":
    main()