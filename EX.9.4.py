fname = input("Enter file name: ")
fh = open(fname)
names = list()
for line in fh:
    if line.startswith("From:"):
        line = line.split()
        names.append(line[1])
counts = dict()
for name in names:
        counts[name] = counts.get(name,0) + 1
bigcount = None
bigname = None
for name,count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count
print(bigname, bigcount)
