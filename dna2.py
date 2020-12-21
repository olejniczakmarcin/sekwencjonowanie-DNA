import random
import difflib
import os
def find_first(listt):
    max=0
    index=0
    for i in range(len(listt)):
        if(listt[i][1]==0):
            if(max<listt[i][2]):
                max=listt[i][2]
                index=i
    return index
def lengg(a):
    return len(a)
def sort_b(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
DNALettersDict = {0: "A", 1: "T", 2: "C", 3: "G"}
#===============================================================================================
#Generate DNA sequence for the test
#===============================================================================================
OriginalDNALength = 1000
OriginalDNASeq = [DNALettersDict[random.randint(0, 3)] for i in range(OriginalDNALength)]
#print(OriginalDNASeq)
#===============================================================================================
#Generate Fragments
#===============================================================================================
NumberOfFragments = 2000
MinLength = 40
MaxLength = 90
tt=True
def SelFragment(DNASeq):
  startPos = random.randint(0, OriginalDNALength-1-MinLength)
  global tt
  if tt==True:
      startPos=0
      tt=False
  length = random.randint(MinLength, MaxLength)
  return [DNASeq[startPos:startPos+length],startPos,length]
ListOfFragments = [ SelFragment(OriginalDNASeq) for i in range(NumberOfFragments)]
#===============================================================================================
#Reconstruct DNA from fragments
#===============================================================================================
i=0
leng1=len(ListOfFragments)
while(i<leng1 and i!=leng1):
    j=0
    while(j<leng1 and i!=j):
        if(i<leng1 and ListOfFragments[i][1]==ListOfFragments[j][1] and ListOfFragments[i][2]==ListOfFragments[j][2]):
            ListOfFragments.remove(ListOfFragments[i])
            leng1-=1
        j+=1
    i+=1
i=0
leng1=len(ListOfFragments)
while(i<leng1 and i!=leng1):
    j=0
    while(j<leng1 and i!=j):
        if(i<leng1 and ListOfFragments[i][1]==ListOfFragments[j][1]):
            if(len(ListOfFragments[i][0])>=len(ListOfFragments[j][0])):
                ListOfFragments.remove(ListOfFragments[j])
                leng1-=1
            else:
                ListOfFragments.remove(ListOfFragments[i])
                leng1-=1
        j+=1
    i+=1
first=find_first(ListOfFragments)
first_el=ListOfFragments[first][0]
ListOfFragments.remove(ListOfFragments[first])
ListOfFragments1=ListOfFragments.copy()
len2=len(ListOfFragments1)
s=sort_b(ListOfFragments1)
ListOfFragments1=s
new_list={}
while(len2>0):
    output_list = [li for li in difflib.ndiff(first_el, ListOfFragments1[0][0])  if li[0] != '-']
    for i in range(len(output_list)):
        output_list[i]=output_list[i].replace(' ','')
    new_list = [i for i in output_list if not i.isalnum()]
    for i in range(len(new_list)):
        new_list[i]=new_list[i].replace('+','')
        first_el.insert(lengg(first_el),new_list[i])
    ListOfFragments1.remove(ListOfFragments1[0])
    len2-=1
if OriginalDNASeq==first_el:
    print("ilosc elemntow w liscie ListOfFragments ")
    print(len(ListOfFragments1),'\n')
    print("THE SAME\n")
    print(first_el)
    if os.path.exists('dna.txt'):
        os.remove('dna.txt')
    f=open('dna.txt','a+')
    for i in range(len(first_el)):
        f.write(first_el[i])
        f.write(' ')
        if(i!=0 and i%30==0):
            f.write('\n')
    f.close()
else:
    print('Not the same')