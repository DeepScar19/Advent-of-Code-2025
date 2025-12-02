inputIDRanges = ""
sumIDs = 0
with open("AOC-2-1-Input.txt", "r") as file:
    inputIDRanges = file.readline()
IDranges = inputIDRanges.split(",")
for IDrange in IDranges:
    IDrangeStart = int(IDrange.split("-")[0])
    IDrangeStop = int(IDrange.split("-")[1])
    for ID in range(IDrangeStart, IDrangeStop+1):
        if len(str(ID))%2==1:
            pass
        elif str(ID)[:len(str(ID))//2:] == str(ID)[len(str(ID))//2:]:
            sumIDs+=int(ID)
print(sumIDs)