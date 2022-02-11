# md5_control

*This script is made to let you automate the integrity control of downloaded files.
Given a directory containing the files to be controlled and a text file listing for every
row the md5_sum hexadecimal code and the corresponding file name separated by "\s", 
the program calculate the correspondece of md5_sum hex inside the text file and the ones 
calculated locally.*


### usage :       ./md5_control.py -d <files_directory> -m <md5file.txt>

  * <files_directory> is the directory containing the files
  * <md5file.txt> is the text file
  * both arguments must contain full paths 
