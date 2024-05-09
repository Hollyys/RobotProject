import requests
import time

def sender(file_path):
    url = 'http://192.168.120.36/command?commandText='
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] != '%':
                response = 'busy'
                while response != 'ok':
                    command = url + line
                    print(command)
                    response = requests.post(url)
                    time.sleep(1)