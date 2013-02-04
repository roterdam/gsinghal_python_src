

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : July 28, 2010                                           #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


#!/usr/bin/python

import sys


"""
@param file: hg19.fa.out : This is repeat masker output
@return : Makes a file for each repeat element (such as AluY, L2, MIR) in hg18.fa.out. 
Each of such file contains all the lines from hg19.fa.out that belong to that repeat element.
"""

def Filter(file):
    dict = {} # new dictionary
    input = open (file, 'rU')
    input.readline()    # In case the first few lines of the file have column tags or are blank, then uncomment 
#                          these lines so that they get removed.
    input.readline()
    input.readline()
    for line in input:
        Repeat = organize(line)
        if Repeat in dict:   # if Repeat is already one of the keys in the dictionary
            value = dict[Repeat] + line   # the line is added to the value of that key
            dict[Repeat] = value
        else:
            dict[Repeat] = line  # new key value pair is created.
    input.close()
    print 'no of repeat elements is :', len(dict)
    for key in dict:
        out = open(key, 'w')  # for every key in dictionary, create a new file using the key as the filename
        out.write(dict[key])  # put the value of that key inside the file
        out.close()
        print key           # print all the keys, 1337 in total for hg18.fa.out
        
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):    
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    repeat = list[9].replace('/','_')  # in case the repeat element has '/' in it, it is replaced by '_'. This is done
    # because the repeat element name is used to make a file name, and file name cannot contain a '/'.
      
    return repeat
   

def main():
    openfile = sys.argv[1]   
    Filter(openfile)   
 
if __name__ == '__main__':
    main()