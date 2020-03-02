name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith("From "):continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) +1

bigcount = None
bigword = None
for k,v in count.items():
    if bigcount == None or v > bigcount:
        bigword = k
        bigcount = v 
print(bigword, bigcount)

#Output : cwen@iupui.edu 5
