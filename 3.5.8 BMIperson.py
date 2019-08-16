def ftintom(ft, inch):
    return ft*0.3048 + inch*0.0254

#print(ftintom(6,4))

def lbstokg(lb):
    return lb*0.45359237

def BMI(weight,height):
    if height<1.0 or height>2.5 or \
       weight<20 or weight>200:
        return None
    return weight/height**2

print(BMI(weight=ftintom(5,7), height=lbstokg(176)))
