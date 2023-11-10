import os
import shutil
# different types of data containers

# lists/2d lists
"""
list1 = ["This", "is", "list", 1]
list2 = ["This", "is", "list", 2]
twoDimensionalList = [list1,list2]
for list in twoDimensionalList:
    print(f'This is list number {list[3]}.')
"""
# tuple is a list but ordered and unchangeable (uses these fellows! ->)
"""
studentData = ("John", "Smith", 20)
"""
# a set is a tuple but has no order and no index. cannot have duplicate values
"""
utensils = {"fork", "knife", "spoon"}
utensilListFromSet = []
for utensil in utensils:
    utensilListFromSet.append(utensil)
print(f'Despite starting with the tuple [fork, knife, spoon], the tuple now reads {utensilListFromSet}. (If they are the same just rerun it :)')
"""
#dictionaries are a changeable, unordered collection of key:value pairs.
"""
playerStats = {'Gold': 20,
               'Health': 73.9,
               'Mana': 200
               }
print(playerStats['Gold'])
"""
# back to the non data containers stuff!
# *args packs all positional arguments into a tuple

"""
def argsAdd(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(argsAdd(1,2,3,4))
"""
# **kwargs packs all keyword arguments into a dictionary
"""
def sayHi(**kwargs):
    print("Hello, your name is ", end="")
    for key,value in kwargs.items():
        print(value, end=" ")
sayHi(title = "Mr.", first = "John", middle = "Doe", last = "Smith")
"""
#exceptions are events detected during program running that interrupt the flow of a program.

#this function will cause an exception!
"""
def divideByZero(number):
    return (number/0)
# so use a try/except statement to make sure we don't crash!
try:
    print(divideByZero(5))
except ZeroDivisionError as exception:
    print(f'Hey! No dividing by zero! Error code: {exception}')
except Exception as exception: #any other exception
    print(f'Something went wrong :( Error code: {exception}')
else:
    print("It worked :)")
# use a finally to run something no matter what happens
finally:
    print("This will always be printed")
"""
#file detection. reccomended to import os
"""
filePath = "C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\fileDetection.txt" #dont forge to use double slashes!
if os.path.exists(filePath) == True : #can just be if os.path.exists(filePath):
    print(f'The file path "{filePath}" exists!')
    if os.path.isfile(filePath):
        print('Additionally, the file path leads to a file.')
    if os.path.isdir(filePath):
        print('Additionally, the file path leads to a directory.')
else:
    print(f'Could not find file path "{filePath}"')
"""
#file reading
"""
file = 'C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\fileReading.txt'
try:
    with open(file) as file: #using open() automatically closes the file after use
        print(file.read())

except FileNotFoundError:
    print(f'File "{file}" not found.')

except Exception as exception:
    print(f'Exception occured: {exception}')
"""
#file writing/appending
"""
try:
    with open('fileWriting.txt','w') as file: #mode 'w' is for Write. Write will overwrite ALL DATA.
        file.write("You just wrote to a file!\nYou also wrote on multiple lines!")
except FileNotFoundError:
    print(f'File "{file}" not found.')

except Exception as exception:
    print(f'Exception occured: {exception}')
"""
"""
try:
    with open('fileWriting.txt','a') as file: #mode 'a' is for append. Will write on next the availiable line
        file.write("Don't worry, this text didn't overwrite your old data!")
except FileNotFoundError:
    print(f'File "{file}" not found.')

except Exception as exception:
    print(f'Exception occured: {exception}')
"""
#copying files
"""
source = "C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\copyableFile.txt"
destination = "C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\copyFile.txt"
shutil.copy(source,destination) #can use copyfile or copy2, not sure what they do tho
"""
#file moving
"""
mainSource = "C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\moveableFile.txt"
mainDestination = "C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\randomDirectory\\moveableFile.txt"
directorySource = mainDestination
directoryDestination = mainSource
try:
    if os.path.exists(mainSource): #can be removed if you dont care about overwriting
        print("File is in pythonPractice directory, moving back to randomDirectory")
        os.replace(mainSource,mainDestination)
    else:
        print("File is in randomDirectory, moving back to pythonPractice directory")
        os.replace(directorySource,directoryDestination)
except FileNotFoundError:
    print("File not found")
except Exception as exception:
    print(f'Error occurred: "{exception}"')
"""
#file deletion
"""
try:
    shouldDeleteFile = input('Do you want to delete this file? Y/N:')
    if shouldDeleteFile.casefold() == ' Y'.casefold() or shouldDeleteFile.casefold() == 'Y'.casefold():
        path = 'C:\\Users\\datha\\PycharmProjects\\learnPythonFr\\pythonPractice\\trashFile.txt'
        os.remove(path) #use os.rmdir to remove directories not containing files, use shutil.rmtree to remove directories with files
    else:
        print("ok")
except FileNotFoundError:
    print("File not found")
except Exception as exception:
    print(f'Error code: {exception}')
"""