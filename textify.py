with open("white.txt", "r+") as f:
    line = f.read()
    lines = line.split("<>")
    for newline in lines:
        f.write(newline + "\n")
    