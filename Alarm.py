# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:22:53 2018

@author: AmatVictoriaCuramIII
"""

import webbrowser
import time
import math

url = 'https://www.youtube.com/watch?v=V2R0K7iX83E'
while True:
    try:
        userInput = input('How many hours until alarm goes off? ')
        totalhours = float(userInput)
        total = math.ceil(totalhours * 60 * 60)
        print('The alarm is set for ' + str(userInput) + ' hours.')
        time.sleep(total)
        webbrowser.open(url)
        break
    except ValueError:
        print('Not a number, try again.')