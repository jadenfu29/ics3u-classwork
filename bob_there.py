word = input()
for i in range(len(word)-2):
    if [word[i],word[i+2]] == ["b","b"]:
        print(True)
        break
else:
    print(False)