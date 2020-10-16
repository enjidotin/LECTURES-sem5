# Name: Naman Garg 
# Roll No: B032
# AIM: Implementation of String Matching Algorithm - Rabin Karp algorithm

from math import *
s=input("Enter string : ").upper()                                                                          #s,pat => String and the pattern to match
pat=input("Enter pattern : ").upper()
prime=int(input("Enter prime number : "))                                                                   #prime => Prime number of the hashing function

hash_pat=int(sum([(ord(ch)-64)*pow(prime,i) for i,ch in enumerate(pat)]))                                   #hash_pat => Hash value of pattern
print(f"Hash value of pattern : {hash_pat}")

match_index=[]                                                                                      #match_index => Stores the index where match is found

pat_len=len(pat)
s_len=len(s)
hash_s=0

for i in range(0,s_len-pat_len+1):

    comp=1

    if(i==0):
        hash_s = int(sum([(ord(ch) - 64) * pow(prime, i) for i, ch in enumerate(s[i:i+pat_len])]))          # First time assigning hash value
        print(f"Current substring : {s[i:i + pat_len]} => Hash value of substring = {hash_s} => ", end="")
    else:
        hash_s = int((hash_s-(ord(s[i-1])-64))/prime) +int((ord(s[i+pat_len-1])-64)*pow(prime,pat_len-1))   # Rolling hash function
        print(f"Current substring : {s[i:i + pat_len]} => Hash value of substring = {hash_s} => ", end="")

    if(hash_s==hash_pat):
        print("Hash values matched! => Character comparison => ",end="")                       # If hash values match then check for character comparisons
        flag=0
        for j in range(i,i+pat_len):
            comp+=1

            if s[j]!=pat[j-i]:
               flag=1
               break
        if(flag==0):
            print(f"Match => Comparisons : {comp}")
            match_index.append(f"Index {i} till {i + pat_len - 1}")
        else:
            print(f"Not a match => Comparisons : {comp}")

    else:
        print(f"Not a match => Comparisons : {comp}")

if(match_index):
    print(f"\nPattern matched at => {', '.join(match_index)}")
else:
    print("The pattern doesnt exist in the string")