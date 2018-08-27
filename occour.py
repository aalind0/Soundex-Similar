f1 = open("b1.txt")
f2 = open("response2.txt", "w")

file1lines = f1.readlines()
if len(file1lines) != 0 :
    uniquewords = set(word for line in file1lines for word in line.split(" "))
    wordlist = list(word for line in file1lines for word in line.split(" "))
    for words in uniquewords:
        f2.write(str(words.rstrip("\n")) + " : " + str(wordlist.count(words)) + " occurence" + "\n")

f2.close()
f1.close()
