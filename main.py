from mchoice import multiplechoice;
from addVocab import addVoc;
from logIn import login;
import csv;

def parseDat(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f);
        temp = list(reader);
    return temp;
def menulist():
    print('1. Play multiple choice');
    print('2. Add data');


with open('userdat.csv','r') as f:
    reader = csv.reader(f);
    tempuser = list(reader);

menu = 0;

if (menu == 0):
    print('==========================================================');
    print(' _    __                 __          __                   ');
    print('| |  / /___  _________ _/ /_  __  __/ /___ _________  ___ ');
    print('| | / / __ \/ ___/ __ `/ __ \/ / / / / __ `/ ___/ _ \/ _ \ ');
    print('| |/ / /_/ / /__/ /_/ / /_/ / /_/ / / /_/ / /  /  __/  __/');
    print('|___/\____/\___/\__,_/_.___/\__,_/_/\__,_/_/   \___/\___/ ');
    print('==========================================================');
    print('Welcome to Vocabularee. Please log in to your account!');

    #-------LOGIN---------#
    username = input('Username: ');
    password = input('Password: ');

    # Searching existence of username in tempuser
    found = False;
    while not(found):
        i = 0;
        while (i < len(tempuser)) and (username != tempuser[i][0]):
            i += 1;
        # (Output : i == len(tempuser) or username found);
        print(i);
        if (i == len(tempuser)):
            print('Username tidak ditemukan.');
            username = input('Username: ');
            password = input('Password: ');
        else:
            if (password == tempuser[i][1]):
                found = True;
                print('Log in berhasil. Selamat datang,',username);
                filename = username+'dat.csv'
                temp = parseDat(filename);
            else:
                print('Password salah.');
                username = input('Username: ');
                password = input('Password: ');

menulist();
menu = int(input('Select menu:'));

if (menu == 1):
    print('========================================');
    print('     __  ___      ____  _       __    ');
    print('    /  |/  /_  __/ / /_(_)___  / /__  ');
    print('   / /|_/ / / / / / __/ / __ \/ / _ \ ');
    print('  / /  / / /_/ / / /_/ / /_/ / /  __/ ');
    print(' /_/  /_/\__,_/_/\__/_/ .___/_/\___/  ');
    print('          ________   /_/    _         ');
    print('         / ____/ /_  ____  (_)_______ ');
    print('        / /   / __ \/ __ \/ / ___/ _ \ ');
    print('       / /___/ / / / /_/ / / /__/  __/');
    print('       \____/_/ /_/\____/_/\___/\___/ ');
    print('=========================================');
    multiplechoice(temp);
    print('Well done! do you want to play again?')
    
elif (menu == 2):
    print(menu);
    addVoc(filename);