# Author: Erin Schick
# Date of Last Edit: November 26th, 2018

import csv 
import requests 
import xml.etree.ElementTree as ET 
import itertools
          
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for dict items 
    items = [] 
  
    # iterate dict items 
    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text 
  
        # append dict dictionary to dict items list 
        items.append(dict) 

    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection/metars'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text 
  
        # append dict dictionary to dict items list 
        items.append(dict) 

    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection/metars/currentMetar'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text
  
        # append dict dictionary to dict items list 
        items.append(dict) 

    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection/metars/currentMetar/Text'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text 
  
        # append dict dictionary to dict items list 
        items.append(dict) 

    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection/metars/historicalMetar'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text
  
        # append dict dictionary to dict items list 
        items.append(dict) 

    for item in root.findall('./NGBWeatherBriefing/METAR/metarSection/metars/historicalMetar/Text'): 
  
        # empty dict dictionary 
        dict = {} 
  
        # iterate child elements of item 
        for child in item: 

            # There are no namespaces left, just need this line
            if child.text is not None:
                dict[child.tag] = child.text 
  
        # append dict dictionary to dict items list 
        items.append(dict) 


    #Makes it into just one dictionary not a list of multiple dictionaries
    flatten = {}

    for d in items:
        flatten.update(d)


    #Add the flattened dictionary to a list to make sure that converting to CSV works correctly
    final_result = []

    final_result.append(flatten)


    # return final_result
    return final_result 
  
  
def savetoCSV(items, filename): 
  
    # specifying the fields for csv file 
    fields = ['sectionType', 'sectionHeading', 'summaryText', 'airportId',
              'condition', 'timestamp', 'EncodedText', 'PlainText', 'issuanceDateTime'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows -- This is getting errors
        writer.writerows(items) 
  
      
def main(): 
  
    # parse xml file 
    items = parseXML('b_copy.xml') 
  
    # store dict items in a csv file 
    savetoCSV(items, 'metar_result.csv') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 


















