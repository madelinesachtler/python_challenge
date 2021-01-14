import os 
import csv 

#read in CSV file 
pybank_csv = os.path.join("..", "Resources","budget_data.csv")
#total = 0 

totalprofits = 0 
totalmonths = 0 
totalchange = 0 
previous = 0 
maxchange = 0 
maxmonth = ""
minchange = 9999999999 
minmonth = ""
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader, None)
    print(f"Header: {header}")

    for row in csvreader: 
        #print(row)

        totalmonths = totalmonths + 1 

        totalprofits = totalprofits + int(row[1])
        
        current = int(row[1])
        change = current - previous 

        if change > maxchange: 
            maxchange = change 
            maxmonth = row[0]

        if change < minchange: 
            minchange = change
            minmonth = row[0]
        

        previous = current 
        if totalmonths > 1: 
            totalchange = totalchange + change




    
    print(f'- - - - - - - - - - - - - - - - - - - - -')
    print(f"Financial Analysis")
    print(f'- - - - - - - - - - - - - - - - - - - - - ')

    print(f"Total Months: {str(totalmonths)}")
    print(f"Total Profits: {str(totalprofits)}")
    
    AverageChange = round(totalchange/(totalmonths-1),2)


    print(f"Average Change: ${str(AverageChange)}")
    print(f"Greatest Increase in Profits: {maxmonth} $({str(maxchange)})")     
    print(f"Greatest Decrease in Profits: {minmonth} $({str(minchange)})")    




