def login(tempuser, teuest):
    username = input('Username: ');
    password = input('Password: ');

    # Searching existence of username in tempuser
    found = False;
    i = 0;
    while not(found):
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
                tempquest = parseDat(filename);
            else:
                print('Password salah.');
                username = input('Username: ');
                password = input('Password: ');