import csv
import sys

def calculateCost(dict):
    outCallsMin = 0
    smsNum = 0
    ph_number = sys.argv[1]

    for row in dict:
        if row['msisdn_origin'] == ph_number:
            outCallsMin += float(row['call_duration'])
            smsNum += int(row['sms_number'])
    if outCallsMin >=  20:
        outCallsMin -= 20
    
    return (outCallsMin + smsNum) * 2

def main():
    csvReader = csv.DictReader(open("data.csv","r"))
    cost = calculateCost(csvReader)
    print('%.2f' % cost,'руб.',end='')

if __name__ == '__main__':
    main()