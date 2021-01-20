import filecmp
file1 = "hi.txt"
file2 = "w.txt"
comp = filecmp.cmp(file1, file2)
print(comp)
