import os
import sys
from openpyxl import Workbook
from PyPDF2 import PdfReader
import docxpy
from tkinter import * #Tkinter

##################### FUNCTIONS ##############################

# Function to evaluate each question for a document
def evaluate_document(document_text):
    document_text = document_text.lower()
    results = [
        "solid" in document_text and 
        "restful" in document_text and 
        ("oop" in document_text or "object oriented" in document_text),

        "azure" in document_text or 
        "aws" in document_text or 
        "oop" in document_text or 
        "object oriented" in document_text or 
        "dependency injection" in document_text,

        "debug" in document_text or 
        "troubleshoot" in document_text or 
        "diagnose" in document_text or 
        "improve" in document_text,

        ".net" in document_text and 
        "c#" in document_text and 
        "sql" in document_text and 
        "azure" in document_text,

        "leadership" in document_text or 
        "mentorship" in document_text,

        "visual studio" in document_text or 
        "visual basic" in document_text or 
        "git" in document_text,

        "agile" in document_text or 
        "scrum" in document_text or 
        "ci/cd" in document_text,

        "design" in document_text or 
        "concept" in document_text,

        "github" in document_text or 
        "gitlab" in document_text or 
        "bitbucket" in document_text or 
        "jira" in document_text or 
        "asana" in document_text or 
        "trello" in document_text,

        any(keyword in document_text.lower() for keyword in ["manage", "management", "manager"]) and "project" in document_text
    ]
    
    return results

# Function to process each document and update the spreadsheet
def process_documents(documents_folder, output_file):

    wb = Workbook()
    ws = wb.active
    ws.append(["filename", 
               "solid, restful, oop", 
               "azure, aws, oop", 
               "debug, troubleshoot, improve, diagnose", 
               ".net, c#, sql, azure", 
               "leadership, mentorship", 
               "visual studio, visual basic, git",
               "agile, scrum, cicd", 
               "design, concept", 
               "github, gitlab, bitbucket, jira, asana, trello",
               "management, project"])
    # Save the file
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

documents_folder = "C:/Users/jalex/Desktop/Campaign/Resumes"
#documents_folder = "./Resume_Samples"
excel_output_file = "excel_output_file.xlsx"

user_path = ""
path_exists = 0
while path_exists == 0:
    print("No valid path entered. ")
    user_path = input("Please enter the full path of where the resumes are located (eg. C:/Resumes ): ")
    path_exists = os.path.exists(user_path)

print("Checking resumes in path: " + user_path)
documents_folder = user_path
    
process_documents(documents_folder, excel_output_file)
print(f"Results saved to {excel_output_file}")

