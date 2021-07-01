file = open("username.txt", "r")

fileArray = file.readlines()
fileArrayWithNoSpace = []

for x in fileArray:
  x = x.strip().lower()
  x = x.replace(" ","")
  fileArrayWithNoSpace.append(x)

write = open("fullname.txt", 'a')

for x in range(len(fileArray)):
  write.write(fileArray[x].replace("\n","") + " " + fileArrayWithNoSpace[x] + '@maltepe.edu.mail.tr\n')


