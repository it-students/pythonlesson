import csv

with open('st.csv','r') as f:
    r = csv.reader(f,delimmiter=',')
    for row in r:
        print(','.join(row))