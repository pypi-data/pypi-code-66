from os import listdir
from os.path import isfile, join


# Returns a list of every file in a folder
def get_all_files(group):
    return [f for f in listdir("dictionaries/" + group + "/") if isfile(join("dictionaries/" + group + "/", f))]


# Prints every filename in a folder, makes you select one of them and returns the according path
def select_file(group):
    onlyfiles = get_all_files(group)
    print("Available files in " + group.upper() + ":\n" + "*"*15)
    for file in onlyfiles:
        print(">\"" + file[:-4] + "\"")
    print("*"*15)
    name = input("Which of the above files do you want to edit?\n")
    return "dictionaries/" + group + "/" + name + ".txt"


# Returns a list of every line in a file
def list_file(fname):
    words_list = list()
    file = open(fname, "r", encoding="utf-8")
    for line in file:
        if line != "\n":
            words_list.append(line.rstrip())
    file.close()
    return words_list
