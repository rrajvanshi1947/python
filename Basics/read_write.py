#The file is created only once within the folder no matter how may times you run it.
fw = open('textfile.txt', 'w')
fw.write('This is a sample text file for Python.\n')
fw.write('I\'m really learning it well with Bucky. He is quite a teacher.\n')
fw.close()


fr = open('textfile.txt', 'r')
readText = fr.read()
print(readText)
fr.close()
