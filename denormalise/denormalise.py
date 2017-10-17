MIN = 597000
MAX = 61292000

fileIn = open("input","r")
fileOut = open("output", "w")

def denormalise(input):
    return str(float(input) * (MAX - MIN) + MIN)

for line in fileIn:
    fileOut.write(denormalise(line) + "\n")


