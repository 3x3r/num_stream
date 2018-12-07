import sys
import csv
import os

path='C:\\Python27/'
cars_in = 0
cars_out = 0
cars_un = 0
for rootdir, dirs, files in os.walk(path):
    for file in files:       
        if((file.split('.')[-1])=='csv'):
            csvpath = os.path.join(rootdir,file)
            print (os.path.join(rootdir,file))
            input_file = open(csvpath, "rb")
            rdr = csv.reader(input_file,delimiter=';')
#output_file = open("out.csv", "wb")
#wrtr = csv.writer(output_file)
            #line = 0
           # cars = 0
            for rec in rdr:
              if rec[5]=='1':
               cars_in+=1
              if rec[5]=='255':
               cars_out+=1
              if rec[5]=='0':
               cars_un+=1
 #print (rec[5])
# wrtr.writerow(rec)
print ("In camera ",cars_in)
print ("Out camera",cars_out)
print ("Unknown",cars_un)
input_file.close()
#output_file.close()
