#!/bin/bash
echo "Updating IoT Hub handler script"

until ping -c1 azure.microsoft.com;
do sleep 5;
done;

curl -s -o /home/pi/smsEagle-iot-hub-handler.py https://raw.githubusercontent.com/nyss-platform-norcross/nyss-sms-gateway/master/SMSEagleIOTBridge/smsEagle-iot-hub-handler.py
res=$?
if test "$res" != "0"
then
    echo "Failed to update IoT Hub handler script"
else
    chmod +x /home/pi/smsEagle-iot-hub-handler.py
    echo "Successfully updated IoT Hub handler script"
    # save script version as latest commit id
    curl -s https://api.github.com/repos/nyss-platform-norcross/nyss-sms-gateway/commits/master | python3 -c "import sys, json; print(json.load(sys.stdin)['sha'])" > /home/pi/iot-hub-handler-version.txt
    # reload files on disk
    systemctl daemon-reload
fi