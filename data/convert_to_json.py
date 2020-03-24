import csv, json
csvpath = 'gofundme.csv'
jsonpath = 'gofundme.json'


data={}
with open(csvpath) as csvfile:
	csvreader = csv.DictReader(csvfile)
	for rows in csvreader:
		id = rows['Link']
		data[id] = rows
		

with open(jsonpath, 'w') as jsonfile:
	jsonfile.write(json.dumps(data, indent=4))
