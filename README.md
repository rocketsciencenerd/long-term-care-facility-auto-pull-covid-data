this script is to pull covid case data about long term care facilities from the maryland department of health website 

this script is meant to run from the terminal applicaiton of a mac 

if you are unsure how to open terminal on a mac, open spotlight search (command + shift bar) and type in terminal 

copy this entire file (longTermCare) on to your desktop

step into the directory by running the following command: `cd Desktop/longTermCare`


to run:

open terminal:

if this is the first time you are running the script
run the following command `sh installer.sh`

to compile data:
run the following command `python3 update_cases.py`
* if you get the error `requests does not have a get command`, run the following:
        `python3 -m pip install requests`

the installer will install the following items needed to run this script on you machine:
- homebrew
- python3
- python3 plugin python3 -m pip install requests

outputs: 
    - ltcFacilityData[date] - this keeps with the format initially provided by olive (new facilities will not be added to this output)
    - ltcFacilitityData_raw[date] - this is the complete list of all facilities that come down from the server at any given time
    
    #todo: need to add auto update for changes in cases/deaths from previous day
