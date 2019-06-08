# Multiple Choice Quiz Module
# Module used in multiple section in main program

# Variable and Modules
import random;
"""
listq : list of string;
lista : list of string
"""

# Algorithm
# Initialization


# Fill List of Answer and List of Question from data

def multiplechoice(temp):
    listq = []
    lista = []

    for i in range(1, len(temp)):
        listq.append(temp[i][0]);
        lista.append(temp[i][1]);

    # Generating random question from the list q
    print('How many question do you want?');
    p = input();
    isIntabove0 = False;

    while not(isIntabove0):
        try:
            val = int(p);
        except ValueError:
            print("That's not an integer!")
            print('Input integer more than 0!');
            p = input();
            continue #Wait... that's illegal!!!

        if (int(p) > 0):
            isIntabove0 = True;
        else:
            print('Input integer more than 0!');
            p = input();

    p = int(p);

    corCount = 0;
    wroCount = 0;
    for i in range(p):
        question = random.choice(listq);
        icount = 0;
        while (icount < len(listq)-1) and (question != listq[icount]):
            icount += 1;
        """Output : icount = index of question"""
        
        temp1 = [lista[icount]];
        #print(question);
        #print(temp1);
        if (len(lista) >= 5):
            for x in range(4):
                found = True;
                while (found):
                    temp2 = random.choice(lista);
                    found = False;
                    itemp1 = 0;
                    while (not(found)) and (itemp1<len(temp1)):
                        if (temp2 == temp1[itemp1]):
                            found = True;
                        else:
                            itemp1 += 1;
                temp1.append(temp2);
        '''else:
            for x in range(len(lista)):
                found = True;
                while (found):
                    temp2 = random.choice(lista);
                    found = False;
                    itemp1 = 0;
                    while (not(found)) and (itemp1<len(temp1)):
                        if (temp2 == temp1[itemp1]):
                            found = True;
                        else:
                            itemp1 += 1;
                temp1.append(temp2);''' 
        #^Not working. I don't know why
        #print(temp1);
        random.shuffle(temp1);
        #print(temp1);
        answera = temp1[0];
        answerb = temp1[1];
        answerc = temp1[2];
        answerd = temp1[3];
        answere = temp1[4];

        # Print Question and Multiple Choice
        print(question);
        print('A. ',answera);
        print('B. ',answerb);
        print('C. ',answerc);
        print('D. ',answerd);
        print('E. ',answere);

        tempAns = input('Your Answer: ');
        while not((tempAns == 'A') or (tempAns == 'a') or (tempAns == 'B') or (tempAns == 'b') or (tempAns == 'C') or (tempAns == 'c') or (tempAns == 'D') or (tempAns == 'd') or (tempAns == 'E') or (tempAns == 'e')):
            print('Your input is not valid');
            tempAns = input('Your Answer: ');

        if (tempAns == 'A') or (tempAns == 'a'):
            answer = answera;
        elif (tempAns == 'B') or (tempAns == 'b'):
            answer = answerb;
        elif (tempAns == 'C') or (tempAns == 'c'):
            answer = answerc;
        elif (tempAns == 'D') or (tempAns == 'd'):
            answer = answerd;
        else:
            answer = answere;

        correct = answer == lista[icount];

        if correct:
            corCount += 1;
            print('Correct!');
        else:
            wroCount += 1;
            print('Wrong!');

    print('Correct answer: ', corCount);
    print('Wrong answer: ', wroCount);
    print('Your Score: ',round(corCount*100/p));