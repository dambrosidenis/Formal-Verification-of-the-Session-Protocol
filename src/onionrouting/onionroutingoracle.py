#!/usr/bin/python3

import sys

lemmas = ['SanityCheck', 'Secrecy', 'SenderAnonymity']

# Name of the current lemma
lemma = sys.argv[1]
# List of goals to solve
goals = sys.stdin.readlines()

if lemma in lemmas :
    # We want to prioritize goals that aim to solve the source for 'ModelIn' facts and goals containing '~~>'
    PriorityGoals = [ index for (goal, index) in zip(goals, range(len(goals))) if ('ModelIn' in goal) or ('~~>' in goal)]
    if not PriorityGoals :
    # If no goals were found, return the standard goal found by the smart heuristic...
    # ... unless is a splitEqs goal ...
        if goals and 'splitEqs' in goals[0] : print('1')
        else : print ('0')
        exit(0)
    else :
    # ... otherwise print the first occurrence of ModelIn
        print (str (PriorityGoals[0]))
        exit(0)
else :
    # If a new lemma is added to the theory, use the smart heuristic to try to solve it
    print ('0')
    exit (0)