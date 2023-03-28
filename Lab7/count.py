
import os.path

filename = "count.txt"


if not os.path.isfile(filename):
 print ("File does not exist")
 #initialise file here
 writeNumber(0)




def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
        return number
    except IOError:
        return 0
def writeNumber(number):
    with open(filename, "wt") as f:
 # write takes a string so we need to convert
         f.write(str(number)) 
# main
num = readNumber()
num += 1
print (f'we have run this program {num} times')

writeNumber(num)

 