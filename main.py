import csv, json, pandas as pd


fileTarget = open('file.json',)
jsonFile = json.load(fileTarget)

with open('NameYourCSV.csv','w') as turnIntoCSV:
    writeOnegaiDesu = csv.writer(turnIntoCSV)
    for offset in jsonFile['offset']:
        print(offset['c'])
        writeOnegaiDesu.writerow([offset['a'],offset['b'],offset['c'],offset['d']])
