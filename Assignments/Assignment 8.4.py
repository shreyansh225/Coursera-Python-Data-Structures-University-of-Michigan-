#file used is romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)

#Output
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
