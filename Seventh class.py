#file Input/Output :- python can be used to perform operations on  file.(read and write data)

#types of all files
#01 TEXT FILE : txt, docx, log, etc
#02 BINARY FILE : mp4, mov, png, jpeg, etc

# OPEN , READ AND CLOSE FILE 
#  f = open("file_name", "mode")

#file name ka mtlb :- sample.txt &  demo.docx
# mode ka mtlb :- ( r - read mode )  &  ( w - write mode )
                
# 'r' ~ open foe reading (deafault)
# 'w' ~ open for writing, truncating the first file
# 'x' ~ create a new file and open for it writing
# 'a' ~ open for writing , appending to the end the file if it exists
# 'b' ~ binary mode
# 't' ~ text mode
# '+' ~ open a disk file for upadating (reading and writing)

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


#READING FILE

# data = f.read()        >  reads entire file
# data = f.readline()      >      reads one line at time 

f = open("demo.txt", "r")
data = f.read()
print(data)
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

print(type(data))
f.close()

#WRITING FILE 'w'


f = open("demo.txt", "w")

f.write("\n kumar.")

f.close()
