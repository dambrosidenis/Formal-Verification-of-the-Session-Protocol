#! /usr/bin/python3

import sys, json

# Location of the file with the priority lists
PRIORITIES = './e2epriorities.json'

# Auxiliary functions that, given a the name of a lemma, returns a ordered list of goals
def loadPriorities (lemmaName) :

    # Open a file and parse its contents as a Python dictionary
    with open(PRIORITIES) as file: oraclesPriorities = json. loads(file.read())

    # Select the correct priority list based on the name of the lemma
    priorities = oraclesPriorities[lemmaName]
    
    # Return the list
    return priorities


# Name of the current lemma
lemma = sys.argv[1]

# List of goals to solve
goals = sys.stdin.readlines()

try :
    # If the name of the lemma is defined within the file load the relevant priority list ...
    priorities = loadPriorities(lemma)
except :
# ... else revert to the standard smart heuristic
    print('0')
    exit(0)

# Search for the index of the highest priority goal present in the goals list
for i in range(len(priorities)) :
    for j in range(len(goals)) :
        # If found, print its index to solve it
        if priorities[i] in goals[j] :
            print(str(j))
            exit(0)

# If no priority goal is found within the list, use the standard smart heuristic
print('0')
exit(0)