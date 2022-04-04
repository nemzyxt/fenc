# Author : Nemuel Wainaina
# Simple script that generates Base64 string of a supplied file
# Have fun ...

from colorama import init, Fore
import base64
import os
import sys

# colors ...
init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

# Generate the Base64 string and print it out
def encode_file(file):
    with open(file, "rb") as f:
        content = f.read()
    try:
        output = base64.b64encode(content)
    except Exception as e:
        print(f"{RED}[!] An error occurred :: {e} {RESET}")
    else:
        # success
        print(f"{GREEN}[*] Success ! {RESET}")
        print(f"=> {content}")

if __name__ == "__main__":
    file = None
    
    if len(sys.argv) == 1:
        print("Usage : python3 fenc.py <FILE_NAME>")
        print("[$] The file is required")
        exit(0)
    elif len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print("Usage : python3 fenc.py <FILE_NAME>")
        print("[$] Too many arguments")
        exit(0)

    # Some checks on the supplied file ...

    # file exists 
    if not os.path.exists(file):
        print(f"{RED}[!] The file {file} could not be found ! {RESET}")
        exit(0)
    
    # file is actually a file and not a directory
    if not os.path.isfile(file):
        print(f"{RED}[!] The supplied path doesn't point to a file ! {RESET}")
        exit(0)

    # we have read permissions on the file
    if not os.access(file, os.R_OK):
        print(f"{RED}[!] Access to the file is denied ! {RESET}")
        exit(0)

    encode_file(file)