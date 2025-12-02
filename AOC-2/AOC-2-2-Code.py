inputIDRanges = ""
sumIDs = 0
with open("AOC-2-1-Input.txt", "r") as file:
    inputIDRanges = file.readline()
IDranges = inputIDRanges.split(",")
for IDrange in IDranges:
    IDrangeStart = int(IDrange.split("-")[0])
    IDrangeStop = int(IDrange.split("-")[1])
    for ID in range(IDrangeStart, IDrangeStop+1):       
        for dividor in range(2,len(str(ID))+1):
            if len(str(ID))%dividor == 0:
                parts = []
                for i in range(dividor):
                    parts.append(str(ID)[i*len(str(ID))//dividor:(i+1)*len(str(ID))//dividor])
                first = parts[0]
                same = True
                for part in parts:
                    if part != first:
                        same = False
                        break
                if same:
                    sumIDs+=int(ID)
                    break             
print(sumIDs)

