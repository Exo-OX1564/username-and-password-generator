import string, os, time, colorama
from colorama import Fore
try:
  import requests
except ImportError:
  input(Fore.RED+
  f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
  exit()
try:  # Setup try statement to catch the error
  import numpy  # Try to import requests
except ImportError:  # If it has not been installed
  # Tell the user it has not been installed and how to install it
  input(Fore.RED+
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
  exit()

# check if user is connected to internet
url = "https://github.com"
try:
    response = requests.get(url)  # Get the responce from the url
except requests.exceptions.ConnectionError:
    # Tell the user
    input(Fore.RED + "You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  # Exit program




chars = []
chars[:0] = string.ascii_letters + string.digits + string.punctuation
c = numpy.random.choice(chars, size=[1, 16])
for s in c:
  try:
    password = ''.join(x for x in s)
  except Exception as exc:
    print(exc)
  print(Fore.LIGHTGREEN_EX + f"[PASSWORD GENERATED]" + Fore.RED +  " -> " + Fore.LIGHTBLUE_EX + f"{password}" + Fore.RESET + "\n------------------------------------------------\n")
  save = input(Fore.LIGHTBLUE_EX + 'Would you like to save this to ' + Fore.YELLOW + "passwords.txt" + Fore.RED + " -> " + Fore.LIGHTGREEN_EX + "(y/n): " + Fore.RESET)
  if save == "y" or save == "yes" or save == "Yes" or save == "YES":
    print("------------------------------------------------\n")
    with open('passwords.txt', 'a') as file:
      file.write(f'[PASSWORD] -> {password}\n')
  print(Fore.LIGHTBLUE_EX + '\nThanks for using the program -> Rerun me to generate more passwords!')
  exit()
