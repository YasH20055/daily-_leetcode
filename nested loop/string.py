s = "DOG"

for i in range(len(s)):
    print(i, s[i])

    # for printing the index and character at that index in the string 
    s = "PYTHON"

for i in range(len(s)):
    if s[i] == "T":
        print("the given charecter is present at ",i,"index")

        #for in banana we  are checking the reapeating a and printing the index of a
        s="BANANA"
c=0
for i in range (len(s)):
    if s[i] =="A":
        c=i
        print(c)
    

    #for print after first char is found in the string
    s="BANANA"

for i in range (len(s)):
    if s[i] =="A":
        break

print(i)
  