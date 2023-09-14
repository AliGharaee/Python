hrs = input('Enter Hours:')
hpr = input('Enter Rate:')
h = float(hrs)
hpr = float(hpr)
if h <=40:
    r = h*hpr
    print(r)
else :
    ot = h-40
    extra = ot*(hpr*1.5)
    base = 40 * hpr
    gp = extra+base
    print(gp)
