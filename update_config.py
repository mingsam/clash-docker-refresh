import os
import json
import requests
import logging
import docker
import time

class ClashConfigUpdater():
    def __init__(self, config_url):
        self.config_url = config_url
        self.logger = self._init_logs_utils()
        
    def _init_logs_utils(self, log_path='./logs'):
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        
        time_now = time.time()
        logger = logging.getLogger("Clash Config Updater")
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("{}/test-{}.log".format(log_path, time_now))
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.info("Log Start.")
        return logger
    
    def get_new_config(self, config_path='./config'):
        if not os.path.exists(config_path):
            os.makedirs(config_path)

        respondse = requests.get(self.config_url, stream=True)
        respondse.raise_for_status()

        time_now = time.time()
        new_config_path = "{}/config-{}.yml".format(config_path,time_now)
        with open(new_config_path, "wb") as f:
            for chunk in respondse.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return new_config_path

    def merge_configs():
        pass
    
    def refresh_clash_docker():
        pass

    def check_clash():
        pass

if __name__ == "__main__":
    my_url = "./config/trojan_url.json"
    with open(my_url, "r") as f:
        url_dict = json.load(f)
    
    print(url_dict)
    
    test_clash_updater = ClashConfigUpdater(url_dict['url'])
    test_clash_updater.get_new_config()