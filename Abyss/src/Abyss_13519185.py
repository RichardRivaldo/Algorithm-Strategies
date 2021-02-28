# Richard Rivaldo
# 13519185 - K04

# Read and process the subjects in each line of the file
def readIntoList(filename):
    # Open and Read File
    file = open(filename, 'r')
    
    # Initialize an empty list
    fullList = []
    
    # Preprocess the string
    for line in file:
        # Ignore empty line that contains newline
        if(line != '\n'):
            # Clean the text
            line = line.replace(".", "")
            line = line.replace('\n', "")
            line = line.replace(" ", "")
            
            # Split and get each subjects
            lineList = (line.split(","))
            
            # Append to the end list
            fullList.append(lineList)
    
    # Close the file
    file.close()
        
    return fullList


# Topological Sort with list comprehension and recursive approach
# This list comprehension acts analogously with the concept of graph as
# the data structure in most topological sort programs
def topologicalSort(subject):
    # Check if the input file contains any subject
    # If not, terminate all process
    if(len(subject) == 0):
        print("\nZERO ZERO ZERO")
        print("Is it just me, or I cannot see a thing in the file you just give me?")
        print("PROCESS TERMINATED: Code 0, invalid file!")
        return
    
    # Initialize boolean to track the sorting process
    # If the graph does not contain any vertex with 0 In-Degree
    foundOne = False
    
    # Initialize an empty list of list that contains yet another list 
    # of valid subject to take each semester
    semSet = [] 
    
    # Init a list to contain a list of every taken subject each semester
    listSem = []
    
    # Find a subject without any prerequisites (In-Degree = 0)
    for prereq in subject:
        if(len(prereq) == 1):
            # Append the subject
            listSem.append(prereq)
            
            # Change the value of the boolean to indicate that at least
            # one vertex has no input edges
            foundOne = True
    
    # Check if the subject can be allocated with Topological Sort schema
    # If there is no subject without input edges, terminate the process
    if(not foundOne):
        print("\nONE ONE ONE")
        print("BEEPBEEP. Endure it anymore, and we will break!")
        print("This is as far as we go, mate. Goodbye..")
        print("PROCESS TERMINATED: Code 1: No more valid subject to take!")
        return
    
    # Decrease and Conquer Approach
    # Remove the subject from the all subject-prereq list
    subject = [prereq for prereq in subject if prereq not in listSem]
    
    # Append the list of the semester to the result list
    semSet.append(listSem)
    
    # Init an empty list to contain an updated version of the subject-prereq list
    updatedSubject = []
    
    # Iterate over the remaining original subject-prereq list
    for remaining in subject:
        # Iterate over the result we got on each semester
        for prereq in listSem:
            # Remove every dependencies that the choosen subject of each semester
            # with remaining subjects from the list
            if(prereq[0] in remaining):
                remaining.remove(prereq[0])
        # Append the subject to the list of updated subjects
        updatedSubject.append(remaining)
    
    # Join every choosen subjects of each semester into a string
    string = ', '.join([prereq[0] for prereq in semSet[0]])
    
    # Make the counter for every semester global to keep track of the count
    global semCounter
    
    # Initialize an array to contain roman numbers
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",]
    
    # Format the string to print the result of each semester with roman number
    print(f'Semester {roman[semCounter]}:'.format(roman[semCounter]), string)
    
    # Increment of the semester counter
    semCounter += 1
    
    # Main basis of the recursion
    # No more subjects left in the list
    # (No more nodes left in the graph)
    if(len(updatedSubject) == 0):
        return
    
    # Handle possibility of having more than 8 Semester
    # to take all subjects
    if(semCounter == 8 and len(updatedSubject) != 0):
        return
    
    # Recursively call the function until all subjects are allocated to every semester
    # i.e. no more subjects left to choose from
    return topologicalSort(updatedSubject)


# Main Program
def abyss():
    # Abyss is Chaos in Greek :)
    print("HELL-OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    print("Don't know what subject to take? We are here!\n")
    print("Abyss: Your chaos solver is ready to help!\n")
    
    # Receive a .txt file name as an input
    filename = input("Give us a food! FYI, we eat .txt files~~\n")
    
    print("\n")
    
    # Init semCounter as a global variable
    # Track the counter of Roman Number in the list
    global semCounter
    semCounter = 0
    
    # Try to read the file into list of subjects-prerequisites
    try:
        # Read the file into list and save it to subject
        subject = readIntoList(filename)
    except:
        # Error message if file invalid or not found
        print("Invalid: Wrong file name or file not found!")
        print("We, Eat, .txt, Files!")
        return
    
    # Do topological sorting and gives output
    topologicalSort(subject)
    
    # ~~~
    print("\nMay chaos not be with you anymore.. and me..")
    print("But Abyss is still here. Call me anytime!")
    print("A       B          B           Y        S")
    
    return

# Call from terminal
if __name__ == "__main__":
    abyss()


# Old approach without recursive
# Works, but does not give optimal output based on the concept of Topological Sorting
# =============================================================================
# # Check if a subject is a prerequisite of other subject
# def checkPrereq(subject, new, target):
#     # Find Target Subject
#     prereqList = []
#     foundNew = False
#     foundTarget = False
#     
#     for prereq in subject:
#         if(prereq[0] == target):
#             prereqList = prereq
#             if(new in prereqList):
#                 foundNew = True
#         if(prereq[0] == new):
#             prereqList = prereq
#             if(target in prereqList):
#                 foundTarget = True
#                 
#     # Check if new is in the prerequisite list of target
#     return foundNew and foundTarget
# 
# def topologicalSort(subject):
#     
#     # Init a copy of Subject List and an empty list to contain results
#     copySubject = subject
#     result = []
#     matkul = ""
#     
#     # Iterate until the subject list is empty -> no more nodes in graph
#     while(len(subject) != 0):
#         # Find subject without any input edges
#         for subjects in subject:
#             
#             # Init empty list to contain subjects in each semester
#             semesterList = []
#             
#             # Get the subjects if the length of the list is 1 -> In-Degree = 0
#             if(len(subjects) == 1):
#                 matkul = subjects[0]
#                 semesterList.append(matkul)
#                 
#                 # Remove the subject from current list
#                 subject.remove(subjects) 
#                 
#                 # Append the subject to corresponding semester
#                 for rest in subject:
#                     if(len(rest) == 1 and not checkPrereq(copySubject, rest[0], matkul)):
#                         matkul = rest[0]
#                         semesterList.append(matkul)
#                         
#                         # Remove the subject from current list
#                         subject.remove(rest)
#                         
#                 # Add each semester to the end result
#                 result.append(semesterList)
#             
#             # Remove the subject from remaining list (graph nodes connected with the subject)
#             for choosen in semesterList:
#                 for remaining in subject:
#                     if(choosen in remaining):
#                         remaining.remove(choosen)                
#                     
#     return result
# 
# def schedule(sortedResult):
#     # Init counter
#     counter = 1
#     
#     # Iterate over result
#     for semester in sortedResult:
#         # Can take only one subject each semester
#         if(len(semester) == 1):
#             print("Semester", counter, ":", semester[0])
#         else:
#         # Can take than one subjects each semester
#             print("Semester", counter, ":", end = " ")
#             for idx in range(len(semester)):
#                 if(idx == len(semester) - 1):
#                     print(semester[idx])
#                 else:
#                     print(semester[idx], end = ", ")
#         counter += 1
# =============================================================================