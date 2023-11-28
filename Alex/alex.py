#SOLID and RESTFUL and (OOP or “object oriented”)
sr = "no"

#Azure or AWS or OOP or “object oriented” or “dependency injection”
azs = "no"

#Debug or troubleshoot or diagnose or improve
debug_exp = "no"

#“.net” and “c#” and SQL and Azure
net_c = "no"

#Leadership or mentorship
leader= "no"

#“visual studio” or “visual basic” or GIT
vs = "no"

#Agile or scrum or “CI/CD” 
agile = "no"

#Design* or concept*
design = "no"

#Github or Gitlab or bitbucket or Jira or Asana or Trello
gith = "no"

#Manage* near project
manag = "no"

with open('test_file.txt','r') as file:
  
    # reading each line    
    for line in file:
  
        # reading each word        
        for word in line.split():
            
            # if SOLID and RESTFUL and (OOP or “object oriented”)
            #    sr = "yes"

            # if Azure or AWS or OOP or “object oriented” or “dependency injection”
            #   azs = "yes"

            # if Debug or troubleshoot or diagnose or improve
            #   debug_exp = "yes"

            # if “.net” and “c#” and SQL and Azure          
            if word in ('C++', 'c++',  '.net', '.NET'):
                net_c = "yes"

            # if Leadership or mentorship
            #   leader= "yes"

            # if “visual studio” or “visual basic” or GIT
            #   vs = "yes"

            # if Agile or scrum or “CI/CD” 
            #    agile = "yes"

            # if Design* or concept*
            #   design = "yes"

            # if Github or Gitlab or bitbucket or Jira or Asana or Trello
            #   gith = "yes"

            # if Manage* near project
            #   manag = "yes"

print (
"SOLID and RESTFUL = " + sr

+ "\nAzure or AWS = " + azs

+ "\nDebug or troubleshoot or diagnose or improve = " + debug_exp

+ "\n.net and c# and SQL and Azure = " + net_c

+ "\nLeadership or mentorship = " + leader

+ "\nvisual studio or visual basic or GIT = " + vs

+ "\nAgile or scrum or CI/CD = " + agile

+ "\nDesign or concept = " + design

+ "\nGithub or Gitlab or bitbucket or Jira or Asana or Trello = " + gith

+ "\nManage* near project = " + manag
)

           