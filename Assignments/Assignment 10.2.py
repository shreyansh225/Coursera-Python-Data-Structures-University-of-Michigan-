name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
di=dict()
for line in handle:
    if line.startswith("From "):
    	pos=line.find(":")
    	lst.append(line[pos-2:pos])
for word in lst:
    di[word]=di.get(word,0)+1
newlst=list()
for key,val in di.items():
    newtup=(key,val)
    newlst.append(newtup)
newlst=sorted(newlst)
for key,val in newlst:
    print(key,val)
