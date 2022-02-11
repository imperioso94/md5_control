#!/usr/bin/env python
# program to process md5sum for a list of files contained in a directory
# need a .txt file with md5sum and corresponding filenames on the same raw separated by "\s", a directory containing the files to be controlled
import os
import hashlib
import sys, getopt


stdout_fileno = sys.stdout

file_directory = ""
file_path = ""



if len(sys.argv)==5 or len(sys.argv)==2 :
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hd:m:",["directory=","md5_file="])
    except getopt.GetoptError:
        stdout_fileno.write("\nusage: ./md5_control.py -d <files_directory> -m <md5file.txt>\n")
        sys.exit(2)
else:
    stdout_fileno.write("\nusage: ./md5_control.py -d <files_directory> -m <md5file.txt>\n")
    sys.exit(2)
      
for opt, arg in opts:     
    if opt in ("-d", "--directory"):
        
        files_directory = arg
    elif opt in ("-m","--md5_file"):
        
        file_path = arg
    elif opt in ("-h"):
        stdout_fileno.write("\nusage: ./md5_control.py d <files_directory> -m <md5file.txt>\n\n files_directory is the directory containing just the files to be controlled\n md5file.txt is a file written in the format: md5_sum_hex_code\sfile_name\n\n")
        sys.exit(2)
    else:
        stdout_fileno.write("\nusage: ./md5_control.py d <files_directory> -m <md5file.txt>\n")
        
    



dictionary={}

with open(file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        md5,name = line.split()
        dictionary[name]=md5


file_list = os. listdir(files_directory)

stdout_fileno.write("\n\n controlling the files: \n\n")

count=0
total=0

for file in file_list:
    md5_hash = hashlib.md5()
    a_file = open(files_directory + '/' + file, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    if dictionary['raw_reads/' + file] != digest:
        stdout_fileno.write("\n" + file + "\tERROR\n")
        count +=1
        total +=1
    else:
        stdout_fileno.write("\n" + file + "\tOK\n")
        total +=1
    a_file.close()

stdout_fileno.write("\n Number of corrupted files: "+str(count)+"\n Total number of files controlled: "+str(total)+"\n")




 

