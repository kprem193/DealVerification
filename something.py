
from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
answer=0
def convert(text):
  check = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety","hundred", "thousand", "million", "billion", "trillion"
      ]

  #text="seven hundred twenty three euro twenty three cent"

  a=text.split(" ")
  f1=0
  j=1

  if(a[-1]=="cent" or a[-1]=="cents"):
    f1=1
    text=text[:len(text)-(len(a[-1])+1)]
    for i in check:
      if(i==a[-3]):
        j=2
        breakprint(final)

    if(j==2):
      print(final)
      text1=a[-3]+" "+a[-2]
      text=text[:len(text)-(len(a[-2])+len(a[-3])+1)]
    if(j==1):
      text1=a[-2]
      text=text[:len(text)-(len(a[-2])+1)]
    text=text[:len(text)-1]
  a=text.split(" ")
  f=0
  for i in check:
    if(i==a[-1]):
      f=1

  if(f!=1):
    text=text[:len(text)-(len(a[-1])+1)]
    if(a[-1]=="dollar" or a[-1]=="dollars"):
      currency="$"
    if(a[-1]=="euro" or a[-1]=="euros"):
      currency = u"\u20ac"
    if(a[-1]=="pound" or a[-1]=="pounds"):
      currency=u"\u00A3"
  if(f==1):
    final=str(text2int(text))
    answer=float(final)
    print(final)
  elif(f1!=1):
    temp_final=str(text2int(text))
    final= temp_final+currency
    answer=float(temp_final)
    print(final)
    
  else:
    temp_final=str(text2int(text))+"."+str(text2int(text1))
    final= temp_final+currency
    answer=float(temp_final)
    print(final)
  if(answer>=50000):
  	print('----------------------------LARGE DEAL----------------------------')
  else:
  	print('----------------------------SMALL DEAL----------------------------')
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


nlp = spacy.load('/var/www/html/LargeDeal/prem') 
output_dir='/var/www/html/LargeDeal/prem'
with open('/var/www/html/LargeDeal/uploads/spacy.txt', 'r') as myfile:
	data=myfile.read().replace('\n', '')
doc = nlp(data)
print("\n\nCall: '%s'\n" % data)
nlp2 = spacy.load(output_dir)
doc2 = nlp2(data)
for ent in doc2.ents:
    if(ent.label_!='saccountfrom' and ent.label_!='saccountto'):
        print(ent.label_,ent.text)
    elif(ent.label_=='amount' ):
        (convert(ent.text))
    else:
        if(ent.label_=='saccountfrom'):
#            ent.label_='sfundfrom'
            print('sfundfrom',ent.text)
        if(ent.label_=='saccountto'):
 #           ent.label_='sfundto'
             print('sfundto',ent.text)
