# csv_to_json

This code read all the csv files inside a directory and write them into a json file "inputspec.json". Each csv file is considered as data from separate site. \
type_of_data and data_vars in the arguments should be seperated by a comma (put space before and after comma).
# Arguments
 &nbsp;&nbsp; directory : directory that contains all the csv files \
 &nbsp;&nbsp; lambda: value for lambda \
 &nbsp;&nbsp; type_of_data: type of the data we have for example FreeSurfer or NIfTI. If more than one type of data seperate them by a space \
 &nbsp;&nbsp; data_vars: values need to be extracted from data (dependent variables). Seperated by a space in command line. 
# How to run
 &nbsp;&nbsp; python csv_to_json.py directory lambda type_of_data , data_vars \
 &nbsp;&nbsp; Exmple: python csv_to_json.py ~\csvs_directory\ 0 int string , attribute0 attribute1 
