import os
import sys
from openpyxl import Workbook
from PyPDF2 import PdfReader
import docxpy

##################### FUNCTIONS ##############################

# Function to evaluate each question for a document
def evaluate_document(document_text):
    document_text = document_text.lower()
    results = [
        ("advanced statistics" in document_text or "machine learning" in document_text) and 
    ("regression" in document_text or "classification" in document_text or 
    "time series analysis" in document_text or "network analysis" in document_text or 
    "clustering" in document_text or "simulation" in document_text or 
    "dimension reduction" in document_text),

("python" in document_text or "SQL" in document_text or "R" in document_text),

("distributed system" in document_text or "distributed computing" in document_text or 
"kafka" in document_text or "mongodb" in document_text or "splunk" in document_text or 
"microservice" in document_text or "docker" in document_text or "oracle 10g" in document_text),

("data" in document_text and 
    ("manipulate" in document_text or "analyze" in document_text) and 
    ("large scale" in document_text or "large data" in document_text or 
    "big data" in document_text or "complex data" in document_text or 
    "communicate complex" in document_text or "communicate complicated" in document_text or 
    "translate technical" in document_text)),

("ML Studio" in document_text or "Power Virtual Agent" in document_text or 
"power automate" in document_text or "power apps" in document_text or 
"S3" in document_text or "sagemaker" in document_text or "redshift" in document_text or 
"lambda" in document_text or "EC2" in document_text or "azure cloud" in document_text or 
"google cloud" in document_text or "ibm cloud" in document_text or 
"oracle cloud" in document_text or "vmware cloud" in document_text or 
"huawei cloud" in document_text or "alibaba cloud" in document_text or 
"digitalocean" in document_text),

("technical writing" in document_text or "user guides" in document_text or 
"user instructions" in document_text or "technical writer" in document_text or 
"datasheets" in document_text or "whitepapers" in document_text)
    ]
    
    return results

# Function to process each document and update the spreadsheet
def process_documents(documents_folder, output_file):

    wb = Workbook()
    ws = wb.active
    ws.append(["filename", 
               "advenced stats", 
               "python sql", 
               "distributed systems", 
               "large data sets", 
               "Cloud", 
               "technical writing",
               ])
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

documents_folder = "H:\Campaign Shashank\Resumes\Resumes"
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