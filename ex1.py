# Open the file in read mode
with open("songs.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Print the line after stripping leading/trailing whitespace
        print(line.strip())