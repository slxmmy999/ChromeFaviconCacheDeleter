import os
import sys
import time

fpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons')

try:
    if sys.argv[1] == "-force":
        os.system("TASKKILL /f  /IM  CHROME.EXE")
        time.sleep(1)
except IndexError:
    print("No aruments!")

if os.path.exists(fpath):
    try:
        os.remove(fpath)
        print("File deleted")
    except PermissionError:
        print("Unable to clear Favicon cache because Chrome is open, close Chrome and try again!")
else:
    print("File does not exist")

fjpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons-Journal')

if os.path.exists(fpath):
    try:
        os.remove(fjpath)
        print("File deleted")
    except PermissionError:
        print("Unable to clear Favicon-Journal because Chrome is open, close Chrome and try again!")
else:
    print("File does not exist")

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