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

#key = ac517886-483b-45cb-a854-64be7acc3ff4
#bus route B61

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtakey, busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data1 = json.loads(data)
print('Bus Line: ' + busline)
my_list = data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']\
[0]['VehicleActivity']
#(len(my_list), my_list[0].keys())
active_buses = (len(my_list))
print('Number of active buses: ' + str(active_buses)) 
for i, it in enumerate(my_list):
 	longitude_bus = (it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
 	latitude_bus = (it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
	print('Bus '+ str(i)+' is at latitude ' + str(latitude_bus) + ' and longitude ' + str(longitude_bus))
 


 	

