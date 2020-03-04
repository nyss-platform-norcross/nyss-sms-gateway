import nyssIotBridge
import requests
import time
import logging

# Python 3 needs to be installed on the SMSEagle to start this script, using "do-not-use_apt-get"
# do-not-use_apt-get update
# do-not-use_apt-get install python3
# do-not-use_apt-get install python3-pip
# pip3 install azure-iot-device

#The connection string can be found in azure iot hub 
conn_str = "
login = ""
cred = ""

logging.basicConfig(
    filename='/var/log/iot-bridge-log.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

def send_sms(params):
    params["login"] = login
    params["pass"] = cred   
    return str(requests.get('https://localhost/index.php/http_api/send_sms', params=params, verify=False))

if __name__ == "__main__":
    #logging.basicConfig(filename='/var/log/iot-bridge-log.log', level=logging.DEBUG)
    nyssIotBridge.init(send_sms, conn_str)
    while True:
        time.sleep(1)
