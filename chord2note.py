def chord2note(name,Mmad,sharpflat):
    ChordName = {}
    ChordName['name'] = name
    ChordName['sharpflat'] = sharpflat
    ChordName['Mmad'] = Mmad

    num1st = 0
    num2nd = 0
    num3rd = 0

    if ChordName['name'] == 'C':
        num1st = 1
    elif ChordName['name'] == 'D':
        num1st = 3 
    elif ChordName['name'] == 'E':
        num1st = 5
    elif ChordName['name'] =='F':
        num1st = 6
    elif ChordName['name'] =='G':
        num1st = 8
    elif ChordName['name'] =='A':
        num1st = 10
    elif ChordName['name'] =='B':
        num1st = 12
    
    if ChordName['Mmad'] == 'M':
        num2nd = num1st+4
        if num2nd>12:
            num2nd = num2nd-12
        num3rd = num1st+7
        if num3rd>12:
            num3rd = num3rd-12    
    elif ChordName['Mmad'] == 'm':
        num2nd = num1st+3
        if num2nd>12:
            num2nd = num2nd-12
        num3rd = num1st+7
        if num3rd>12:
            num3rd = num3rd-12
            
    if ChordName['sharpflat'] == 'b':
        num1st -= 1
        num2nd -= 1
        num3rd -= 1
    elif ChordName['sharpflat'] == '#':
        num1st += 1
        num2nd += 1
        num3rd += 1

    def num2note(a):
        if a==0:
            a='si'
        if a==1:
            a='do'
        if a==2:
            a='#do'
        elif a==3:
            a='re'
        elif a==4:
            a='#re'
        elif a==5:
            a='mi'
        elif a==6:
            a='fa'
        elif a==7:
            a='#fa'
        elif a==8:
            a='sol'
        elif a==9:
            a='#sol'
        elif a==10:
            a='la'
        elif a==11:
            a='#la'
        elif a==12:
            a='si'
        return a

    note=[num2note(num1st),num2note(num2nd),num2note(num3rd)]
    print(note)
    
    return note

