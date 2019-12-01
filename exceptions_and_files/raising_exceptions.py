try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError

# alternative
# try:
#    num = 5 / 0
# except:
#    print("An error occurred")
#    raise
