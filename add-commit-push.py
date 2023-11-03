import os
import sys

print('Number of arguments:')
print(len(sys.argv))
print('Argument List:')
print(str(sys.argv))

print('add-commit-push')
print('\ngit status')
os.system('git status')

print('\ngit add -A')
os.system('git add -A')
print('\ngit commit -m "Update files."')
os.system('git commit -m "Update files."')
print('\ngit push')
os.system('git push')