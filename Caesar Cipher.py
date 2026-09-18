import string 
print("== Caesar Cipher Tool ==\n[1] Encrypt Message\n[2] Decrypt Message")
print('_'*20)
user_choice = int(input('Select an option (1/2) : '))
if user_choice != 1 and user_choice != 2 :
         print('⚠️ Invalid input! Please choose from the available options only ! ' )
         exit()
user_message = input('\nEnter a message : ')
shift_number = int(input('Enter a shift number : '))
def final_message(choice,message,number) :
   
    result = ''
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    for x in message :
        if x not in string.ascii_letters :
                   result += x 
                   continue 
        if x in uppercase_letters :
             original = uppercase_letters.index(x)
             if choice == 1 :
              new = (original + number) % 26 
              result += uppercase_letters[new]
             elif choice == 2 :
              new = (original - number) % 26
              result += uppercase_letters[new]
        elif x in lowercase_letters :
               original = lowercase_letters.index(x)
               if choice == 1 :
                new = (original + number) % 26 
                result += lowercase_letters[new]
               elif choice == 2 :
                new = (original - number) % 26 
                result += lowercase_letters[new]
    return result
print(final_message(choice=user_choice,message=user_message,number=shift_number))