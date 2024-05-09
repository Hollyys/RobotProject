import requests
import time

def sender(file_path, TEST_MODE):
    url = 'http://192.168.120.36/command?commandText='
    with open(file_path, 'r') as file:
        cnt = 0
        for line in file:
            if line[0] != '%':
                command = url + line
                if TEST_MODE:
                    cnt += 1
                    print(f"Request{cnt}: {command}")
                    time.sleep(1)
                else:
                    while response != 'ok':
                        response = requests.post(command)
                        time.sleep(1)
                        response = 'busy'
            if TEST_MODE and cnt == 10:
                print('Sender test finished.\n')
                break