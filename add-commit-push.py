import os
import sys

commitCommand = '\ngit commit -m "Update files."'
if len(sys.argv) == 3:
    if sys.argv[1] == '-m':
        commitCommand = '\ngit commit -m "' + sys.argv[2] + '"'

print('add-commit-push')
print('\ngit status')
os.system('git status')

print("Continue with add,commit,push? (y):")
userInput = input()
if userInput != 'y':
    print('Canceling program')
    quit()

print('\ngit add -A')
os.system('git add -A')
print(commitCommand)
os.system(commitCommand)
print('\ngit push')
os.system('git push')