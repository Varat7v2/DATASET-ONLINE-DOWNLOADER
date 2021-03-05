#!/bin/bash

'''
Using major-keywords alongwith prefixes and postfixes, generating disparate keywords for search engines
OUTPUT: Separate CSV files for each classes
'''
python classifier-keywords-generator.py

'''
Scrape images online
'''

python online-images-download.py


# '''
# Allocate downloaded images into training, validation, and testing sets
# '''
# python csv2class-allocator.py