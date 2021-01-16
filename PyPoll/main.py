import os 
import csv 

#read in CSV file 
pypoll_csv = os.path.join("..", "Resources","election_data.csv")

candidates = {}
totalvotes = 0 
winnerofvotes = 0 
winnercandidate = ""


with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader, None)
    print(f"Header: {header}")

    for row in csvreader:

        totalvotes = totalvotes + 1 

        if row[2] not in candidates: 
            candidates[row[2]]=1 
        else: 
            candidates[row[2]] = candidates[row[2]] + 1 

f = open("pypoll.txt", "a")
print(f'- - - - - - - - - - - - - - - - - - - - - - - -', file =f)
print(f'Election Results ', file=f)
print(f'- - - - - - - - - - - - - - - - - - - - - - - -', file=f)
print(f'Total Votes:{str(totalvotes)}', file=f)
print(f'- - - - - - - - - - - - - - - - - - - - - - - -', file=f)



for key, value in candidates.items():
    if value > winnerofvotes: 
        winnerofvotes = value
        winnercandidate = key
    
   
   
   
    print(f"{key}: {round((value/totalvotes)*100, 2)}% ({value})", file=f)
print(f'- - - - - - - - - - - - - - - - - - - - - - - -', file=f)

print(f'Winner Candidate: {str(winnercandidate)}', file=f)
print(f'- - - - - - - - - - - - - - - - - - - - - - - -', file=f)
f.close()