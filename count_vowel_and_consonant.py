text=input("enter string: ")
count_vowel=0
count_consonant=0
for char in text:
    if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
        count_vowel+=1
    elif (char>='a'and char<='z'):
        count_consonant+=1
print(f"total vowel: {count_vowel}")
print(f"total consonant: {count_consonant}")    

    
