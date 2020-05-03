# main python program 

response=['Welcome to smart calculator','My name is JARVIS', 
          'Thank You!!','Sorry ,this is  beyond my ability.Kindly try something else.'] 
  
# fetching tokens from the text command 
def extract_from_text(text): 
    l=[] 
    for t in text.split(' '): 
        try: 
            l.append(float(t)) 
        except ValueError: 
            pass
    return l 
  
# calculating LCM 
def lcm(a,b): 
    L=a if a>b else b 
    while L<=a*b: 
        if L%a==0 and L%b==0: 
            return L 
        L+=1
  
# calculating HCF 
def hcf(a,b): 
    H=a if a<b else b 
    while H>=1: 
        if a%H==0 and b%H==0: 
            return H 
        H-=1
# Addition 
def add(a,b): 
    return a+b 

# Subtraction 
def sub(a,b): 
    return a-b


# Power Calculation   
def power(a,b):
    if(b==1):
        return(a)
    if(b!=1):
        return(a*power(a,b-1))


# Factorial
def factorial(n):
    if n == 1:
        return n
    if n== 0:
        return 1
    if n<0:
        return 0
    else:
        return n*factorial(n-1)

# Difference 
def dif(a,b): 
    if a>b:
        return a-b
    else:
        return b-a
    
# Multiplication 
def mul(a,b): 
    return a*b 
  
# Division 
def div(a,b):
    if a>b:
        return a/b 
    else:
        return b/a
  
# Remainder 
def mod(a,b): 
    return a%b 
  
# Response to command 
# printing - "Thank you" on exit 
def end(): 
    print(response[2]) 
    input('press enter key to exit') 
    exit() 
#A funtion to print a message that handles the exception
def sorry(): 
    print(response[3]) 
   
# Operations - performed on the basis of text tokens 
operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add, 
            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub, 
            'DIFFERENCE':dif,'LCM':lcm,'HCF':hcf, 
            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul, 
            'DIVISION':div,'DIVIDES':div,'MOD':mod,'REMAINDER'
            :mod,'MODULAS':mod,'FACTORIAL':factorial,'POWER':power} 
  
# commands 
commands={'EXIT':end,'END':end,'CLOSE':end} 
           
print('--------------'+response[0]+'------------') 
print('------------------'+response[1]+'--------------------') 
   
    
flag=0   
while True: 
    print() 
    text=input('enter your queries:  ') 
    for word in text.split(' '): 
        if word.upper() in operations.keys(): 
            try: 
                l = extract_from_text(text) 
                if len(l)==2:
                    r = operations[word.upper()] (l[0],l[1])
                else:
                    r = operations[word.upper()] (l[0])
                print(r) 
            except: 
                pass
            finally:
                 break
        elif word.upper() in commands.keys():
            flag=1
            break
    else:
        sorry() 
    if flag==1:
        print(response[2]) 
        break
    
