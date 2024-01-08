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
file = open("File_1.txt", 'w')
str1 = "Line-1\n"
str2 = "Line-2\n"
list = ["Line-3\n","Line-4\n"]
set = {"Line-5\n","Line-6\n"}
val = 321
flt = 3.14
file.write(str1 + str2 )
file.writelines(list)
file.writelines(set)
file.write(str(val) + "\n" + str(flt))
file.flush()
file.close()


# program to read from file
file = open("File_1.txt", 'r')

begining = file.tell() ## get current position in file
print("begining: " , begining)

# seek(int offset ,int reference)
# offset : +value for right and -value for left
# reference:(0,1,2) By default 0.
# 0: sets the reference point at the beginning of the file 
# 1: sets the reference point at the current file position 
# 2: sets the reference point at the end of the file 
file.seek(begining) # reference by default 0.

print("Total Characters : " , len(file.read()))

file.seek(begining)
print("Total Lines : " , len(file.readlines()))



file.seek(begining)
## read all line as String
print("------------")
read = file.read() 
print("type(read) : " , type(read))
print("read : \n",read)


file.seek(begining)
## read only one line as String
print("------------")
readline = file.readline() 
print("type(readline) : " , type(readline))
print(readline)
readline = file.readline() 
print(readline)


file.seek(begining)
## read all lines as List
print("------------")
readlines = file.readlines() 
print("type(readlines) : " , type(readlines))
print("readlines : ", readlines)

## Read lines of file directly with for loop
file.seek(begining)
print("------------")
for line in file:
    print(line)

file.close()
