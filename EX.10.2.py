fname = input("Enter file name: ")
fh = open(fname)
names = list()
for line in fh:
    if line.startswith("From "):
        line = line.split()
        names.append(line[5])
hour = list()
for h in names:
            hour.append(h.split(':')[0])
counts = dict()
for h in hour:
        counts[h] = counts.get(h,0) + 1
for h,f in sorted(counts.items()):
    print(h,f)
