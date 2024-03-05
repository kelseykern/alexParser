import os
import sys
from openpyxl import Workbook
from PyPDF2 import PdfReader
import docxpy
from tkinter import * #Tkinter GUI
check_button_array = dict()
excel_output_file = "excel_output_file.xlsx"
root = Tk()
row_count = 0
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

############################## FUNCTIONS ##############################

# Function to evaluate each question for a document
def evaluate_document(document_text):
    global check_button_array
    global conditions_array

    document_text = document_text.lower()

    # conditions_array = array of conditions
    # condition = array of requirements (all requirements must be fulfilled for the condition to be fulfilled)
    # requirement = list of strings (must contain atleast 1 string from list)
    results = []
    for i, condition in enumerate(conditions_array):
        #check if this checkbox was ticked
        box = check_button_array.get(i)
        box_val = box.get()
        if box_val == 0: continue


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
    global conditions_array
    global check_button_array
    # create an excel object
    wb = Workbook()
    ws = wb.active
    
    # create headers array
    headers = []
    headers.append("filename")
    for i, condition in enumerate(conditions_array):
        #check if this checkbox was ticked
        box = check_button_array.get(i)
        box_val = box.get()
        if box_val == 0: continue


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
            results = [filename] + evaluate_document(document_text)
            ws.append(results)
            wb.save(excel_output_file) 
        if filename.endswith(".pdf"):   
            reader = PdfReader(documents_folder+"/"+filename) 
            num_pages = len(reader.pages)
            # to-do: update to check all pages
            page = reader.pages[0]
            document_text = page.extract_text() 
            results = [filename] + evaluate_document(document_text)
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

def create_grid_condition(i,condition):
    row_num = root.grid_size()[1]
    check_button_array[i] = IntVar()

    condition_string = stringify_condition(condition)

    check_button = Checkbutton(root, text=condition_string, variable=check_button_array[i]) #, command=lambda key=i: Readstatus(key))
    check_button.grid(row=row_num, sticky=W, padx=10, pady=10) 

def add_condition():
    global conditions_array
    new_condition = [["hello"],["Im","new"]]
    print("add condition",new_condition)

    conditions_array.append(new_condition)

    create_grid_condition((len(conditions_array)-1), conditions_array[len(conditions_array)-1])

############################## MAIN CODE ##############################

def main1():
    global row_count
    global conditions_array
    #global check_button_array
    howto_label = Label( root, text="enter path of resumes below then press button")
    howto_label.grid(row=row_count, sticky=W, padx=10, pady=10) 
    row_count+=1
    
    path_input = Text(root, height=1, width=49)
    path_input.grid(row=row_count, sticky=W, padx=10, pady=10) 
    row_count+=1
    
    
    for i, condition in enumerate(conditions_array):
        create_grid_condition(i, condition)
        row_count+=1
    
    new_condition_button = Button(root, text="add condition", command=lambda: add_condition())
    new_condition_button.grid(row=row_count, sticky=W, padx=10, pady=10) 
    row_count+=1
    
    # create the button that gets the input and runs function
    output = Button(root, text="Run parser", 
                    command=lambda: process_documents(str(path_input.get("1.0", 'end-1c')),
                                                         excel_output_file
                                                         ))
    output.grid(row=row_count, sticky=W, padx=10, pady=10) 
    row_count+=1
    
    root.mainloop()
    
    print(f"Results saved to {excel_output_file}")

if __name__ == '__main__':
    main1()



