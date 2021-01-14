import json

with open("config_test.json") as config:
    config = json.load(config)

DRIVER_PATH = config["chrome_driver_path"]
URL = config["URL"]
