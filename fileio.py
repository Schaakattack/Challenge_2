# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_data):
    """Saves the qualifying data to a CSV file.

    Args:
        qualifying_data (list of lists): The qualifying bank data.
    """
   
   # creating the csvwriter
   
    with open ("qualifed_data.csv", "w") as csvfile :
        #line creates the header row and creates csvwriter for rest of file.
        csvwriter = csv.writer (csvfile)
        csvwriter. writerow (["Lender" , "Max Loan Amount" , "Max LTV", "Max DTI" , "Min Credit Score" , "Interest Rate"])
        for qualified_loan in qualifying_data :
            csvwriter. writerow (qualified_loan)
