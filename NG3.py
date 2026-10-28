# Read data from input file
f = open("input.txt", "r")
lines = f.readlines()
f.close()

# Count total number of lines
print("Total number of lines:", len(lines))

# Extract first two lines
data = lines[:2]

# Write data into a new file
f = open("output.txt", "w")
f.writelines(data)
f.close()

print("First two lines written to output.txt")