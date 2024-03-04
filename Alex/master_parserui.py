import os
import sys
from openpyxl import Workbook
from PyPDF2 import PdfReader
import docxpy
from tkinter import * #Tkinter GUI

conditions_array = [
    [
      ["solid"],
      ["restful"],
      ["oop","object oriented"]
    ],
    [
      ["azure", "aws", "oop", "object oriented", "dependency injection"]
    ],
    [
      ["debug", "troubleshoot", "diagnose", "improve"]
    ],
    [
      [".net"],
      ["c#"],
      ["sql"],
      ["azure"]
    ],
    [
      ["leadership", "mentorship"]         
    ],
    [
      ["visual studio", "visual basic", "git"]
    ],
    [
      ["agile", "scrum", "ci/cd"]
    ],
    [
      ["design", "concept"]        
    ],
    [
      ["github", "gitlab", "bitbucket", "jira",  "asana", "trello"]        
    ],
    [
       ["manage", "management", "manager"],
       ["project"]
    ]
]
##################### FUNCTIONS ##############################

# Function to evaluate each question for a document
def evaluate_document(document_text):
    document_text = document_text.lower()

    # conditions_array = array of conditions
    # condition = array of requirements (all requirements must be fulfilled for the condition to be fulfilled)
    # requirement = list of strings (must contain atleast 1 string from list)
    results = []
    for condition in conditions_array:
        # need to fulfill every requirement for condition to be marked true
        for req in condition:
            req_fulfilled = False
            # need to match atleast 1 word in req array
            for word in req:
                if word in document_text:
                    req_fulfilled = True
                    break
            if req_fulfilled == False:
                break

        results.append(req_fulfilled)

    return results


# Function to process each document and update the spreadsheet
def process_documents(documents_folder, output_file):

    wb = Workbook()
    ws = wb.active
    
    headers = []
    headers.append("filename")
    for condition in conditions_array:
        title = ""
        for index, req in enumerate(condition):
            title = title + "["
            for i, word in enumerate(req):
               if i == 0: title = title + word
               else: title = title + " OR " + word
            title = title + "]"
            if index != len(condition)-1: title = title + " AND "
        headers.append(title)       

    # Save the file
    ws.append(headers)
    wb.save(excel_output_file)
    
    # Iterate through each document in the folder
    for filename in os.listdir(documents_folder):
        if filename.endswith(".docx"):
            document_text = docxpy.process(documents_folder+"/"+filename)
            results = [filename] + evaluate_document(document_text)
            print(results)
            ws.append(results)
            wb.save(excel_output_file) 
        if filename.endswith(".pdf"):   
            reader = PdfReader(documents_folder+"/"+filename) 
            num_pages = len(reader.pages)
            # to-do: update to check all pages
            page = reader.pages[0]
            document_text = page.extract_text() 
            results = [filename] + evaluate_document(document_text)
            print(results)
            ws.append(results)
            wb.save(excel_output_file) 
        if filename.endswith(".txt"): 
            print("text files not supported")           

##################### MAIN CODE ##############################

#documents_folder = "C:/Users/jalex/Desktop/Immigration_Campaign/Resumes"
documents_folder = "./Resume_Samples"
excel_output_file = "excel_output_file.xlsx"
#
#user_path = ""
#path_exists = 0
#while path_exists == 0:
#    print("No valid path entered. ")
#    user_path = input("Please enter the full path of where the resumes are located (eg. C:/Resumes ): ")
#    path_exists = os.path.exists(user_path)
#
#print("Checking resumes in path: " + user_path)
#documents_folder = user_path
#    
process_documents(documents_folder, excel_output_file)
print(f"Results saved to {excel_output_file}")



