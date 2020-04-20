# shebang line for python3
#!/usr/bin/python3

# An interactive python-based datasets retriever for the GEO database

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

#Download files from the GEO database using any GEO accession numbers (GSE, GSM, GPL, or GDS)
# A GEO Series record is an original submitter-supplied record that summarizes an experiment.
## A GSE (or a Series) is an original submitter-supplied record
#that summarizes whole study including samples and platforms
# https://www.ncbi.nlm.nih.gov/geo/info/overview.html

#gse_number = {}

class geo_record(object):
        """
        Return a geo_record object whose: series [GEO accession number (GSExxx)] is *series*,
        sample [GEO accession number (GSMxxx)] is *sample*, platform [GEO accession number (GPLxxx)] is *platform*,
        and dataset [GEO Dataset records (GDSxxx) is *dataset*].
        
        :param series: str -- GEO accession number (GSExxx)
        :type series:
        :param sample: str -- GEO accession number (GSMxxx)
        :type sample:
        :param platform: str -- GEO accession number (GPLxxx)
        :type platform:
        :param dataset: str -- GEO Dataset records (GDSxxx)
        :type dataset:
        """
        
     def __init__(self, series, sample, platform, dataset):
        """ 
        The constructor for geo_record class
        :param series: 
        :type series:
        :param sample:
        :type sample:
        :param platform:
        :type platform:
        :param dataset: 
        :type dataset:
        """
        
        self.series = series
        self.sample = sample
        self.platform = platform
        self.dataset = dataset

"""
Commenting this out for now.
need to look at the type of data that is stored in the GEO database a little bit more

class geo_datatype(object):
    def __init__(self, microarray, ngs, functional_genomics):
    
"""

# Makes a function that will contain the desired program.
def get_GEO_files(self, series, sample, platform, dataset):
    """
    Get filename using GEO accession number (either 'series', 'sample', 'platform', or 'dataset')
    """
    # Create a loop until the user enter a valid GEO accession number
    # Calls for an infinite loop that keeps executing until an exception occurs
    while True:
         print()
         print("What is the GEO accession number for the dataset you would like to download?")
         print("You can use either Series (e.g.: GSE1563), Sample (e.g.: GSM906), Platform (e.g.: GPL2020), or Dataset (e.g.: GDS1563)")
         print("If you would like to download multiple files at once, simply separate each GEO accession number with a comma (e.g.: GSE1563, GSM906, etc)")
         try:
             geo_access_num = [str(geo_access_num) for geo_access_num in input("Enter the GEO accession number here: ").split(",")]
             break
             # geo={}.geo_access_num, destdir=output_dir
        # (1) print all the GEO accession numbers provided by the user (and remove the square brackets from the output of the list)
        print("You entered the following GEO accession numbers: " + str(geo_access_num)[1:-1])
        # (2) print the total number of inputs provided by the user
        print("A total of %d GEO accession number was provided" % len(geo_access_num))
                
        """     
        #another option is to
        # (1) ask the user for inputs -> (2) create an empty list to store these values ->
        # (3) loop through all the inputs entered by the user -> (4) add these inputs to that 'empty' list
        # see below for details...
        Note: if usiong this option, make sure to check indentation in the print statement
        
        geo_access_num = input("Enter the GEO accession number here: ").split(",")
        temp_list = []
        for i in geo_access_num:
            temp_list.append(i)
        print("You entered the following GEO accession numbers: " + str(temp_list)[1:-1])
        print("The total number of GEO accession numbers provided is: ", len(temp_list))
        """
        
        ## check that the GEO accession number(s) entered by the uder is(are) valid...(3 options - see below)
        # (1) if all the the inputs are invalid, throw an error and ask the user to enter at least 1 valid input to continue
        # (2) if one or more of the GEO accession number is invalid, throw a warning, reject those entries and proceed to download only the valid GEO accession numbers
        ## do this by: [first] remove the invalid inputs from the original list, [second] store the invalid inputs into a separate list,
        ## [third] download only the valid input from the original list
        for geo in geo_access_num
                if geo in Geo_type #need to add a valid statement here (this is just for place holder right now
                   print("only some of these GEO accession numbers are valid")
                   print("The following GEO accession numbers are invalid: %s, \n and will be ignored" % )
                   print("therefore only the followng GEO accession numbers will be downloaded")
        # (3) if all inputs are valid, proceed to download all
                else:
            
         # If something else that is not a GEO accession number is introduced, the ValueError exception will be called
         except ValueError:
             # The cycle will go on until validation
             print("Error! This GEO accession number is invalid. \n Please enter a valid GEO accession number to continue" )
             
         # When a valid GEO accession number is entered successfully, the loop will end.
        
        # prepare files for processing
            for i in geo_access_num:
                if i series = "GSE"
                elif series = none 
                elif
                ese
                dataset = GEOparse.get_GEO(geo=geo_access_num, destdir=output_dir)
             # ask user to create a folder name
             # This 'folde name' input will be used to create a new folder to store files in (if folder does not already exist)
             print("Where would you like to save these files? ")

             try: 
                 # An input is requested and stored in a variable
                 folder_name = input("Enter a project or folder name: ")
                 
             except SyntaxError:
                 folder_name = None
                 
                 # (1) Test for empty strings
                 if folder_name is None:
                     print("You must choose or create a project folder in order to continue")
                     folder_name = input("Enter a project name: ")
                 
                 else :
                     # Converts the user input into a string
                     folder_name_str = str(folder_name)
                     print("The project name you entered is": %s) % folder_name_str
                     
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
         print("Downloading %s dataset into %s folder", % (dataset, output_dir))
         return dataset
         
                     print("Please wait...")
                     for i in tqdm(output_dir)
                     print "Download is Complete!)
                     print("Go to the %s folder to view the downloaded dataset", % file_name)
                     break
 if __name__== "__main__":
    main()
