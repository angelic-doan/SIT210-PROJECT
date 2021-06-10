import requests
import json

import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)

if __name__ == "__main__":
    # write_key='RALPPPSP4M0DA84P'
    # read_key='MPEMPZW9062ODK81'
    # channel = 1409969
    
    channel = 1411798
    read_key='TR2GUSNPFHCUNNTX'
    write_key='ZQPPUJL0AGN0M3HB'
    
    url = f'https://api.thingspeak.com/channels/{channel}/fields/1.json?api_key={read_key}&results=1'
    while True:
        response = requests.get(url)
        reed_json = json.loads(response.text)
        reed_status = reed_json['feeds'][0]['field1']
        print(reed_json['feeds'][0]['created_at'], ' ', reed_status)
        if int(reed_status):
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)