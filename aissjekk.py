#!/usr/bin/env python

import serial
import ais
import re
import math
import time
ser = serial.Serial("/dev/ttyUSB0", 38400)
clock = int(time.time())

while(True):
    line = ser.readline()
    line = line.decode('ISO-8859-1')
    if re.match("\!AIVDM,1", line):
        aismsg = line.split(',')
        try:
            aisdata = ais.decode(aismsg[5], int(aismsg[6][:1]))
        except:
            print(line)
            pass
        o = open("aislog", "a")
        o.write(time.strftime("%d/%m %H:%M:%S")+" "+str(aisdata['mmsi'])+"\n")
        print(time.strftime("%d/%m %H:%M:%S")+" "+str(aisdata['mmsi'])+"\n")
        o.close()
        #if aisdata['mmsi'] == 257412620:
        #    print('\n'+str(aisdata['mmsi']))
        #    for d in aisdata:
        #        print(d, aisdata[d])
        #    print(str(aisdata['mmsi'])+'\n')
            #o = open("aislogg", "a")
           # difference = int(time.time()) - clock
           # clock = int(time.time())
           # if(aisdata['id'] == 18):
           #     lat = aisdata['y']
           #     lon = aisdata['x']
           #     print(aisdata['mmsi'], lat, lon,  difference)
           #     o.write(str(aisdata['mmsi'])+" "+str(lat)+" "+str(lon)+" "+str(difference)+"s\n")
           # elif(aisdata['id'] == 24):
           #     if(aisdata['part_num'] == 0):
           #         print(aisdata['name'],  difference)
           #         o.write(str(aisdata['name'])+" "+str(difference)+"s\n")
#
#
#            else:
#                print("ID:"+str(aisdata['id']))
#                
#            o.close()
