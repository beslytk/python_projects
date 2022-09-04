# context manager using class -> using __enter__ and __exit__ methods
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file


    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

print(f.closed)
###########################################################3
# context manager using function

#### Using contextlib ####
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f                  # run till here for line -> with open_file('sample.txt', 'w') as f: -> setup
    finally:
        f.close()                # run after the with block exits -> teardown

# using try finally, will ensure that teardown block runs even if there occurs some error

with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)

###########################################################3
# Practical Example
#### CD Example ####
import os

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)
###########################################################3
# equivalent usage with context manager
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd
        os.chdir(destination)
        yield                        # not using any variable in context mgr, so no need to yield anything
    finally:
        os.chdir(cwd)                   # teardown

with change_dir('Sample-Dir-One'):
    print(os.listdir())
with change_dir('Sample-Dir-Two'):
    print(os.listdir())
