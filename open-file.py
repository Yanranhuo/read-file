# # read-file
# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt


# # Use words.txt as the file name
try:
	fname = input("Enter file name: ")
except:
	print('this is the wrong file name')
  //check if we  it is the valid file name//
fh = open(fname)
con = fh.read()
cont = con.upper()
content = cont.rstrip()
print(content)
