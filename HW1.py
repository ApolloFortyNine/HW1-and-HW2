#HW1 #1
#Due Date: 06/01/2018, 11:59PM EST
# - First, read the file "HW1.pdf" posted on CANVAS 
# - Then, try to understand what the provided code is doing
# - Finally, complete the four functions according to the instructions
### Use the Python debugger and the unittest module to assit you to achieve the goal of the assigment 
##*************************************
#Name: Ethan Tabler

def findNextOpr(txt):
    #txt must be a nonempty string. 
    if len(txt)<=0 or not isinstance(txt,str):
        print("type error: findNextOpr")
        return "type error: findNextOpr"
    #In this exercise +, -, *, / are all the 4 operators
    #The function returns -1 if there is no operator in txt,
    #otherwise returns the position of the leftmost operator
    #--- continue the rest of the code here ----#
    for i in range(len(txt)):
        if txt[i] == "+" or txt[i] == "-" or txt[i] == "*" or txt[i] == "/":
            #if txt[i+1] == "+" or txt[i+1] == "-" or txt[i+1] == "*" or txt[i+1] == "/":
            #    print("type error: extra operators")
            #    return None, None, "type error: extra operators"
            return i
        else:
            continue
    if "+" not in txt or "-" not in txt or "*" not in txt or "/" not in txt:
        return -1

    #--- function code ends -----#


def isNumber(txt):
    #txt must be a non-empty string
    #returns True if txt is convertible to float, else False
    if len(txt)==0 or not isinstance(txt, str):
        print("type error: isNumber")
        return "type error: isNumber"
    #--- continue the rest of the code here ---#
    txt.strip("-")
    try:
        txt = float(txt)
        return True
    except:
        return False
    #--- function code ends ---#

def getNextNumber(expr, pos):
    #expr is a given arithmetic formula of type string
    #pos = start position in expr
    #1st returned value = the next number (None if N/A)
    #2nd returned value = the next operator (None if N/A)
    #3rd returned value = the next operator position (None if N/A)
    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        print("type error: getNextNumber")
        return None, None, "type error: getNextNumber"
    #--- continue the rest of the code here ---#
    #1st val
    num = ""
    numbers = set(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", " "))
    operators = set(("+", "-", "*", "/"))
    for character in range(len(expr[pos:])):
        if expr[character+pos] in numbers:
            num = num + expr[character+pos]
        elif expr[character+pos] in operators:
            if expr[character+1+pos] in operators:
                print("type error: extra operators")
                return None, None, "type error: extra operators"
            break
        
    
    #3rd val
    nextOprPos = findNextOpr(expr[pos:])+pos
    #2nd val
    opr = None
    if nextOprPos != -1:
        for index in range(len(expr[pos:])):
            if expr[index+pos] == "+":
                opr = "+"
                break
            elif expr[index+pos] == "-":
                opr = "-"
                break
            elif expr[index+pos] == "*":
                opr = "*"
                break
            elif expr[index+pos] == "/":
                opr = "/"
                break
            else:
                continue

        
    ### Return all values ###
    if isNumber(num):
        return float(num), opr, nextOprPos
    else:
        return "type error: isNumber"

 
    #--- function code ends ---#
    

def exeOpr(num1, opr, num2):
    #This funtion is just an utility function. It is skipping type check
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        return num1/num2
    else:
        return None

    
def calculator(expr):
    #expr: nonempty string that is an arithmetic expression
    #the fuction returns the calculated result

    if len(expr)<=0 or not isinstance(expr,str):
        print("input error: line A in calculator")        #Line A
        return "input error: line A in calculator"
    
    #Hold two modes for operator precedence: "addition" and "multiplication"
    #Initialization: get the first number

    ## Think why the next 6 lines are necessary... 
    ## Is there another way to achieve the same result? 
    expr = expr.strip()
    if expr[0]!="-":
        newNumber, newOpr, oprPos = getNextNumber(expr, 0)
    else:
        newNumber, newOpr, oprPos = getNextNumber(expr, 1)
        newNumber *= -1
    #####


    if newNumber is None:
        print("input error: line B in calculator")   #Line B
        return "input error: line B in calculator"
    elif newOpr is None:
        return newNumber
    elif newOpr=="+" or newOpr=="-":
        mode="add"
        addResult=newNumber     #value so far in the addition mode
        mulResult=None          #value so far in the mulplication mode
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber
    pos=oprPos+1                #the new current position
    opr=newOpr                  #the new current operator
    addOpr = None               #setup for later addition/subtraction
    
    #Calculation starts here. 
    #Use the above completed functions effectively!
    while True:
        #--- continue the rest of the while loop code here ---#
        
        newNumber, newOpr, oprPos = getNextNumber(expr, pos)    #get next values
        
        if newOpr == "*" or newOpr == "/":
            nextMode = "mul"
        elif newOpr == "+" or newOpr == "-":
            nextMode = "add"
        else:
            nextMode = None
        ##############################################################################
        if nextMode == None:
            if mode == "add":
                return exeOpr(float(addResult), opr, float(newNumber))
            elif mode == "mul":
                mulResult = exeOpr(float(mulResult), opr, float(newNumber))
                if addOpr != None:
                    return exeOpr(float(addResult), addOpr, float(mulResult))
                return mulResult
        ###############################################################################
        elif mode == "mul" and nextMode == "add":
            mulResult = exeOpr(float(mulResult), opr, float(newNumber))
            if addOpr != None:
                addResult = exeOpr(float(mulResult), addOpr, float(addResult))
                mulResult = None
            addOpr = None
        ###############################################################################
        elif mode == "add" and nextMode == "mul":
            if mulResult != None:
                addResult = exeOpr(float(mulResult), opr, float(addResult))
            mulResult = newNumber
            addOpr = opr
        ###############################################################################
        elif mode == "add" and nextMode == "add":
            addResult = exeOpr(float(addResult), opr, float(newNumber))
            
        elif mode == "mul" and nextMode == "mul":
            mulResult = exeOpr(float(mulResult), opr, float(newNumber))
           
        pos=oprPos+1                #the new current position
        opr=newOpr                  #the new current operator
        mode=nextMode
        #
        #--- end of function ---#
