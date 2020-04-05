#!/usr/bin/python3

# A python-based datasets retriever for GEO database

"""
author: Chris Etienne
email: cetienn01@gmail.com
github: https://github.com/cetienn01
package title: ExtractGEO
"""

#import libraries/packages that you will need
import GEOparse
import pandas as pd
import numpy as np
import sys
import os
from os import path
from tqdm import tqdm

#Download files from the GEO database using GSE accession numbers
#A GSE (or a Series) is an original submitter-supplied record
#that summarizes whole study including samples and platforms

#gse_number = {}

# Makes a function that will contain the desired program.
def get_filename_fromGEO():
    """
    Get filename using GEO accession number
    """
    # Create a loop until the user enter a valid GEO accession number
    # Calls for an infinite loop that keeps executing until an exception occurs
    while True:
         print()
         print("What is the GEO (series) accession number for the dataset you would like to download? \n (e.g.: GSE1563)")
         
         try:
             geo_access_num = input("Enter GSE number here: ")
             dataset = GEOparse.get_GEO(geo=geo_access_num, destdir=output_dir)
             # geo={}.geo_access_num, destdir=output_dir
             
         # If something else that is not a GSE number is introduced, the ValueError exception will be called
         except ValueError:
             # The cycle will go on until validation
             print("Error! This GEO number is invalid. \n Please enter a valid GEO (series) accession number to continue" )
             
         # When a valid GSE number is entered successfully, the loop will end.
         else:
             # ask user to create a folder name
             # This input will be used to create a new folder to store files in (if folder does not already exist)
             print("Where would you like to save these files? ")

             try: 
                 # An input is requested and stored in a variable
                 folder_name = input("Enter a project name: ")
                 
             except SyntaxError:
                 folder_name = None
                 
                 # (1) Test for empty strings
                 if folder_name is None:
                     print("You must choose or create a project folder in order to continue")
                     folder_name = input("Enter a project name: ")
                 
                 else :
                     # Converts the user input into a string
                     folder_name_str = str(folder_name)
                     print("The project name you entered is: %s ") % folder_name_str
                     
             # (2) Check to see if [output directory] folder is an existing directory
             else:
                 # confirm that a given path points to a directory                 
                 if os.path.isdir(folder_name_str):
                     print("%s is a directory " % folder_name_str)
                     # and use it to store the dataset/files..
                     output_dir = open(folder_name_str, "r+")
                 else:
                     # let the user know this folder/directory does not exist
                     print("The folder %s could not be found " % folder_name_str)

                     # then...automatically create output directory folder using the user input (folder name)
                     print("A new folder named '%s' will be created to store the files " % folder_name_str)
                     #if not os.path.isdir(folder_name_str):
                     os.makedirs(folder_name_str_dir)
                     output_dir = os.path.dirname(folder_name_str_dir)

         # Download files/dataset
         print("Downloading %s dataset into %s folder", % dataset, % output_dir)
         return dataset
         
                     print("Please wait...")
                     for i in tqdm(output_dir)
                     print "Download is Complete!)
                     print("Go to the %s folder to view the downloaded dataset", % file_name)
                     break
                    if __name__== "__main__":
                        main()