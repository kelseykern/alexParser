import pandas as pd
import os

# Function to evaluate each question for a document
def evaluate_document(document_text):
    # Modify the logic as needed for each question
    results = [
        "SOLID" in document_text and "RESTUL" in document_text and ("OOP" in document_text or "object oriented" in document_text),
        "Azure" in document_text or "AWS" in document_text or "OOP" in document_text or "object oriented" in document_text or "dependency injection" in document_text,
        "Debug" in document_text or "troubleshoot" in document_text or "diagnose" in document_text or "improve" in document_text,
        ".net" in document_text and "c#" in document_text and "SQL" in document_text and "Azure" in document_text,
        "Leadership" in document_text or "mentorship" in document_text,
        "visual studio" in document_text or "visual basic" in document_text or "GIT" in document_text,
        "Agile" in document_text or "scrum" in document_text or "CI/CD" in document_text,
        "Design" in document_text or "Concept" in document_text,  # Assuming case-insensitive matching for "Design" and "Concept"
        "Github" in document_text or "Gitlab" in document_text or "bitbucket" in document_text or "Jira" in document_text or "Asana" in document_text or "Trello" in document_text,
        any(keyword in document_text.lower() for keyword in ["manage", "management", "manager"]) and "project" in document_text
    ]
    
    return results

# Function to process each document and update the spreadsheet
def process_documents(documents_folder, output_file):
    # Create an empty DataFrame
    df = pd.DataFrame(columns=["Document"] + [f"Question {i+1}" for i in range(10)])
    
    # Iterate through each document in the folder
    for filename in os.listdir(documents_folder):
        if filename.endswith(".txt"):  # Assuming the documents are text files
            with open(os.path.join(documents_folder, filename), "r") as file:
                document_text = file.read()
            
            # Evaluate each question for the document
            results = [filename] + evaluate_document(document_text)
            
            # Append results to the DataFrame
            df = df.append(pd.Series(results, index=df.columns), ignore_index=True)
    
    # Save the DataFrame to the output file (CSV format)
    df.to_csv(output_file, index=False)

# Specify the folder containing the documents and the output file
documents_folder = "/path/to/documents"
output_file = "output.csv"

# Process the documents and update the spreadsheet
process_documents(documents_folder, output_file)

print(f"Results saved to {output_file}")
