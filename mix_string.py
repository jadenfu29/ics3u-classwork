a,b = input(),input()
final = ""
for i in range(max(len(a),len(b))):
    if i<len(a):
        final+=a[i]
    if i<len(b):
            final+=b[i]
print(final)