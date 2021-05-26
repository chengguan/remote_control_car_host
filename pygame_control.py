'''
Author: TEO Cheng Guan

Simple remote control car. (Host)

This app runs on a host with WiFi connection in the same network as the RPI.

This app controls the RPI remote control car using pygame module.

'''

import sys
import time
import requests

import pygame

URL = "http://192.168.68.122:5000/move"

def main():
    pygame.init()

    pygame.joystick.init()
    clock = pygame.time.Clock()

    print(pygame.joystick.get_count())

    _joystick = pygame.joystick.Joystick(0)
    _joystick.init()

    while pygame.joystick.get_count():
        sent_command = False

        events = pygame.event.get()

        for event in events:
            print(f'{event}')

            if event.type == pygame.JOYAXISMOTION:
                if (event.axis == 1) & (int(event.value) < 0):
                    print('Up pressed')
                    PARAMS = {'direction':'up'}
                    sent_command = True
                elif (event.axis == 1) & (int(event.value) == 0):
                    print('Up/down release')
                    PARAMS = {'direction':'stop'}
                    sent_command = True
                elif (event.axis == 1) & (int(event.value) > 0):
                    print('Down pressed')
                    PARAMS = {'direction':'down'}
                    sent_command = True
                elif (event.axis == 0) & (int(event.value) < 0):
                    print('Left pressed')
                    PARAMS = {'direction':'left'}
                    sent_command = True
                elif (event.axis == 0) & (int(event.value) == 0):
                    print('Left/right release')
                    PARAMS = {'direction':'stop'}
                    sent_command = True
                elif (event.axis == 0) & (int(event.value) > 0):
                    print('Right pressed')
                    PARAMS = {'direction':'right'}
                    sent_command = True

        if sent_command:
            print(PARAMS)
            r = requests.get(url = URL, params = PARAMS)
        clock.tick(30)

    PARAMS = {'direction':'stop'}
    r = requests.get(url = URL, params = PARAMS)

if __name__ == "__main__":
    main()
