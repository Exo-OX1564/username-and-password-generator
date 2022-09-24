import random, colorama
from colorama import Fore

full_name = input(Fore.LIGHTBLUE_EX + "Please enter your name: ").lower().split()
print('\n-------------------------------------------------------\n')
if len(full_name) > 1:
  first_letter = full_name[0][0]
  three_letters_surname = full_name[-1][:3].rjust(3, 'x')
  number = '{:03d}'.format(random.randrange (1,999))
  username = '{}{}{}'.format(first_letter, three_letters_surname, number)
  print(Fore.LIGHTGREEN_EX + f"[USERNAME GENERATED]" + Fore.RED + " -> "+ f"{username}")
  optiontosave = input(Fore.LIGHTBLUE_EX + 'Would you like to save this to ' + Fore.YELLOW + "usernames.txt" + Fore.RED + " -> " + Fore.LIGHTGREEN_EX + "(y/n): " + Fore.RESET)
  if optiontosave == "y" or optiontosave == "yes" or optiontosave == "Yes" or optiontosave == "YES":
    with open('usernames.txt', 'a') as file:
      file.write(f'[USERNAME] -> {username}\n')
  print(Fore.LIGHTBLUE_EX + '\nThanks for using the program -> Rerun me to generate more usernames!')
  exit()
  
    
