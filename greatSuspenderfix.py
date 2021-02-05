import webbrowser
file = open("data.txt", "r") 
for line in file: 
    for i in range(len(line)):
        if line[i] == "u" and line[i+1] == "r" and line[i+2] == "i" and line[i+3] == "=":
            webbrowser.open(line[i+4:-1], 2)
file.close() 