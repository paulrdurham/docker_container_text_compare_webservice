
####### \\\\\\||||||||
## Author : Paul Durham (PaulR.Durham@gmail.com)
## Date : 02-02-2021
## Description : A simple FLASK APP that compares 
##  two strings. Basic comparison. The delta of the 
## word occurances is * .01 and subrated from 1.00
## to get similarity.
##
##  You can use curl commands such as ...
##  curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\" TEXT! \",\"two\":\" TEXT! \"}"
## A percentage will be returned.
####### ///////|||||||

import json
import string
import flask
from flask import request
import sys
app = flask.Flask(__name__)
app.config["DEBUG"] = True
    
@app.route('/compare', methods=['POST'])
def compare():

    ## Getting the contents of --data from the curl command
    byte_content = request.data
    ## turning it into a proper string
    json_string = byte_content.decode('utf8')
    ## passing in the RAW string to the json.loader
    content = json.loads(json_string.encode('unicode_escape'))
    
    
    one = content['one']
    two = content['two']
    res = compare_these_files(one,two)
    return str(res)

## this just returns an array of words to ignore
## in a production enviroment this would not be
## hard coded
def ignoreWords():
    return ['the','it','a','an','i','you','we','us','me','her','he','him','them','that','they','this']

## these three files are str 
def compare_these_files(file_1,file_2):
    ## first lets remove punctuation
    file_1 = file_1.replace('.','').replace("'",'').replace(',','').replace('"','')
    file_2 = file_2.replace('.','').replace("'",'').replace(',','').replace('"','')

    ## lets lowercase everything
    file_1 = file_1.lower()
    file_2 = file_2.lower()
    
    
    ## third lets turn them into lists
    list_1 = file_1.split(' ')
    list_2 = file_2.split(' ')
    
    
    ## lets create dictionaries for each file
    dict_1 = {}
    dict_2 = {}
    
    
    ## We are going to store the words and the number of occurances
    ## BUT we are going to ignore some words
    words_to_ignore = ignoreWords()
    dict_1 = process(list_1,words_to_ignore)
    dict_2 = process(list_2,words_to_ignore)
    
        
    ## process comparison
    result_1_2 = compare(dict_1,dict_2)
    
    
    return [result_1_2]

## compares two dictionaries
def compare(dict_1,dict_2):
    ## getting things setup
    common = {}
    ## set means only one entry per word
    keys = set()
    ## getting all words from each dictionary
    for x in dict_1.keys():
        keys.add(x)
    for x in dict_2.keys():
        keys.add(x)
    ## gather number of entries with full key list
    for x in keys:
        ## blank item
        if x=='':
            print("skipping blank")
        else:
            one = 0
            if x in dict_1:
                one = dict_1[x]
            two = 0
            if x in dict_2.keys():
                two = dict_2[x]
            common[x] = [one,two]
    ## this is a dictionary with combined dictionaries
    percentage = 1
    print(common)
    ## this could technically be done in the prior loop
    for y in common.keys():
        x = common[y]
        
        ## this just compares two see which has more
        ## occurances
        first = x[0]
        second = x[1]
        
        ## Lets compare them
        size = 0
        if first > second:
            size = first-second
        else:
            size = second-first
        percentage -= size * .01
    return percentage
    
## Turns the lists into dictionaries that contain the number of occurances
def process(list, ignore_these_words):
    res = {}
    for x in list:
        if x in ignore_these_words:
            print('')
        elif x in res.keys():
            res[x] = 1 + res[x]
        else:
            res[x] = 1
    return res



app.run(host='0.0.0.0',port=5000)



