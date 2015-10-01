def  poly10_2D(c,data,y=None):

    if (y is None):
        x=data[0,:]
        y=data[1,:]
    else:
        x=data

    F = c[0]+c[1]*x+c[2]*y+c[3]*x*x+c[4]*x*y+c[5]*y*y \
        +c[6]*x**3+c[7]*x**2*y+c[8]*x*y**2+c[9]*y**3 \
        +c[10]*x**4+c[11]*x**3*y+c[12]*x**2*y**2+c[13]*x*y**3+c[14]*y**4 \
        +c[15]*x**5+c[16]*x**4*y+c[17]*x**3*y**2+c[18]*x**2*y**3+c[19]*x*y**4+c[20]*y**5 \
        +c[21]*x**6+c[22]*x**5*y+c[23]*x**4*y**2+c[24]*x**3*y**3+c[25]*x**2*y**4+c[26]*x*y**5+c[27]*y**6 \
        +c[28]*x**7+c[29]*x**6*y+c[30]*x**5*y**2+c[31]*x**4*y**3+c[32]*x**3*y**4+c[33]*x**2*y**5+c[34]*x*y**6+c[35]*y**7 \
        +c[36]*x**8+c[37]*x**7*y+c[38]*x**6*y**2+c[39]*x**5*y**3+c[40]*x**4*y**4+c[41]*x**3*y**5+c[42]*x**2*y**6+c[43]*x*y**7+c[44]*y**8 \
        +c[45]*x**9+c[46]*x**8*y+c[47]*x**7*y**2+c[48]*x**6*y**3+c[49]*x**5*y**4+c[50]*x**4*y**5+c[51]*x**3*y**6+c[52]*x**2*y**7+c[53]*x*y**8+c[54]*y**9 \
        +c[55]*x**10+c[56]*x**9*y+c[57]*x**8*y**2+c[58]*x**7*y**3+c[59]*x**6*y**4+c[60]*x**5*y**5+c[61]*x**4*y**6+c[62]*x**3*y**7+c[63]*x**2*y**8+c[64]*x*y**9+c[65]*y**10

    return F

