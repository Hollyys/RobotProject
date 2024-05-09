import requests

def sender(file_path):
    url = 'http://192.168.120.36/command?commandText='
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] != '%':
                command = url + line
                # print(command)