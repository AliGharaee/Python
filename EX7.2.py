fname = input("Enter file name: ")
fh = open(fname)
count = 0
t = 0
for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            n = float(line[20 : ])
            t = t + n
            count = count + 1
av= t / count
print('Average spam confidence:' , av)
