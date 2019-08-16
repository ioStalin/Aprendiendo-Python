def ftintom(ft, inch):
    return ft*0.3048 + inch*0.0254

print(ftintom(6,4))

def ftintom1(ft, inch=0.0):
    return ft*0.3048+inch*0.0254

print(ftintom1(6))
