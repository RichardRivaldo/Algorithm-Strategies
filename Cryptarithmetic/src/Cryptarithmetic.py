# Library
import time

# Function to open and process file contents into a list of strings
def read_file(filename):
    file = open(filename, "r")
    
    # Global variable to count program run time 
    # Excluding the amount of time needed to read the file
    global startTime
    startTime = time.time()
    
    # Empty list to contain processed letters
    letters = []
    for line in file:
        # Remove excess spaces and newlines
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        
        # Remove non-letter chars
        line = "".join([chars for chars in line if chars.isalpha()])
        
        # Append processed file lines into the list
        if line != "":
            letters.append(line)
    return(letters)

# Function to find and map all distinct alphabets in the equation
def map_distinct(letters):
    # Initiate empty lists to contain processed results
    words = [] # List of distinct chars
    mapped = [] # List of list of every indexes of each char
    
    # Find distinct chars and append it to words
    for word in letters:
        for i in range(len(word)):
            if(word[i] not in words):
                words.append(word[i])
    
    # Join distinct chars into a string
    distinct = "".join(words)
    
    # Map every char in each words into indexes based on distinct string
    for letter in letters:
        mapped.append([distinct.find(char) for char in letter])
    return(mapped)

# Function to find spaces of possible numbers
def permute(targetList):
    # Initiate empty list to contain permutation results
    resultList = []
    
    # Recursive basis: empty target
    if(len(targetList) == 0):
        return(resultList)
    # Recursive basis: target length = 1
    elif(len(targetList) == 1):
        return([targetList])
    # Recurrents
    else:
        for idx in range(len(targetList)):
            for comp in permute(targetList[:idx] + targetList[(idx + 1):]):
                resultList.append([targetList[idx]] + comp)
        return(resultList)

# Function to match every possibilities into the words
def matching_to_numbers(target, spaces):
    # Join every chars into a single string and change its type into integer
    match = "".join(str(spaces[chars]) for chars in target)
    return(int(match))

# Brute Force approach to try finding every possible solutions of the cryptarithmetic
def search(list_of_idx):
    # Initiate empty list to contain temporary and final solutions of the equation
    solution_list = []
    final = []
    
    # Contains the numbers of test done to find the solutions
    count = 0
    
    # Find possible solutions
    for possibles in permute(list('1234567890')):
        # Sum all operands after matched and no leading zeros
        totalOperand = 0
        for idxs in list_of_idx[:-1]:
            # Handle leading zeros
            if(len(str(matching_to_numbers(idxs, possibles))) == len(idxs)):
                totalOperand += matching_to_numbers(idxs, possibles)
        
        # The result of the equation
        if(len(str(matching_to_numbers(list_of_idx[-1], possibles))) == len(list_of_idx[-1])):
            results = matching_to_numbers(list_of_idx[-1], possibles)
        else:
            results = -1
        
        # Check if the results is true
        if(totalOperand == results):
            # Append the solutions of each matching numbers
            for idx in (list_of_idx):
                match = matching_to_numbers(idx, possibles)
                solution_list.append(match)
        
        # Partition the list into a final solution list
        eqLength = len(list_of_idx)
        for i in range(0, len(solution_list), len(list_of_idx)):
            temp = solution_list[i: (i + eqLength)]
            
            # Handle non-unique solution
            if(temp not in final):
                final.append(temp)
                
        # Increment the tests count
        count += 1
    return(final, count)

# Cryptarithmetic procedure to run all processes needed
def cryptarithmetic(filename):
    # Read the file and process it
    letters = read_file(filename)
    
    # Map each distinct chars
    list_of_idx = map_distinct(letters)
    
    # Searching for solutions
    sols, count = search(list_of_idx)
    
    # Width for right alignment
    width = len(letters[-1])
    
    # Output original file
    print("Cryptarithmetic:")
    for i in range(len(letters[:-2])):
        print(letters[i].rjust(width))
    print(letters[-2].rjust(width), "+")
    print("-" * (width + 2))
    print(letters[-1])
    print()
    
    # Output solutions
    if(len(sols) == 0):
        print("No solutions found!")
    else:
        solsOf = 1
        for solution in sols:
            print("Solution " + str(solsOf) + ":")
            for j in range(len(solution[:-2])):
                print(str(solution[j]).rjust(width))
            print(str(solution[-2]).rjust(width), "+")
            print("-" * (width + 2))
            print(solution[-1])
            solsOf += 1
            print()
        print()
    
    # Run Time
    totalTime = time.time() - startTime
    print("Total Duration : ", totalTime, "seconds")
    
    # Total tests
    print("Total Testcases: ", count, "testcases")
    
cryptarithmetic("filename.txt")