def note2chord(note0,note1,note2):
    def note2num(a):
        for i in range(11):
            notename=['do','#do','re','#re','mi','fa','#fa','sol','#sol','la','#la','si']
            if notename[i] == a:
                break
        return i
    
    num1st = note2num(note0)
    num2nd = note2num(note1)
    num3rd = note2num(note2)
    
    def num2chord(a,b,c):
        if b-a == 3:
            Mmad = 'm'
        elif b-a == 4:
            Mmad = 'M'
        chordname=['C','#C','D','#D','E','F','#F','G','#G','A','#A','B']
        sharpflat = ''
        if '#' in chordname[a]:
            sharpflat = '#'
        name = chordname[a]
        chord = [sharpflat,name,Mmad]
        
        return chord
    
    chord = num2chord(num1st,num2nd,num3rd)
    chord = chord[0]+chord[1]+chord[2]
    print(chord)
    
    return chord

