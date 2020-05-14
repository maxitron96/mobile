import csv
import sys

def calculateCost(stats,ip):
    traffic = 0
    for item in stats:
        if len(item) == 5:
            if item[1].find(ip) != -1:
                trafficString = item[3]
            elif item[2].find(ip) != -1:
                trafficString = item[4]
            if trafficString.find('M') == -1:
                traffic += int(trafficString)
            else:
                traffic += float(piceOfTraffic[:piceOfTraffic.find('M')]) * 1024 * 1024
    return '%.2f' % (traffic / 1024 / 1024)
        
def main():
    with open('traffic.csv','r') as csvTrafic:
        cost = calculateCost(csv.reader(csvTrafic),sys.argv[1])
        print(cost)

if __name__ == '__main__':
    main()