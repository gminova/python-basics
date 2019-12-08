try:
    print('writing...')
    file = open('exceptions_and_files/myfile.txt', 'w')
    file.write('Trololololo')
finally:
    file.close()
    print('complete!')
