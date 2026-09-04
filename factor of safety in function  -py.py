A short script that calculates the Factor of Safety (FoS), a fundamental mechanical design concept.
c_fos(u, w) computes FoS as ultimate strength ÷ working stress.
Concepts used: functions, return values.

code:
    
def c_fos(u,w):
    return u/w

a=c_fos(500,100)
print('factor of safety =',a)
