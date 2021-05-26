'''
Author: TEO Cheng Guan

Simple remote control car. (Host)

This app runs on a host with WiFi connection in the same network as the RPI.

This app controls the RPI remote control car using inputs module.

'''

import datetime
import time
import importlib
import requests

import inputs

URL = "http://192.168.68.122:5000/move"

def main():
    while 1:
        try:
            events = inputs.get_gamepad()
        except inputs.UnpluggedError:
            print(f'Gamepad lost. Retrying...')
            events = []
            time.sleep(1)
            importlib.reload(inputs)
            continue
            
        except OSError as err:
            print(f'Gamepad lost. Retrying...OSError')
            events = []
            time.sleep(1)
            importlib.reload(inputs)
            continue

        except KeyboardInterrupt:
            print("Exiting...")
            break

        for event in events:
            #timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            #print(f"{timestamp}: {event.ev_type}-{event.code}-{event.state}")

            if (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==0):
                PARAMS = {'direction':'up'}
            elif (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==127):
                PARAMS = {'direction':'stop'}
            elif (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==255):
                PARAMS = {'direction':'down'}
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==0):
                PARAMS = {'direction':'left'}
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==127):
                PARAMS = {'direction':'stop'}
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==255):
                PARAMS = {'direction':'right'}

        print(PARAMS)
        r = requests.get(url = URL, params = PARAMS)

if __name__ == "__main__":
    main()
