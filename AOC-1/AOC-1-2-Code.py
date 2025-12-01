rotator = []
pos = 50
zeros = 0
for i in range(100):
    rotator.append(i)
with open("AOC-1-1-Input.txt", "r") as file:
    for turn in file:
        if turn[0] == "L":
            for i in range(int(turn[1:])):
                pos -=1
                if rotator[abs(pos%100)] == 0:
                    zeros+=1
        elif turn[0] == "R":
            for i in range(int(turn[1:])):
                pos +=1
                if rotator[abs(pos%100)] == 0:
                    zeros+=1
print(zeros)