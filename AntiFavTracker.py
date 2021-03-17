import os
import sys
import time

fpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons')

try:
    if sys.argv[1] == "-force":
        os.system("TASKKILL /f  /IM  CHROME.EXE")
        time.sleep(1)
except IndexError:
    pass

if os.path.exists(fpath):
    try:
        os.remove(fpath)
        print("\"Favicons\" file has been deleted")
    except PermissionError:
        print("Unable to delete the file \"Favicon\" because Chrome is open, close Chrome and try again!")
else:
    print(f"\"{fpath}\" file does not exist")

fjpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons-journal')

try:
    os.remove(fjpath)
    print("\"Favicons-journal\" file has been deleted")
except PermissionError:
    print("Unable to delete the file \"Favicon-journal\" because Chrome is open, close Chrome and try again!")
except FileNotFoundError:
    print(f"\"{fjpath}\" file does not exist")


sys.stdout.write("Exiting in 3")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write("2")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write("1")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.33)
sys.stdout.write(".")
sys.stdout.flush()