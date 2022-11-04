# chars > 8 and chars <= 16
# at least one capital letter (ASDDFG)
# at least one number (0 - 9)
# at least one lower letter
import random

password_length = random.randint(9,17)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
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
print(password)