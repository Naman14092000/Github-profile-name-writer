#1/usr/bin/python
import datetime
import random
import time
# A = [0,-1,-2,-3,3,5,10,12,18,19,20,21];
# L = [0,-1,-2,-3,-4,7,14,21]
# E = [0,-1,-2,-3,-4,7,14,21,3,10,17,5,12]
# K = [0,-1,-2,-3,-4,17,11,5,13,21]
# H = [0,-1,-2,-3,-4,5,12,21,20,19,18,17]
# J = [0,7,14,-4,3,10,17,24,11,12,13]
# I = J[:]
# I.extend([21,28])
# N = [0,-1,-2,-3,-4,4,12,20,24,25,26,27,28]

# aIncrement = 5
# lIncrement = 5
# eIncrement = 5
# kIncrement = 5
# hIncrement = 5
# jIncrement = 6
# iIncrement = 6
# nIncrement = 6

##########
# If you want to generate some different patterns then this, then the folder components is for you. :D
###########

arrA = [-3, -2, -1, 0, 3, 5, 10, 12, 18, 19, 20, 21]
incrementA = 5
arrB = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 18, 19, 20]
incrementB = 5
arrC = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 21]
incrementC = 5
arrD = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 18, 19, 20]
incrementD = 5
arrE = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 21]
incrementE = 5
arrF = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 17]
incrementF = 5
arrG = [-4, -3, -2, -1, 0, 3, 7, 10, 12, 14, 17, 19, 21, 24, 26, 27, 28]
incrementG = 6
arrH = [-4, -3, -2, -1, 0, 5, 12, 17, 18, 19, 20, 21]
incrementH = 5
arrI = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 21, 24, 28]
incrementI = 6
arrJ = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 24]
incrementJ = 6
arrK = [-4, -3, -2, -1, 0, 5, 11, 13, 17, 21]
incrementK = 5
arrL = [-4, -3, -2, -1, 0, 7, 14, 21]
incrementL = 5
arrM = [-4, -3, -2, -1, 0, 4, 12, 18, 24, 25, 26, 27, 28]
incrementM = 6
arrN = [-4, -3, -2, -1, 0, 4, 12, 20, 24, 25, 26, 27, 28]
incrementN = 6
arrO = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 18, 19, 20, 21]
incrementO = 5
arrP = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 18]
incrementP = 5
arrQ = [-4, -3, -2, -1, 0, 3, 7, 10, 13, 14, 17, 21, 24, 25, 26, 27, 28, 35]
incrementQ = 7
arrR = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 13, 18, 21]
incrementR = 5
arrS = [-4, -3, -2, 0, 3, 5, 7, 10, 12, 14, 17, 19, 20, 21]
incrementS = 5
arrT = [-4, 3, 10, 11, 12, 13, 14, 17, 24]
incrementT = 6
arrU = [-4, -3, -2, -1, 0, 7, 14, 17, 18, 19, 20, 21]
incrementU = 5
arrV = [-4, -3, -2, 6, 14, 20, 24, 25, 26]
incrementV = 6
arrW = [-4, -3, -2, -1, 0, 6, 12, 20, 24, 25, 26, 27, 28]
incrementW = 6
arrX = [-4, 0, 4, 6, 12, 18, 20, 24, 28]
incrementX = 6
arrY = [-4, 4, 12, 13, 14, 18, 24]
incrementY = 6
arrZ = [-4, 0, 3, 6, 7, 10, 12, 14, 17, 18, 21, 24, 28]
incrementZ = 6

### And the numbers
arr1 = [4, 7, 10, 11, 12, 13, 14, 21]
increment1 = 5
arr2 = [-4, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 18, 19, 21]
increment2 = 5
arr3 = [-4, -2, 0, 3, 5, 7, 10, 12, 14, 17, 18, 19, 20, 21]
increment3 = 5
arr4 = [-4, -3, -2, 5, 12, 17, 18, 19, 20, 21]
increment4 = 5
arr5 = [-4, -3, -2, 0, 3, 5, 7, 10, 12, 14, 17, 19, 20, 21]
increment5 = 5
arr6 = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 19, 20, 21]
increment6 = 5
arr7  = [-4, 0, 3, 6, 10, 12, 17, 18, 24]
increment7  = 6
arr8 = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 18, 19, 20, 21]
increment8 = 5
arr9 = [-4, -3, -2, 0, 3, 5, 7, 10, 12, 14, 17, 18, 19, 20, 21]
increment9 = 5


user = raw_input("Enter the github username:- ")
email = raw_input("Enter the registered github email id:- ")
print "Now you need to enter the date from which you want to start writing your name"
time.sleep(2)
print "For more details or to know how to find date, refer README.md"
time.sleep(2)
year = int(raw_input("Enter the year:- "))
mon = int(raw_input("Enter the month:- "))
day = int(raw_input("Enter the day:- "))
name=raw_input("Enter the name (currently supports only name and space):- ")
num = int(raw_input("How many commits do you want..:- "))
startingDate = datetime.datetime(year, mon, day)

for word in name:
	if word.isdigit():
		text = "arr" + str(word)
	else:
		text = "arr" + word.upper()

	if text != ' ':
		increment = eval('increment' + word)
		print word
		myArray = eval(text)
		for i in myArray:
			first = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			second = 'git add .'
			third = 'git commit -m "blah blah" --amend --author="' + user + ' <' +email + '> " --date="' + (startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y") + '"'

			final = first + '; ' + second + '; ' + third + '; git push origin master --force'
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(num) + '`;do ' +  final+ '; done' + '\n')
		startingDate = startingDate + datetime.timedelta(days=increment*7)
	else:
		startingDate = startingDate + datetime.timedelta(days=1)
print "Go and execute the file runThis.sh in your repository"