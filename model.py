import csv

def get_people():
    with open("people.csv", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        sp = list(reader)
        return sp

def add(man):
    with open("people.csv", "a", encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(man)

def delete(number):
    with open("people.csv", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        sp = list(reader)
    if number < len(sp):
        del sp[number]
    
    with open("people.csv", "w", encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for row in sp:
            writer.writerow(row)