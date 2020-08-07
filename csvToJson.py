# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:48:48 2020

@author: Fatemeh
"""

import glob
import pandas as pd
import sys

def get_input():
    base_dir = sys.argv[1]
    lambda_ = sys.argv[2]
    type_of_data = sys.argv[3]
    data_values = []
    #save all the data values into a list 
    for arg in sys.argv[4:]:
        data_values.append(arg)
    return base_dir, lambda_, type_of_data, data_values

def read_csv_files(base_dir, lambda_, type_of_data, data_values):
    """read the csv files and convert their data into a string of json format,
    first column in the csv files is considered as index column and the rest of
    columns are considered as covariates"""
    json_content = "[\n"
    file_path = base_dir + '*.csv'   
    files=glob.glob(file_path)
    for file in files:
        with open(file) as csvFile:
            data = pd.read_csv(csvFile)
            data = data.set_index(data.columns[0])
            json_content += "{\n \"covariates\":{\n \"value\": {\n"
            columns = data.columns
            for i in list(data.index):
                json_content += "\t \t \""+str(i)+"\":{"
                for column in columns:
                    json_content += "\n \t \""+column+"\": \""+str(data.loc[i][column])+"\","
                json_content = json_content[:-1]
                json_content += "},\n"
            json_content = json_content[:-2]
            json_content += "}},\n"
            json_content += "\"data\":{\"fulfilled\":true,\n \t \"value\":[ {\n \t \"type\":\""+type_of_data+"\",\n\"value\":[ \n"
            for i in data_values:
                json_content += "\t \""+str(i)+"\",\n"
            json_content = json_content[:-2]
            json_content += "]\n } ]"
            json_content += "},\n\"lambda\":{    \"fulfilled\":true,\n \"value\":"+lambda_+"}\n},"
    json_content = json_content[:-1] 
    json_content += "\n ]"
    return json_content

def writ_to_json(jsonFilename, json_content):
    """writes json_content which is a string into a json file"""
    with open(jsonFilename, 'w') as jsonFile:
        jsonFile.write(json_content)

if __name__ == '__main__':
    base_dir, lambda_, type_of_data, data_values = get_input()
    json_content = read_csv_files(base_dir, lambda_, type_of_data, data_values)
    jsonFilename = base_dir+"inputspec.json"
    writ_to_json(jsonFilename, json_content)
