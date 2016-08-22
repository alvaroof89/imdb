# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:14:32 2016
@author: alvaroof89
Script for loading, parsing, and then exporting into csv the plot.list file rom imdb database
OUTPUT: key:title value:plot
"""
import re
import csv

#import the plot.list file from the imdb database and parse it using regexp module
file = open("C:/Users/alvaroo89/Data Science/Proyectos/IMDB/plot.list", 'r', encoding="ISO-8859-1")
text = file.read()
p = re.findall(r'MV: (.*)\s+((?:PL: (.*)\s)+)+', text, re.MULTILINE)
dict = {}
for i in range(0,len(p)):
    dict[str(p[i][0])] = re.sub("(\nPL:|\n|PL: )","",str(p[i][1]))

#Now 'dict' has key:title and value:plot. Ready for analyse
#Export to csv so it can be easily loaded into R afterwards

with open('C:/Users/alvaroo89/Data Science/Proyectos/IMDB/dict.csv', 'w', encoding="ISO-8859-1") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
        writer.writerow([key, value])
       
#the text mining procedures will be performed in R scripts kept in this same project folder
