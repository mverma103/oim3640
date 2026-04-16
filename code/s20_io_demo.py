# Read entire file
#with open("data/s20.txt") as f:
    # text = f.read()
    # text = f.readline()
    # text = f.readlines()

    # print(text)

# Read file line by line (best for large files)
# with open("data/s20.txt") as f:
#     for line in f:
#         print(line.strip()) 

# Write to file ('w' = overwrite, 'a' = append)
with open("data/s20_output.txt", "w") as f:
    f.write("Hello World!\n")