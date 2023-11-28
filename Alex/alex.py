FILENAME = 'test_file.txt'

#def parse_file_and_check_word(file_path, user_input):
#    with open(file_path) as data:
#        while line := data.readline():
#            q, *d = map(str.strip, line.split('-'))
#            if d and q == user_input:
#                return d[0]

#print(parse_file_and_check_word(FILENAME, '.net'))
#print(parse_file_and_check_word(FILENAME, 'C++'))


with open('test_file.txt','r') as file:
  
    # reading each line    
    for line in file:
  
        # reading each word        
        for word in line.split():
  
            # displaying the words           
            if word in ('C++', 'c++',  '.net', '.NET'):
                print(word)
           