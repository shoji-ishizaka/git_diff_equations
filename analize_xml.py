'''
Created on 2021/10/25

@author: shoji
'''

import xml.etree.ElementTree as ET

time_start = 0.0
time_end = 0.0                       # Days
number_of_cuculation = 0          # Number of calculations

formula_list = []
init_values_list = []

def make_expression():
    '''making the string of arguments, and the string of formula'''
    global time_start, time_end, number_of_cuculation, formula_list, init_values_list
    
    tree = ET.parse('equation.xml')
    root = tree.getroot()

    '''making the string of time structures'''
    for element in [ child for child in root if child.tag == 'time']:
        if element.attrib["name"] == "START": 
            time_start = float( element.find("value").text)
        if element.attrib["name"] == "END": 
            time_end = float( element.find("value").text)
        if element.attrib["name"] == "NUMBER_OF_CALCULATION": 
            number_of_cuculation = int( element.find("value").text)

    '''making the strings of arguments'''
    add_exp = ""
    for element in [ child for child in root if child.tag == 'coefficient']:
        add_exp = add_exp + "," + element.attrib["name"] + "=" + element.find("value").text
    
    '''making the strings of formula and setting the initial values'''
    for element in [ child for child in root if child.tag == 'formula']:
        init_values_list.append( float( element.find("init_value").text))
        formula_list.append( "lambda x" + add_exp + ": " + element.find("exp").text)
        