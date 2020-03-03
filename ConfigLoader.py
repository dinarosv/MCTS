import json

def get_config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    
    nim = data["NIM"]
    ledge = data["Ledge"]
    verbose_mode = data["Verbose_mode"]
    return nim, ledge, verbose_mode