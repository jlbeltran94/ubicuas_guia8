from flask import Flask, render_template, request, redirect, url_for
import dbFunctions
import time
import csv

app = Flask(__name__)
beaconsList = []
input_file = csv.DictReader(open("beaconStations.csv"))
for row in input_file:
    beaconsList.append(row)
direction = 2
@app.route("/")
def main():
    events = dbFunctions.getAllEvents()    
    dates(events)
    return render_template('index.html', events=events)

@app.route("/dateSel")
def dateSel():    
    return render_template('dateSel.html')

@app.route("/date", methods=['GET', 'POST'])
def datesele():
    if request.method == 'POST':
        date = request.form['fecha_ini']
        print(date)
        return redirect(url_for('fechas', fecha=date))

@app.route("/equipo/<beacon>") # Get <beacon> as input variable for the function sensor
def sensor(beacon):
    equipo = changeString(beacon)
    events = dbFunctions.getAllEventsFrom(equipo)
    dates(events)
        
    return render_template('index.html', events=events)

@app.route("/lastStop") # Get <beacon> as input variable for the function sensor
def lastSensor():
    events = dbFunctions.getLast()
    dates(events)
        
    return render_template('index.html', events=events)

@app.route("/nextStop") # Get <beacon> as input variable for the function sensor
def nextStop():
    events = dbFunctions.getLast()    
    station = 4
    nextstation = 0
    for beacon in beaconsList:
        if events[0]["name"] == beacon["Station"]:
            station = int(beacon["Order"])
    if station == 4:
       global direction
       direction = 2
    if station == 1:
        global direction
        direction = 1
    if direction== 1 and station < 4:
        nextstation = station + 1
    if direction == 2 and station > 1:
        nextstation = station - 1    
    print("NEXTSTATION"+str(nextstation))
    for beacon in beaconsList:
        if int(beacon["Order"]) == nextstation:
            print("entro")
            events[0]["name"] = beacon["Station"]
    vel = getSpeed()
    timen = 1/vel
    events[0]["date"] = events[0]["date"] + timen
    dates(events)
    return render_template('index.html', events=events)

@app.route("/fecha/<fecha>") # Get <beacon> as input variable for the function sensor
def fechas(fecha):
    dateb = changeStringDate(fecha)
    events = dbFunctions.getAllEvents()
    fechas = []
    dates2(events)
    for event in events:
        if event['date'] == dateb:
            fechas.append(event)
    return render_template('index.html', events=fechas)

@app.route("/speed") # Get <beacon> as input variable for the function sensor
def speed():    
    events = dbFunctions.getLastP()
    seconds = events[0]["date"] - events[1]["date"]
    hour = seconds/3600
    vel = 1/hour
    

    return render_template('speed.html', vel=vel)

def getSpeed():
    events = dbFunctions.getLastP()
    seconds = events[0]["date"] - events[1]["date"]
    vel = 1/seconds
    return vel

def dates(events):
    for event in events:
        time1 = event['date']
        event['date'] = time.strftime("%Y/%m/%d %H:%M", time.localtime(time1))

def dates2(events):
    for event in events:
        time1 = event['date']
        event['date'] = time.strftime("%Y/%m/%d", time.localtime(time1))

def changeString(name):
    l = list(name)
    for i in range(0, len(l)):
        if l[i] == '_':
            l[i] = ' '                    
    s = "".join(l)    
    return s

def changeStringDate(name):
    l = list(name)
    for i in range(0, len(l)):
        if l[i] == '_':
            l[i] = '/'                    
    s = "".join(l)    
    return s

if __name__ == "__main__":
    app.run()