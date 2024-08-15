import win32com.client # the module needed for win32 COM API functions
import time
import os
# -*- coding: utf-8 -*-

#Hinweis: CANape.dll beschreibt die COM-Schnittstelle von CANape. Bei der Installation wird sie normalerweise in der Registry eingetragen und somit die COM-Befehle
#		  unter HKEY-CLASSES-ROOT zB: 'CANape.Application' stehen. Wird dies bei der Installation net gemacht kann man es manuell mit dem Befehl -regsvr32 CANape.dll-
#		  in der Windowskonsole nachtraeglich noch machen.

canape = win32com.client.Dispatch('CANape.Application')
print('CANape dispatched.....')

canape.Open1(r"C:\Users\Public\Documents\Vector\CANape Examples 21.0\XCPDemo",1,50000,False) 	

dev = canape.Devices.Add("XCPsim","XCPsim.a2l","XCP",1)

XCP_1_Task = dev.Tasks("100ms")
XCP_1_Task.Channels.Add("channel1")

timeStamp = 0

print('Start the measurement.....')
canape.Measurement.Start()

for a in range(1,3):
    #Reading values of measurement signals by executing NextSample() before
    print('\n############################################################################################\n')
    print('Reading values of measurement signals NextSample() executed before\n')
    print('###############################################################################################\n')
    for i in range(1, 300):
        #arrayValues = XCP_1_Task.CurrentValues(timeStamp)
        arrayValues_2 = XCP_1_Task.NextSample(timeStamp)        
        #arrayValues = XCP_1_Task.CurrentValues(timeStamp)
        #print'Array current values obj.CurrentValues: ',arrayValues
        print('Array current values obj.NextSample: ',arrayValues_2)
        time.sleep(0.01)
        print ('\n')

time.sleep(1)
canape.Measurement.Stop()
print('\nStop the measurement.....\n')
print('\nExit CANape...Thank you for using!\n')
canape.Quit()
