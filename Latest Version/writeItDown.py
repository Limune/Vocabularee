import random;

def writeIt(temp):
    listq = []
    lista = []

    for i in range(1, len(temp)):
        listq.append(temp[i][0]);
        lista.append(temp[i][1]);

    # Generating random question from the list q
    print('How many question do you want? (Max:',len(listq),')');
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
    tempq =[];
    for i in range(p):
        found = True;
        while (found):
            question = random.choice(lista);
            found = False;
            itempq = 0;
            while (not(found)) and (itempq<len(tempq)):
                if (question == tempq[itempq]):
                    found = True;
                else:
                    itempq += 1;
        tempq.append(question);

        #print(tempq);
        print(question);

        icount = 0;
        while (icount < len(lista)-1) and (question != lista[icount]):
            icount += 1;
        """Output : icount = index of question"""
        print('');
        answer = input('Type your answer: ');

        if (answer.lower() == listq[icount]):
            print('Correct!');
            corCount += 1;
        else:
            print('Wrong!');
            wroCount += 1;

    print('Correct answer: ', corCount);
    print('Wrong answer: ', wroCount);
    print('Your Score: ',round(corCount*100/p));
