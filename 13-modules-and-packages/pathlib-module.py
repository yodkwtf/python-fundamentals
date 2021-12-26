# import Path class from `pathlib` module
from pathlib import Path

# create an instance of class (relative path by default)
path = Path()

# check if a dir exists
path = Path('exercises')
print(path.exists())

# make a new dir
path = Path('testing')
path.mkdir() # will create a `testing` dir in root
# delete a dir
path.rmdir() # will remove the `testing` dir