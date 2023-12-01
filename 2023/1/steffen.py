with open('./input1') as f:
    lines = f.readlines()

total_sum=0

for line in lines:
    idxs = [i for i in range(0, len(line)) if line[i].isdigit()]
    total_sum += int(line[idxs[0]])*10
    total_sum += int(line[idxs[len(idxs) - 1]])

print(total_sum)