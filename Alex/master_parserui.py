import os
import sys
from openpyxl import Workbook
from PyPDF2 import PdfReader
import docxpy
from tkinter import * #Tkinter GUI

##################### FUNCTIONS ##############################

# Function to evaluate each question for a document
def evaluate_document(document_text, conditions_array):
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
def process_documents(documents_folder, output_file, conditions_array):

    # create an excel object
    wb = Workbook()
    ws = wb.active
    
    # create headers array
    headers = []
    headers.append("filename")
    for condition in conditions_array:
        title = stringify_condition(condition)
        headers.append(title)       

    # Save the excel file
    ws.append(headers)
    wb.save(excel_output_file)

    if documents_folder == "": documents_folder = "./Resume_Samples"
    
    # Iterate through each document in the folder
    for filename in os.listdir(documents_folder):
        if filename.endswith(".docx"):
            document_text = docxpy.process(documents_folder+"/"+filename)
            results = [filename] + evaluate_document(document_text, conditions_array)
            print(results)
            ws.append(results)
            wb.save(excel_output_file) 
        if filename.endswith(".pdf"):   
            reader = PdfReader(documents_folder+"/"+filename) 
            num_pages = len(reader.pages)
            # to-do: update to check all pages
            page = reader.pages[0]
            document_text = page.extract_text() 
            results = [filename] + evaluate_document(document_text, conditions_array)
            print(results)
            ws.append(results)
            wb.save(excel_output_file) 
        if filename.endswith(".txt"): 
            print("text files not supported")           

def stringify_condition(condition):
    condition_string = ""
    for index, req in enumerate(condition):
        condition_string = condition_string + "["
        for i, word in enumerate(req):
           if i == 0: condition_string = condition_string + word
           else: condition_string = condition_string + " OR " + word
        condition_string = condition_string + "]"
        if index != len(condition)-1: condition_string = condition_string + " AND "
    return condition_string

##################### MAIN CODE ##############################

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


excel_output_file = "excel_output_file.xlsx"
root = Tk()
row_count = 0

howto_label = Label( root, text="enter path of resumes below then press button")
howto_label.grid(row=row_count, sticky=W)
row_count+=1

path_input = Text(root, height=1, width=49)
path_input.grid(row=row_count, sticky=W)
row_count+=1

for i, condition in enumerate(conditions_array):
    temp_var = IntVar()
    condition_string = stringify_condition(condition)

    check_var = Checkbutton(root, text=condition_string, variable=temp_var)
    check_var.grid(row=row_count, sticky=W)
    row_count+=1

# create the button that gets the input and runs function
output = Button(root, text="Run parser", 
                command=lambda: process_documents(str(path_input.get("1.0", 'end-1c')),
                                                     excel_output_file, 
                                                     conditions_array
                                                     ))
output.grid(row=row_count, sticky=W)
row_count+=1

root.mainloop()

print(f"Results saved to {excel_output_file}")



