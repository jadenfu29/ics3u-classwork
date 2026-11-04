word = input()
for i in range(len(word)-2):
    if [word[i],word[i+1],word[i+2]] == ["x","y","z"] and (i==0 or word[i-1]!="."):
        print(True)
        break
else:
    print(False)