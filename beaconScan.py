from bluetooth.ble import BeaconService

import Beacon
import time
import csv
import dbFunctions

dbFunctions.createTable()
input_file = csv.DictReader(open("beaconStations.csv"))
beaconsList = []
beaconsRead = []
addressM = ""

for row in input_file:
    beaconsList.append(row)
for beacon in beaconsList:
    beacon["state"] = True
    beacon["read"] = False
station = 1
direction = True

DISCOVER_TIME = 5 # In seconds, scan interval duration.
service = BeaconService() # Start the service object as beacon service


def getMaxRssi():
    rssiM = -100
    beacon = Beacon.Beacon([0,0,0,0,-100],"")
    for beaconRead in beaconsRead:
        if int(beaconRead._rssi) > rssiM:
                rssiM = beaconRead._rssi
                beacon = beaconRead
    return beacon
    
while True:
    devices = service.scan(DISCOVER_TIME)
    # Scan the devices inside the beacon service
    for address, data in list (devices.items()): # Run for loop for the scanned beacons
        b = Beacon.Beacon(data, address) # Create the object b from class Beacon
        beaconsRead.append(b)
    
    for beacon in beaconsList:
        if addressM != getMaxRssi()._address and int(getMaxRssi()._rssi) >= -90 and beacon["BeaconMAC"] == getMaxRssi()._address:
            addressM = getMaxRssi()._address
            dataI = {}
            dataI["name"] = beacon["Station"]
            dataI["date"] = time.time()
            print(getMaxRssi()._address)
            dbFunctions.insertEvent(dataI)
            break
         


                    
            
        
 