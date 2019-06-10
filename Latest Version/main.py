from mchoice import multiplechoice;
from addVocab import addVoc;
from writeItDown import writeIt;
from logIn import login;
import csv;

def parseDat(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f);
        temp = list(reader);
    return temp;
def menulist():
    print('1. Play Multiple Choice quiz');
    print('2. Play Write It Down! quiz');
    print('3. Add new question')
    print('4. Use another account');
    print('5. Exit');
def login():
    username = input('Username: ');
    password = input('Password: ');

    # Searching existence of username in tempuser
    found = False;
    while not(found):
        i = 0;
        while (i < len(tempuser)) and (username != tempuser[i][0]):
            i += 1;
        # (Output : i == len(tempuser) or username found);
        # print(i); {for testing}
        if (i == len(tempuser)):
            print('Username tidak ditemukan.');
            username = input('Username: ');
            password = input('Password: ');
        else:
            if (password == tempuser[i][1]):
                found = True;
                print('Log in berhasil. Selamat datang,',username);
                filename = username+'dat.csv'
            else:
                print('Password salah.');
                username = input('Username: ');
                password = input('Password: ');
    return parseDat(filename);

with open('userdat.csv','r') as f:
    reader = csv.reader(f);
    tempuser = list(reader);
    print('==========================================================');
    print(' _    __                 __          __                   ');
    print('| |  / /___  _________ _/ /_  __  __/ /___ _________  ___ ');
    print('| | / / __ \/ ___/ __ `/ __ \/ / / / / __ `/ ___/ _ \/ _ \ ');
    print('| |/ / /_/ / /__/ /_/ / /_/ / /_/ / / /_/ / /  /  __/  __/');
    print('|___/\____/\___/\__,_/_.___/\__,_/_/\__,_/_/   \___/\___/ ');
    print('==========================================================');
    print('Welcome to Vocabularee. Please log in to your account!');

temp = login();

menu = 0;
while not(menu == 5):
    if (menu == 0):
        print('==========================================================');
        print(' _    __                 __          __                   ');
        print('| |  / /___  _________ _/ /_  __  __/ /___ _________  ___ ');
        print('| | / / __ \/ ___/ __ `/ __ \/ / / / / __ `/ ___/ _ \/ _ \ ');
        print('| |/ / /_/ / /__/ /_/ / /_/ / /_/ / / /_/ / /  /  __/  __/');
        print('|___/\____/\___/\__,_/_.___/\__,_/_/\__,_/_/   \___/\___/ ');
        print('==========================================================');
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

        isPlay = 'y';
        while (isPlay.lower() == 'y'):
            multiplechoice(temp);
            print('Well done! do you want to play again? (Y/N)')
            isPlay = input();
            while not((isPlay.lower() == 'n') or (isPlay.lower() == 'y')):
                print('Please input \'N\' or \'Y\'');
                isPlay = input();
        menu = 0;
    elif (menu == 3):
        # print(menu); {just for testing}
        addVoc(filename);
        menu = 0;
    elif (menu == 2):
        isPlay = 'y';
        while (isPlay.lower() == 'y'):
            writeIt(temp);
            print('Well done! do you want to play again? (Y/N)')
            isPlay = input();
            while not((isPlay.lower() == 'n') or (isPlay.lower() == 'y')):
                print('Please input \'N\' or \'Y\'');
                isPlay = input();
        menu = 0;
    elif (menu == 4):
        print('You have logged out.')
        temp =login();
        menu = 0;
print('   ___                            __   __                    _    ');
print('  / __|    ___     ___      o O O \ \ / /   ___    _  _     | |   ');
print('  \__ \   / -_)   / -_)    o       \ V /   / _ \  | +| |    |_|   ');
print('  |___/   \___|   \___|   TS__[O]  _|_|_   \___/   \_,_|   _(_)_  ');
print('_|"""""|_|"""""|_|"""""| {======|_| """ |_|"""""|_|"""""|_| """ | ');
print('\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'./o--000\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'')