########################################################
#
# CMPSC 441: Homework 1
#
########################################################


########################################################
# 0. Your name and email address
########################################################

student_name = 'John Nguyen'
student_email = 'jnn5163@psu.edu'





########################################################
### 1. Sequences
########################################################

def list_add(l1, l2):
    newList = []
    for item1 in l1:
        for item2 in l2:
            if item1 not in newList:
                newList.append(item1)
            if item2 not in newList:
                newList.append(item2)
    return newList

def dict_extend(dict1, dict2):
    newDict = {}
    for key, value in dict1.items():
        newDict[key]=[value]

    for key, value in dict2.items():
        if key in newDict:
            newDict[key].append(value)
        else:
            newDict[key]=[value]
    
    return newDict

def dict_invert(dct):
    newDict={}
    for key, value in dct.items():
        if value in newDict:
            newDict[value].append(key)
        else:
            newDict[value]=[key]

    return newDict        

def dict_nested(lst):
    if len(lst)==0:
        return {}
    
    newLst = lst[1:len(lst)]
    return {lst[0]:dict_nested(newLst)}

     
########################################################
### 2. List Comprehension
########################################################


def list_product(l1, l2):
    return [[x,y] for x in l1 for y in l2]

def list_flatten(list_of_seqs):
    return [x[y] for x in list_of_seqs for y in range(len(x))]

def dict_to_table(dct):
    return [(tuple(dct.keys()))] + [tuple(dct[x][i] for x in dct) for i in range(len(next(iter(dct.values()))))]

def nlargest(dct, n):
    return []

def unique_values(list_of_dicts):
    return []


########################################################
### 3. Other algorithms
########################################################

def encode(input):
    if len(input)==0:
        return ""
    elif len(input)==1:
        return "1"+input
    
    newString=""
    letterCount=1
    for i in range(1,len(input)):
        if input[i]==input[i-1]:
            letterCount+=1
        elif input[i]!=input[i-1]:
            newString+=str(letterCount)+input[i-1]
            letterCount=1

        if i==len(input)-1:
            newString+=str(letterCount)+input[i]

    return newString

def decode(input):
    newString=""
    for i in range(len(input)):
        if i%2==0:
            for j in range(int(input[i])):
                newString+=input[i+1]
    return newString

def camel_case(var_name):
    wordLst = var_name.lower().split("_")
    for i in range(1,len(wordLst)):
        wordLst[i] = wordLst[i].capitalize()

    newString=""
    for word in wordLst:
        newString+=word

    return newString

        


########################################################
### 4. Fraction class
########################################################


class Fraction():
    def __init__(self, numerator, denominator=1):
        self.num = numerator
        self.den = denominator
        try:
            numerator/=denominator
        except:
            raise ZeroDivisionError(str(numerator)+"/"+str(denominator))
        

    def get_fraction(self):
        return (self.num,self.den)

    def __neg__(self):
        return Fraction(-self.num, self.den)
       
    def __add__(self, other):
        if self.den == other.den:
            return Fraction(self.num+other.num, self.den)
        
        newDen = self.den*other.den
        return Fraction(self.num*other.den + self.den*other.num, newDen)

    def __sub__(self, other):
        if self.den == other.den:
            return Fraction(self.num-other.num, self.den)
        
        newDen = self.den*other.den
        return Fraction(self.num*other.den - self.den*other.num, newDen)

    def __mul__(self, other):
        return Fraction(self.num*other.num, self.den*other.den)

    def __truediv__(self, other):
        return Fraction(self.num*other.den, self.den*other.num)
        
    def __eq__(self, other):
        if self.num*other.den==other.num*self.den:
            return True
        return False

    def __lt__(self, other):
        if self.num*other.den<other.num*self.den:
            return True
        return False
    
    def __call__(self):
        return self.num/self.den

    def simplify(self):
        n=10
        while n>1:
            if self.num%n==0 and self.den%n==0:
                self.num/=n
                self.den/=n
                print(self.num)
            else:
                n-=1

        #get proper sign
        if self.num*self.den>0:
            self.num = abs(self.num)
            self.den = abs(self.den)
        
    def __str__(self):
        return str(self.num)+'/'+str(self.den)

#DELETE AFTER
if __name__=="__main__":
    # print(nlargest({'item1':45.50,'item2':35, 'item': 41.30, 'item4':55},3))

    f, g, h = Fraction(2,6), Fraction(2,3), Fraction(0, 5)
    k = f * f
    print(k.get_fraction())
    k = f * g
    print(k.get_fraction())
    k = f / f
    print(k.get_fraction())
    k = f / g
    print(k.get_fraction())
    k = f / h
    print(k.get_fraction())
    