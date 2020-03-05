fname = input("Enter file:")
fhand = open(fname)
rjec = {}
for i in fhand:
    if i.startswith("From") and len(i.split()) > 2:
        line = i.split()
        if not rjec.has_key(line[5][:2]):
            rjec[line[5][:2]] = 1
        else:
            rjec[line[5][:2]] += 1
                
key = sorted(rjec)
for i in key:
    print(i, rjec[i])
