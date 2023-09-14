# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inpr = inp.rstrip()
print(inpr.upper())
