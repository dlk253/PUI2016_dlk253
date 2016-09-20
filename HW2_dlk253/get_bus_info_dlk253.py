from __future__ import print_function
import json
import urllib2 
import os
import sys
import numpy
import pylab as pl
import pandas as pd

mtakey = sys.argv[1]
busline = sys.argv[2]
csv = sys.argv[3]

#key = ac517886-483b-45cb-a854-64be7acc3ff4
#bus route B61
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtakey, busline)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data1 = json.loads(data)

if not len(sys.argv) == 4:
    print("Invalid number of arguments")
    sys.exit()
csv = open(sys.argv[3], "w")
csv.write('Latitude, Longitude, Stop Name, Stop Status'+'\n')  
my_list = data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']\
[0]['VehicleActivity']
my_otherlist = data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']\
[0]['VehicleActivity']#[0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
for i, it in enumerate(my_list):
 	longitude_bus = (it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
 	latitude_bus = (it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
 	stop_name = (it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
 	stop_status = (it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
 	['Distances']['PresentableDistance'])
	csv.write(str(latitude_bus) + ', ' + str(longitude_bus)+', ' + str(stop_name)+', ' + str(stop_status)+'\n')


#write to file, identical if you want to print on the screen - write is a function of the file that you have opened.
#pandas, buffer put above before the loops, write function, look at email/ui notebooks 



 	

