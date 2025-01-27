#!/usr/bin/env python
# coding: utf-8

# In[54]:


# For this homework assignment, we will use the code from "Processing Multiple Files and Writing Files" 
# where we processed the file "03_Prod.mdout". We will create another Jupyter "analyze_mdout.ipynb". 
# Refer to this file for further details about the assignment.
# We will modify this using argparse to run in terminal.

## My Code ##
# Let us do an assignment now to find the total energy from any user defined mdout file.

import os
import numpy
import argparse

def open_mdout(mdout_file_path):    # "mdout_file_path" is just a placeholder to take the needed xyz file path

    
    # Create a .txt file to store Etot data (to have a variable file name, we use basename function):
    filename = os.path.basename(mdout_file_path)
    split_filename = filename.split('.')
    mdout_filename = split_filename[0]
    with open (F'{mdout_filename}_Etot_file' , 'w+') as Etot_txt_file:  # This line create a txt file
    
    # open the mdout file to get Etot data:
        with open (mdout_file_path , 'r') as outfile:    # "mdout_file_path" is user defined file path in terminal 
            data = outfile.readlines()
            for line in data:
                if "Etot" in line:
                    Etot_line = line
                    #print(Etot_line)
                    split_Etot_line = Etot_line.split()
                    Etot_value = float(split_Etot_line[2])
                    print(Etot_value)
                    Etot_txt_file.write(F'The total energy value is {Etot_value} \n')
                        

if __name__ == "__main__":
    # Initialize argparse
    parser = argparse.ArgumentParser(description = "The script analyzes a user given mdout file and outputs Etot.")
    # Generate argument for mdout file
    parser.add_argument("mdout_file" , help="The file path to get any mdout file")
    args = parser.parse_args()
    mdout_file = args.mdout_file  
    open_mdout(mdout_file)
        
# To call a function, I need input

## To use this code on terminal ##
# Convert ipynb file to py using: jupyter nbconvert --to script analyze_mdout.ipynb
# Use this command to enter the directory: cd /Users/areejnad/Documents/Areej\ Academic\ Data/My\ Research/CCR\ and\ Simulation\ Learning/Learning\ Python/Learning\ Data/
# Use this command to execute: python analyze_mdout.py "CMS Workshp (MolSSI data)/03_Prod.mdout"
# Use this command to execute: python analyze_mdout.py "CMS Workshp (MolSSI data)/polyAT_wat_md2.mdout"


# In[56]:


## Original Code (Previously written by me) ##
# Let us do an assignment now to find the total energy from 03_Prod.mdout file.

# # Create a .txt file:
# with open ('Etot.txt' , 'w+') as Etot_txt_file:

# # Define the file path:
#     os_file_path = os.path.join('CMS Workshp (MolSSI data)' , '03_Prod.mdout')
#     print(os_file_path)

# # Remember that in the previous example, we used 2 for loops as we were processing 
# # multiple files in a directory. Here, we don't need that as there is only one file to process
#     with open (os_file_path , 'r') as outfile:
#         data = outfile.readlines()
#         for line in data:
#             if "Etot" in line:
#                 Etot_line = line
#                 #print(Etot_line)
#                 split_Etot_line = Etot_line.split()
#                 Etot_value = split_Etot_line[2]
#                 print(Etot_value)
#                 Etot_txt_file.write(F'The total energy value is {Etot_value} \n')
# Etot_txt_file.close()


# In[58]:


## ChatGPT suggested code

# import os
# import argparse

# def open_mdout(mdout_file_path):  
#     """
#     Reads an mdout file, extracts total energy (Etot) values, and writes them to a .txt file.
#     """
#     # Dynamically create the output file name based on the input file name
#     filename = os.path.basename(mdout_file_path)
#     mdout_filename = filename.split('.')[0]
#     output_file_path = f"{mdout_filename}_Etot_file.txt"

#     # Initialize a flag to check if any Etot values are found
#     etot_found = False

#     # Open the mdout file and the output file
#     with open(mdout_file_path, 'r') as infile, open(output_file_path, 'w') as Etot_txt_file:
#         for line in infile:
#             if "Etot" in line:  # Look for lines containing "Etot"
#                 split_line = line.split()
#                 try:
#                     # Extract and write the Etot value
#                     Etot_value = float(split_line[2])
#                     print(f"Found Etot: {Etot_value}")  # Print the value to the console
#                     Etot_txt_file.write(f"{Etot_value}\n")
#                     etot_found = True
#                 except (IndexError, ValueError):
#                     print(f"Warning: Could not parse Etot value from line: {line.strip()}")

#         # Handle the case where no Etot values were found
#         if not etot_found:
#             print(f"No Etot values found in {mdout_file_path}")
#             Etot_txt_file.write("No Etot values found.\n")

#     print(f"Etot values written to {output_file_path}")


# if __name__ == "__main__":
#     # Initialize argparse
#     parser = argparse.ArgumentParser(description="The script analyzes a user-given mdout file and outputs Etot values.")
#     # Add argument for the mdout file
#     parser.add_argument("mdout_file", help="The file path to the mdout file to analyze.")
#     args = parser.parse_args()

#     # Call the function to process the mdout file
#     open_mdout(args.mdout_file)


# In[ ]:





# In[ ]:




