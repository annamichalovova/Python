def double_string(s):
    nejdelsi=0
    delka=(len(s))
    for i in range(1,delka+1):
        for k in range(i,delka+1):
            if len(s[i-1:k]) > 1 and len(s[i-1:k]) > nejdelsi and s.count(s[i-1:k]) > 1:
                nejdelsi = len(s[i-1:k])
            #print("substring:", s[i-1:k], " ,pocet opakovani:", s.count(s[i-1:k])," ,delka substringu:", len(s[i-1:k]))
        #print("---")
    return nejdelsi


s=input("Zadejte retezec: ")
print(double_string(s))


