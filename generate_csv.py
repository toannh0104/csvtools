import csv

with open ('test.csv', 'w') as f:
    twriter = csv.writer(f);
    i=1;
    twriter.writerow(['Agent ID']);
    for i in range (1, 300000): 
        twriter.writerow([i]);
        i = i + 1;
