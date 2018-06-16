'''import csv
def openf(fname):
    with open(fname,newline='')as cvfile:
        line = csv.reader(cvfile,delimiter =',' ,  quotechar='|')
        for row in line:
            print(','.join(row))


openf('text.csv')'''