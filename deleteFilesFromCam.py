import os
import glob
import datetime 
from datetime import date
import subprocess
import time

''' 
Put this script in the autostart of your computer or use it in the task scheduler.
Autostart-directory-Windows: cmd + shell:startup
''' 

def iterateAndDeleteFiles(directory, diffDays, delimiter, now):
    files = glob.glob(directory)
    for f in files:
        filename = f.split(delimiter)
        
        year = int(filename[1][0:4])
        month = int(filename[1][4:6])
        day = int(filename[1][6:8])
        
        fileDate = date(year, month, day)

        if((now - fileDate).days > diffDays):
            print("deleted: " + str(day) + "-" + str(month) + "-" + str(year))            
            os.remove(f)

if __name__== "__main__":
    print("\nSCRIPT: Delete files after n days by filename!\n")
    
    # "net use" to mount a network drive in windows
    subprocess.call(r"net use X: \\192.168.178.5\testShare /user:shareUser password")
    
    print("working...please wait...")
    
    # settings for all calls
    now = datetime.date.today()
    # after n days the files will be deleted
    diffDays = 45
    
    delimiter = "_"

    # delete the cam files in the OutdoorCam directory
    directory = "X:\\OutdoorCam\\*"
    iterateAndDeleteFiles(directory, diffDays, delimiter, now)
    
    # delete the cam files in the IndoorCam directory
    directory = "X:\\IndoorCam\\*"
    iterateAndDeleteFiles(directory, diffDays, delimiter, now)

    # wait n seconds before unmount the network drive 
    time.sleep(15)

    subprocess.call(r"net use X: /y /delete")
