import urllib2
import csv

googl_url = r'https://query1.finance.yahoo.com/v7/finance/download/GOOGL?period1=1547254374&period2=1549932774&interval=1d&events=history&crumb=AgrfwP3OJX1'

def filedownload(url):
    response = urllib2.urlopen(url)
    readFile = csv.reader(response)
    readFileStr = str(readFile)
    readFileSplit = readFileStr.split('\\n')
    fw = open('data.csv', 'w')
    for line in readFileSplit:
        fw.write(line)
    fw.close()

filedownload(googl_url)