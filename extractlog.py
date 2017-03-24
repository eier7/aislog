#!/usr/bin/env python

import re


mmsi = []
startdate = ""
enddate = ""
gotstartdate = False
with open("aislog", "r") as f:
    for line in f:
        if(not gotstartdate):
            startdate = line.split(" ")[0]
            gotstartdate = True
        enddate = line.split(" ")[0]
        mmsi.append(line.split(" ")[1].replace("\n", ""))

mmsi = list(set(mmsi))
counter = 0
mmsia = []
for m in mmsi:
    counter = counter+1
    mmsia.append([str(counter), m])

o = open("plotlog", "w")
with open("aislog", "r") as d:
    for line in d:
        for n in mmsia:
            if(line.split(" ")[1].replace("\n", "") == n[1]):
                    o.write(line.split(" ")[0]+" "+n[0]+" "+n[1]+"\n")

o.close()
g = open("plot.gnuplot", "w")
g.write('set timefmt "%d/%m_%H:%M:%S"\n')
g.write("set xdata time\n")
g.write('set xrange ["'+startdate + '":"' + enddate + '"]\n')
g.write('set format x "%H:%M"\n')
g.write("unset ytics\n")
g.write("set yrange [-1:"+str(len(mmsia)+1)+"]\n")
g.write("set ytics font \"Arial, 4\"\n")
#for h in mmsia:
#    g.write("set label \""+h[1]+"\" at \""+enddate+"\","+h[0]+" offset -3,0,0 font \"Arial,3\"\n")
mytics = ""
for h in mmsia:
    mytics += '"'+h[1]+'" '+h[0]+','
g.write("set ytics (" + mytics + ')\n')
g.write('plot "plotlog" using 1:2 with dots title ""\n')

g.close()
