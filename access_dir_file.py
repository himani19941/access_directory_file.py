
from pathlib import Path
import os


def access_files(home_path):

    """It will find the path of .py files inside the home directory and count the total number of .py file.
    Moreover it will segregate the total .py files on basis of their content weather they contains classes,
    function or implemented inheritance"""

    path_list, li_fun, li_class, li_normal, li_inheritance = [], [], [], [], [] # empty lists to store path
    # of all files and lists to store similar content

    for root, directory, file_folder in os.walk(home_path):
        for inside_file in file_folder:
            if inside_file.endswith('.py'):  # searches .py file from all the files
                path_list.append(os.path.join(root, inside_file))  # all the .py paths are getting stored

    for path in path_list:  # takes each path which is absole from path_list
        # path1 = os.path.abspath(path)  # converts in absolute path
        flag = False
        with open(path, 'r', encoding='latin-1') as f:  # opening, reading and encoding of file
            li_lines = f.readlines()  # list of lines getting stored in list li_lines

        for line1 in li_lines:  # loop through each line in list li_lines
            count = 0
            if flag == True:
                break
            line = line1.split(' ')  # splitting each line with a blank space

            for word in line:  # class Apple()
                if flag == True:
                    break
                elif word == 'class':
                    count = count + 1
                    continue
                elif count == 1:
                    count = 0
                    li_apple = list(word)

                    for char in li_apple:
                        if char == '(' or char == ')':
                            li_inheritance.append(path)
                            flag = True
                            break
                        else:
                            li_class.append(path)
                            flag = True
                            break
                elif word == 'def':
                    li_fun.append(path)
                    flag = True
                    break
        else:
            li_normal.append(path)  # else clause for 'for loop',if no break statement will occure
            # in for loop this else will get executed

    path_list_12 = 'Absolute path of each .py file', path_list
    count_files2 = "Count of total Executable files are: ", len(path_list)  # by len method, calculating
    # length of list which is equal to number of files also
    count_fun_file2 = 'Count of Files using function: ', len(li_fun)
    count_class_file2 = 'Count of Files using classes: ', len(li_class)
    count_normal_file2 = 'Count of Files using neither classes nor functions: ', len(li_normal)
    count_inheritance_file2 = 'Count of Files using Inheritance: ', len(li_inheritance)

    return path_list_12, count_files2, count_fun_file2, count_class_file2, count_normal_file2, count_inheritance_file2


p = Path.home()  # We can get Path of the home directory
p = str(p)

path_list_1, count_files, count_fun_file, count_class_file, count_normal_file, count_inheritance_file = access_files(p)
# function call,passing the argument
print(path_list_1, '\n', count_files, '\n', count_fun_file, '\n', count_class_file, '\n', count_normal_file,'\n',
      count_inheritance_file)  # printing the output
