# csv_to_json

This code read all the csv files inside a directory and write them into a json file "inputspec.json". Each csv file is considered as data from separate site. 
# Arguments
 &nbsp;&nbsp; directory : directory that contains all the csv files \
 &nbsp;&nbsp; lambda: value for lambda \
 &nbsp;&nbsp; type_of_data: type of the data we have for example FreeSurfer or NIfTI. \
 &nbsp;&nbsp; data_vars: values need to be extracted from data (dependent variables). 
# How to run
 &nbsp;&nbsp; python csv_to_json.py -p directory -l lambda -t type_of_data -v data_vars \
 &nbsp;&nbsp; Exmple: python csv_to_json.py -p ~\csvs_directory\ -l 0 -t int string -v attribute0 attribute1 
