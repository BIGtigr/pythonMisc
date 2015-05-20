f = open("test.txt", "r")
lines = f.readlines()
print lines
lines.sort(key=len)
print lines
f = open("output.txt", "w")
f.writelines(lines)
f.close



