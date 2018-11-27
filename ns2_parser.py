# Author: Erin Schick
# Date of Last Edit: November 26th, 2018

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    
    #Remove original file
    remove(file_path)
    
    #Move new file
    move(abs_path, file_path)

def main(): 

	#It takes the XML file name here
    replace('b_copy.xml', 'ns2:', '')


if __name__ == "__main__": 

    # calling main function 
    main()