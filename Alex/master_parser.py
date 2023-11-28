import os
import datetime
from openpyxl import Workbook

# Function to evaluate each question for a document
def evaluate_document(document_text):
    # Modify the logic as needed for each question
    results = [
        "SOLID" in document_text and 
        "RESTUL" in document_text and 
        ("OOP" in document_text or "object oriented" in document_text),

        "Azure" in document_text or 
        "AWS" in document_text or 
        "OOP" in document_text or 
        "object oriented" in document_text or 
        "dependency injection" in document_text,

        "Debug" in document_text or 
        "troubleshoot" in document_text or 
        "diagnose" in document_text or 
        "improve" in document_text,

        ".net" in document_text and 
        "c#" in document_text and 
        "SQL" in document_text and 
        "Azure" in document_text,

        "Leadership" in document_text or 
        "mentorship" in document_text,

        "visual studio" in document_text or 
        "visual basic" in document_text or 
        "GIT" in document_text,

        "Agile" in document_text or 
        "scrum" in document_text or 
        "CI/CD" in document_text,

        "Design" in document_text or 
        "Concept" in document_text,  # Assuming case-insensitive matching for "Design" and "Concept"

        "Github" in document_text or 
        "Gitlab" in document_text or 
        "bitbucket" in document_text or 
        "Jira" in document_text or 
        "Asana" in document_text or 
        "Trello" in document_text,

        any(keyword in document_text.lower() for keyword in ["manage", "management", "manager"]) and "project" in document_text
    ]
    
    return results

#RESUME_FOLDER = "C:\Users\jalex\Desktop\Immigration Campaign\Resumes"
#RESUME_FOLDER = "/c/Users/jalex/Desktop/Immigration Campaign/Resumes"
#RESUME_FOLDER = "./Resume_Samples"
RESUME_FOLDER = "C:\Resume_Samples"

# Function to process each document and update the spreadsheet
def process_documents(documents_folder, output_file):

    wb = Workbook()
    ws = wb.active
    # Rows can also be appended
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

    #file1 = open(output_file, "w")
    #file1.writelines("Results\n")
    #file1.writelines([ "filename", 
    #                   "solid, restful, oop", 
    #                   "azure, aws, oop", 
    #                   "debug, troubleshoot, improve, diagnose", 
    #                   ".net, c#, sql, azure", 
    #                   "leadership, mentorship", 
    #                   "visual studio, visual basic, git",
    #                   "agile, scrum, cicd", 
    #                   "design, concept", 
    #                   "github, gitlab, bitbucket, jira, asana, trello"])
    #file1.writelines("\n")
    #file1.close()
    
    # Iterate through each document in the folder
    for filename in os.listdir(documents_folder):
        if filename.endswith(".txt"):  # Assuming the documents are text files
            with open(os.path.join(documents_folder, filename), "r") as file:
                document_text = file.read()
            
            # Evaluate each question for the document
            results = [filename] + evaluate_document(document_text)
            print(results)
            #file1 = open(output_file, "a")
            #file1.writelines(str(results))
            #file1.writelines("\n")
            #file1.close()

            ws.append(results)
            # Save the file
            wb.save(excel_output_file)

# Specify the folder containing the documents and the output file
documents_folder = RESUME_FOLDER
#output_file = "output.csv"
excel_output_file = "excel_output_file.xlsx"

# Process the documents and update the spreadsheet
process_documents(documents_folder, excel_output_file)

print(f"Results saved to {excel_output_file}")