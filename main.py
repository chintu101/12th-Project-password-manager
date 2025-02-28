import random
import re
import os
import shutil

global numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
global lowercase_char
lowercase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                  'z']

global upperchase_char
upeercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                  'Z']

global special_char
special_char = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']
punctuations = ['?', '.', ',', '!']

global random_int, random_int1, randomint_2, random_int3, random_int3
global random_lowerchasechar, random_lowerchasechar1, random_lowerchasechar2, random_lowerchasechar3

global random_uppercasechar, random_uppercasechar1, random_uppercasechar2, random_uppercasechar3
global random_specialchars, random_specialchars1, random_specialchars2, random_specialchars3
random_int = random.choice(numbers)
random_int1 = random.choice(numbers)
random_int2 = random.choice(numbers)
random_int3 = random.choice(numbers)
random_lowercasechar = random.choice(lowercase_char)
random_lowercasechar1 = random.choice(lowercase_char)
random_lowercasechar2 = random.choice(lowercase_char)
random_lowercasechar3 = random.choice(lowercase_char)
random_uppercasechar = random.choice(upeercase_char)
random_uppercasechar1 = random.choice(upeercase_char)
random_uppercasechar2 = random.choice(upeercase_char)
random_uppercasechar3 = random.choice(upeercase_char)
random_specialchars = random.choice(special_char)
random_specialchars1 = random.choice(special_char)
random_specialchars2 = random.choice(special_char)
random_specialchars3 = random.choice(special_char)


def create_func():
    a = open("passwords.txt", "a+")


def view_func():
    a = open("passwords.txt", "r")
    print(a.read())


def write_func():
    a = open("passwords.txt", "w")

    print(a.write())


def phone_number(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    numbercheck = re.compile("(0|91)?[7-9][0-9]{9}")
    return numbercheck.match(s)

    # Driver Code

    s = "347873923408"
    if (numbercheck(s)):
        print("Valid Number")
    else:
        print("Invalid Number")


def check(gmail):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email = input("enter email :")

    if (re.search(regex, email)):
        print("Valid Email")
        return (email)
    else:
        print("Invalid Email")
        check(gmail)


def del_func():
    if os.path.exists("passwords.txt"):
        os.remove("passwords.txt")
        print("sucessful")
        exit()
    else:
        print("file does not exist")
        exit()


def copytoanother_file_remove_exisitingfile():
    currentfile = input("enter file path")
    newfile = input("enter file path")
    shutil.copyfile(currentfile, newfile)

    if os.path.exists(currentfile):
        os.remove(currentfile)


def copytoanother_file_keep_exisitingfile():
    currentfile = input("enter file path")
    newfile = input("enter file path")
    shutil.copyfile(currentfile, newfile)


def password_generator():
    domainname = str(input("enter domain name :"))
    username = str(input("enter username :"))


def intermediate_password():
    temp_pass = random_int + random_int1 + random_int2 + random_int3 + random_lowercasechar + random_lowercasechar1 + random_lowercasechar2 + random_lowercasechar3 + random_uppercasechar + random_uppercasechar1 + random_uppercasechar2 + random_uppercasechar3 + random_specialchars + random_specialchars1 + random_specialchars2 + random_specialchars3
    return temp_pass


def final_password():
    a = intermediate_password()
    a = list(a)
    a_random = random.shuffle(a)
    a = ''.join(a)
    print("password:", a)
    return a


def instagram():
    check(gmail)

    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["instagram \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


# write_func(password)
def facebook():
    check(gmail)
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["facebook \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def twitter():
    check(gmail)
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["twitter \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def netflix():
    check(gmail)
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["netflix \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def amazon():
    check(gmail)
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["amazon \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def gmail():
    check(gmail)
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = ["gmail \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def reddit():
    check(gmail)
    a = final_password()
    b = reddit_passcheck(a)
    while b == False:
        a = final_password()
        b = reddit_passcheck(a)
    reddit_pass = a

    file1 = open("passwords.txt", "w")
    L = ["reddit \n", f"password: {reddit_pass}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


def reddit_passcheck(a):
    y = []
    for x in final_password():
        y = y.append(x)
    i = 0
    newvar = True
    while i < len(y):
        if [y[i]] != [y[i + 1]]:
            i = i + 2
            newvar = True
        else:
            newvar = False
            break
        return newvar


def new_accnt_details():
    check(gmail)
    domain = input("enter domain:")
    password = final_password()
    file1 = open("passwords.txt", "w")
    L = [f"{domain} \n", f"password: {password}\n", f"gmail:{gmail}\n"]
    file1.writelines(L)
    file1.close()


# starting display messages

print("Welcome to password Generator and Manager!")
print("press the key to perform the required action!")
print("checking file instance")
print("1.generate a password"
      "\n2.managing password saves"
      "\n3.file settings"
      "\n4.add an existing account for saving"
      "\n5.exit program")
action = input("enter key :")

if (action == '1'):

    print(
        "\nWhich of the following sites would you like to generate a password for:\n1.instagram\n2.facebook\n3.twitter\n4.netflix\n5.reddit\n6.amazon\n7.gmail\n8.other")
    key = input("enter key :")

    if (key == '1'):
        instagram()






    elif (key == '2'):
        facebook()
    elif (key == '3'):
        twitter()
    elif (key == '4'):
        netflix()
    elif (key == '5'):
        reddit();
    elif (key == '6'):
        amazon()
    elif (key == '7'):
        gmail()
    elif (key == "8"):
        new_accnt_details()
    else:
        print("key does not match!")
        exit()










elif (action == '2'):
    print("1.view saved passwords"
          "\n2.edit saved passwords")
    keyforaction_2 = input("enter key:")

    if (keyforaction_2 == "1"):
        view_func()
    elif (keyforaction_2 == "2"):
        write_func()
    else:
        print("thats not a valid key!")
        exit()
elif (action == '3'):

    print("\nchoose the following actions: "
          "\n1.delete file"
          "\n.copy data to another file and delete existing file"
          "\n3.copy data to a new file and keep existing file")

    key = input("enter key :")
    if (key < '1' or key > '4'):
        print("\nplease choose a valid key")
        exit()
    elif (key == "1"):
        del_func()

    elif (key == '2'):

        print("\nAre you sure want to permanently delete this file and move dta to a new file")
        key = input("1.yes"
                    "\n2.no")
        if key == '1':

            copytoanother_file_remove_exisitingfile()
        else:
            exit()


    elif (key == '3'):
        print("\nAre you sure want to permanently delete this file and move data to a new file")
        key = input("1.yes"
                    "\n2.no")
    if key == '1':
        copytoanother_file_keep_exisitingfile()
    else:
        exit()




elif (action == '4'):
    new_accnt_details()


elif (action == '5'):

    exit()
