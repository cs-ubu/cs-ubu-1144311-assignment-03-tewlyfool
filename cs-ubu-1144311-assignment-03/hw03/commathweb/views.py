from django.shortcuts import render
def dto32(d):
    fin = d
    i = bin(int(fin))[2:]
    f = fin - int(fin)
    ft = ''
    while f> 0:
        f = f*2
        ft = ft+str(int(f))
        f -= int(f)
    e = 127+len(i)-1
    ex = bin(e)[2:]
    m = i[1:]+ft
    s = '0' if fin>=0 else '1'
    m = (m+((23-len(m))*'0'))[:23]
    return s+ex+m
def dto64(d):
    fin = d
    i = bin(int(fin))[2:]
    f = fin - int(fin)
    ft = ''
    while f> 0:
        f = f*2
        ft = ft+str(int(f))
        f -= int(f)
    e = 2047+len(i)-1
    ex = bin(e)[2:]
    m = i[1:]+ft
    s = '0' if fin>=0 else '1'
    m = (m+((52-len(m))*'0'))[:52]
    return s+ex+m

# Create your views here.
# Assignment 03

# # สร้างเว็บเพื่อให้ผู้ใช้สามารถเรียกใช้ฟังก์ชันต่อไปนี้ผ่านเว็บได้

# * แปลงเลขทศนิยมเป็น IEEE floating point single precision (32-bit)

# ```python
# def decto32fp(d):
# 	pass
# ```
def dectofp(req):
    if req.method == 'POST':
        rp = req.POST
        try:
            d = float(rp['d']) 
        except:
            d=0
        s = rp['s']
        if s=='86x':
            return render(req,'show.html',{'l':dto32(d)})
        elif s=='64x':
            return render(req,'show.html',{'l':dto64(d)})
    else :
        return render(req,'show.html',{})
# * แปลงเลขทศนิยมเป็น IEEE floating point double precision (64-bit)

# ```python
# def decto32fp(d):
# 	pass
# ```

def home(req):
    return render(req,'home.html',{})

# * แก้ระบบสมการเชิงเส้น $Ax = b$

# ```python
# def solve(A, b):
# 	pass
# ```
def solvej(A, b):
    try:
        import numpy as np
        a,b = np.array(A) , np.array(b)
        n = len(a[0])
        # eliminate
        for k in range(0, n-1):
            for i in range(k+1, n):
                if a[i,k] != 0.0:
                    lam = a[i,k]/a[k,k]
                    a[i,k:n] = a[i, k:n] - lam*a[k,k:n]
                    b[i] = b[i] - lam*b[k]
        x = np.array([0]*n)
        # Back Substitution 
        for k in range(n-1, -1, -1):
            x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
        return x.flatten()
    except:
        return ['ไม่สามารถหาคำตอบได้']
def readA(xi,rm):
    A = []
    for i in range(xi):
        t =[]
        for j in range(xi):
            try:
                if rm['U'+str(i)+str(j)]==None:t.append(0)
                elif rm['U'+str(i)+str(j)]=='':t.append(0)
                else: t.append(float(rm['U'+str(i)+str(j)])) 
            except:t.append(0)
        A.append(t)
    return A
def readb(xi,rm):
    b=[]
    for i in range(xi):
        try:    
            if rm['c'+str(i)]==None:b.append(0)
            elif rm['c'+str(i)]=='':b.append(0)
            else :b.append(float(rm['c'+str(i)])) 
        except: b.append(0)
    return b
def solve(req):
    if req.method == 'POST':
        rp=req.POST
        try:xi = int(rp['xi'])
        except:xi=0  
        A = readA(xi,rp)
        b = readb(xi,rp)
        return render(req,'solve.html',{'l':solvej(A,b),'x':range(xi)})
    else:
        return render(req,'solve.html',{})
