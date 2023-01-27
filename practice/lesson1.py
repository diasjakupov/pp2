inputT = ""
processedData = []


while inputT != "0":
    inputT = input()
    if inputT != "0":
        processedData.append(int(inputT))




print("*"*8)

print(f"max: {max(processedData)}")
print(f"min: {min(processedData)}")
print(f"sum: {sum(processedData)}")
print(f"av: {(sum(processedData)/len(processedData))}")

unique = set(processedData)


for i in unique:
    print(f"Unique: {i}")

for i in unique:
    print(f"{i} = {processedData.count(i)}")

