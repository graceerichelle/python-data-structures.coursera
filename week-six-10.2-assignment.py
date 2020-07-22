name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
file_dict={}
for line in handle :
    line=line.rstrip()
    if line.startswith("From ") : 
            words=line.split()
            time=words[5]
            hours=time[:2]
            file_dict[hours]=file_dict.get(hours,0)+1
for k,v in sorted (file_dict.items()) :
    print(k,v)
