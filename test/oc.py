import re
f = open("concepts+soundex.txt", "r").readlines()
t = open("response2.txt", "r").readlines()
z = open("new2.txt", "w")
for line2 in t:
    line2 = line2.strip()
    for line1 in f:
        line1 = line1.strip()
        l = line1.split('\t')[1]
        #print(l)
        if line2 in l:
            #print (line1)
            z.write(line1 + "\n")

z.close()


# for line2 in t:
#     for line1 in f:
#         if line2 in line1:
#             z.write(line1)
