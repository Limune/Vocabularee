import csv;

def addVoc(filename):
    newQ = str(input('Input question you want to add: '));
    newA = str(input('Input answer of the question: '));
    temp = [newQ,newA];
    with open(filename,'a',newline='') as f:
        newFileWriter = csv.writer(f,lineterminator='\n');
        newFileWriter.writerow(temp);
    print('Adding success!');
