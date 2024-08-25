'''
author : Jaydatt
file read write 

Method-1 :
file =  open(fileName, "r" or "w")
......
file.close()

Method-2 (close file automatically):
 with open(fileName, "r" or "w") as f: 
 ......codes....
 .......


Methods: 

filevar.write(string) : Add a string to the end of the file. filevar must refer to a file that has been opened for writing.

filevar.writelines(List or Set or Array) : Add a string to the end of the file. filevar must refer to a file that has been opened for writing.

filevar.read() or filevar.read(n) : Read and return a string of n characters, or the entire file as a single string if n is not provided.

filevar.readline() or filevar.readline(n) : Read and return the next line of the file with all text up to and including the newline character

filevar.readlines() or filevar.readlines(n) :
Returns a list of strings

filevar.tell() : get current position in file

filevar.seek(int offset ,int reference) or
filevar.seek(int offset) reference By default 0   : 
    offset : +value for right and -value for left
    reference:(0,1,2) By default 0.
    0: point at the beginning of the file 
    1: point at the current file position 
    2: point at the end of the file 


'''
# program to write into file 
file = open("File_1.csv", 'w')

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

file.write("Name, Age, Sport\n")

# output each of the rows:
for item in olympians:
    row_string = "{},{},{}\n".format(item[0], item[1], item[2])
    file.write(row_string)

file.close()


# program to read from file
file = open("File_1.csv", 'r')
read = file.read()
lines = read.split('\n')
for line in lines:
    words = line.split(',')
    print(words)
 
file.close()


