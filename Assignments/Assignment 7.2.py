# Use the file name mbox-short.txt as the file name
total=0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    count=count+1
    pos=line.find(':')
    value=line[pos+1:]
    total=total+float(value)
    avg=total/count
print("Average spam confidence:",avg)

#Output:
#Average spam confidence: 0.750718518519
