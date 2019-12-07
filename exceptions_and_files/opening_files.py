file = open('exceptions_and_files/myfile.txt')
print(file.read(15))  # print first 15 chars
file.close()

# # write mode
# open("exceptions_and_files/myfile.txt", "w")

# # read mode (default mode)
# open("exceptions_and_files/myfile.txt", "r")
# open("exceptions_and_files/myfile.txt")

# # binary write mode
# open("exceptions_and_files/myfile.txt", "wb")
