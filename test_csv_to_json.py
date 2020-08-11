# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:48:54 2020

@author: Fatemeh
"""

import pytest
import json
import os
from csv_to_json import csv_to_json_, write_to_json


def test_csv_to_json():
    """this function compares the expected json string to what csv_to_json return, spaces and \n's are removed when comparing"""
    json_dict = {
            "covariates":{ 
                    "value":{
                        "subject0": {
                            "attribute0": 3.0,
                            "attribute1": 12.0
                        },
                        "subject1": {
                            "attribute0": 1.2,
                            "attribute1": 10.9
                        }
                    }
                    },
            "data":{
                    "fulfilled": True,
                    "value": {
                            "type": ["float"],
                            "value": [
                                "attribute0",
                                "attribute1"
                            ]
                            }
                    },
            "lambda":{
                    "fulfilled": True,
                    "value": 0
                    }
            }
    json_string = "[" + json.dumps(json_dict).replace(' ', '').replace('\n', '') + "]"
    directory = os.path.join(os.getcwd(), "test/")
    lambda_ = "0"
    data_type = ["float"]
    data_vars = ["attribute0", "attribute1"]
    assert csv_to_json_(directory, lambda_, data_type, data_vars).replace(' ', '').replace('\n', '') == json_string
    
    
def test_write_to_json():
    """this saves a sample json string into a file and tests write_to_json function"""
    tmp_dir = os.getcwd()
    json_content = '{ "name":"John", "age":30}'
    directory = os.path.join(tmp_dir, 'inputspec.json')
    write_to_json(directory, json_content) 
    with open(directory) as json_file:
        data = json.load(json_file)
    json_string = json.dumps(data)
    assert json_string.replace(' ', '') == json_content.replace(' ' , '')