name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts = dict()
handle = open(name)

for line in handle:
    if line.startswith('From '):
        line=line.split()
        counts[line[1]]=counts.get(line[1],0)+1
bigword=None
bigcount=0
for key,val in counts.items():
  if bigcount==0 or val>bigcount : 
        bigcount=val
        bigword=key
print(bigword,bigcount)
