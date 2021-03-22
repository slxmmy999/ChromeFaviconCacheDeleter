import os
import sys
import time
from datetime import datetime

today = datetime.now()
today = today.strftime("%m-%d-%Y_%H%M%S.log")
logpath = os.path.join("log", today)
logfail = False

try:
    open(logpath, "x")
except Exception as e:
    print("Error occurred when creating log file: ", e)
    logfail = True

fpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons')

try:
    if sys.argv[1] == "-force":
        os.system("TASKKILL /f  /IM  CHROME.EXE")
        time.sleep(1)
        with open(logpath, "a") as f:
            f.write("Log: Chrome kiled sucessfully\n")
except IndexError:
    with open(logpath, "a") as f:
            f.write("Log: No arguments passed, step ignored\n")

if os.path.exists(fpath):
    try:
        os.remove(fpath)
        print("\"Favicons\" file has been deleted")
        with open(logpath, "a") as f:
            f.write(f"Log: \"{fpath}\" file has been deleted\n")
    except PermissionError:
        print("Unable to delete the file \"Favicon\" because Chrome is open, close Chrome and try again!")
        with open(logpath, "a") as f:
            f.write(f"Log: PERMISSION ERROR; Chrome was open, \'{fpath}\" file could not be deleted\n")
else:
    print(f"\"{fpath}\" file does not exist")
    with open(logpath, "a") as f:
        f.write(f"Log: \"{fpath}\" FILE DOES NOT EXIST\n")

fjpath = os.path.join(os.environ['HOMEPATH'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Favicons-journal')

try:
    os.remove(fjpath)
    print("\"Favicons-journal\" file has been deleted")
    with open(logpath, "a") as f:
        f.write(f"Log: \"{fjpath}\" file has been deleted\n")
except PermissionError:
    print("Unable to delete the file \"Favicon-journal\" because Chrome is open, close Chrome and try again!")
    with open(logpath, "a") as f:
        f.write(f"Log: PERMISSION ERROR; Chrome was open, \'{fjpath}\" file could not be deleted\n")
except FileNotFoundError:
    print(f"\"{fjpath}\" file does not exist")
    with open(logpath, "a") as f:
        f.write(f"Log: \"{fjpath}\" FILE DOES NOT EXIST\n")

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"A log of this run can be found at {dir_path}/{logpath}")
x = 0
for f in os.listdir(dir_path + "/log"):
    x+=1
if x > 25:
    for f in os.listdir(dir_path + "/log"):
        if f.title() == today:
            continue
        else:
            os.remove(f)
with open(logpath, "a") as f:
    f.write(f"Log: Old log files deleted\n")

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