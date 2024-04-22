'''
Katellyn Hyker
Chapter 5 Project 2
File text navigation
Prompt for filename and create a list of the lines of text
Loop that prints the number of lines and asks for a line number
If the input is 0 program ends otherwise the program prints the associated line

'''

file_name = input("Enter file name: ")
with open(file_name) as file:
    lines = [line.rstrip() for line in file]

print("Number of lines:", len(lines))

while True:
    line_num = 0
    num = int(input("Enter a line number or 0 to quit: "))
    if num >0 and num < len(lines):
        print(lines[num-1])
    else:
        if num == 0:
            break