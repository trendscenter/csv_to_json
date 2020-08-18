# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:48:48 2020

@author: Fatemeh
"""

import glob, os
import pandas as pd
import json
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type = dir_path, required=True, help = "path that contains all the csv files")
    parser.add_argument("-l", "--lmda", type = int, required=True, help = "lambda value")
    parser.add_argument("-t", "--types", type = str, nargs='+', required=True,
                        help="types of the data we have for example FreeSurfer, int or string")
    parser.add_argument("-v", "--vars", type = str, nargs='+', required=True,
                        help="dependent variables that need to be extracted from data")
    args = parser.parse_args()
    return args.path, args.lmda, args.types, args.vars


def csv_to_json_(base_dir, lambda_, type_of_data, data_vars):
    """read the csv files and convert their data into a string of json format,
    first column in the csv files is considered as index column and the rest of
    columns are considered as covariates"""
    json_content = "["
    file_path = base_dir + '*.csv'
    files = glob.glob(file_path)
    for file in files:
        with open(file) as csvFile:
            data = pd.read_csv(csvFile)
            data = data.set_index(data.columns[0])
            data_ = data.to_json(orient="index")
            data_parsed = json.loads(data_)
            json_dict = {
                    "covariates":{ 
                            "value": data_parsed
                            },
                    "data":{
                            "fulfilled": True,
                            "value": {
                                    "type": type_of_data,
                                    "value": data_vars
                                    }
                            },
                    "lambda":{
                             "fulfilled": True,
                             "value": int(lambda_)
                             }
                    }
            json_content += json.dumps(json_dict, indent=4) + ","
    json_content = json_content[:-1]
    json_content += "\n]"
    return json_content


def write_to_json(json_filename, json_content):
    """writes json_content which is a string into a json file"""
    with open(json_filename, 'w') as jsonFile:
        jsonFile.write(json_content)


if __name__ == '__main__':
    base_dir, lambda_, type_of_data, data_vars = get_input()
    json_content = csv_to_json_(base_dir, lambda_, type_of_data, data_vars)
    json_filename = base_dir + "inputspec.json"
    write_to_json(json_filename, json_content)
