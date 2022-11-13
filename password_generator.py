# chars > 8 and chars <= 16
# at least one capital letter (ASDDFG)
# at least one number (0 - 9)
# at least one lower letter
import random

#password generator
def ps_generator():
    password_length = random.randint(9,16)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    #convert to uppercase
    letters_uppercase = []
    for letter in letters:
        letter_uppercase = letter.upper()
        letters_uppercase.append(letter_uppercase)

    #list with all allowed options
    all_options = letters + numbers + letters_uppercase

    #generate password
    password_list= []
    while len(password_list) != password_length:
        password_list.append(random.choice(all_options))
        password=''.join(password_list)

    #make sure that the condition are complied
    if password.isalpha():
        element_position1 = random.randint(0,password_length-1)
        password_list[element_position1] = str(random.randint(0,10))
    if password.isupper():
        element_position2 = random.randint(0,password_length)
        while element_position2 == element_position1:
            element_position2 = random.randint(0,password_length-1)
        password_list[element_position2] = random.choice(letters)
    if password.islower():
        element_position3 = random.randint(0,password_length-1)
        while element_position3 == element_position1 or element_position3 == element_position2:
            element_position3 = random.randint(0,password_length)
        password_list[element_position3] = random.choice(letters_uppercase)

    password=''.join(password_list)
    return password

#menu
print('\nWELCOME')

def menu():
    option = (input('''\nChoise your option:
             1. Generate password
             2. Get password
             3. Exit
      Your option: '''))
    return option
user_option=menu()

#option1
def generator(app,option):
    user_passwords = ''
    passw = ps_generator()
    if option==1:
        print(f'Your new password for {app} is {passw}')
    return(app+' '+passw+'\n')

#option2
def get(list_pass,app,option):
    if app in list_pass:
        position_app=list_pass.index(app)
        passw=list_pass[position_app+1]
        if option==1:
            print(f'Your password for {app} is {passw}')
    else:
        print(f'You don´t have password for {app} yet')
        passw=''
    return passw

#option yes
def replace(app, old_pass):
    with open('pass_file.txt', 'r+') as file:
        ps_list = file.readlines()
        old_info=app+' '+old_pass+'\n'
        position_line = ps_list.index(old_info)
        new_info=generator(app,2)
        while len(old_info)!=len(new_info):
            new_info = generator(app,2)
        ps_list[position_line]=new_info
        file.seek(0)   #lleva al cursor al punto 0 del txt
        file.writelines(ps_list)
        new_info_ls=new_info.split()
        print(f'Your new password for {new_info_ls[0]} is {new_info_ls[1]}')
    return (ps_list)

#create txt
def extern_file(app_password):
    with open('pass_file.txt', "a") as file:
        file.write(str(app_password))

#read results
def read_file():
    with open('pass_file.txt', 'r') as file:
        ps_list=file.read().split()
    return (ps_list)

extern_file('')
while user_option!='3':
    if user_option=='1':
        app_name = input('\nEnter app name: ').lower()
        pass_list = read_file()
        if app_name in pass_list:
            print(f'You already have a password for {app_name}')
            choise=input('Do you want to replace it? (y/n): ').lower()
            while choise!='n' and choise!='y':
                choise=input('Invalid character, please enter "y" or "n": ').lower()
            if choise=='n':
                get(read_file(), app_name,1)
            else:
                old_passw=get(pass_list, app_name,2)
                replace(app_name,old_passw)
        else:
            extern_file(generator(app_name,1))
    elif user_option=='2':
        x=1
        app_name = input('\nEnter app name: ').lower()
        get(read_file(), app_name,x)
    else:
        print('Invalid option, try again.')
    user_option=menu()

print('\nBye Bye')