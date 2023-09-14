fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    linesp = line.split()
    for mem in linesp:
          if mem not in lst:
                lst.append(mem)
    else:
            continue
lst.sort()
print(lst)
