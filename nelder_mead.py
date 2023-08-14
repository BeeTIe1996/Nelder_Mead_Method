#!/usr/bin/python
# -*- coding: utf-8 -*-
class Vector(object):
    def __init__(self, x, y):
        """ Create a vector, example: v = Vector(1,2) """
        self.x = x
        self.y = y

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)

    def c(self):
        return (self.x, self.y)
        
# objective function
def f(point):
    x, y = point
    return (1-x)**2 + 100*(y-x**2)**2

def nelder_mead(alpha=1, beta=0.5, gamma=2, maxiter=850):
    
    # initialization
    v1 = Vector(-1, -1)
    v2 = Vector(1, -4)
    v3 = Vector(2, 0)

    for i in range(maxiter):
        adict = {v1:f(v1.c()), v2:f(v2.c()), v3:f(v3.c())}
        points = sorted(adict.items(), key=lambda x: x[1])
        
        best = points[0][0]
        good = points[1][0]
        worst = points[2][0]
        
        
        mid = (good + best)/2

        # reflection
        xr = mid + alpha * (mid - worst)
        if f(xr.c()) < f(good.c()):
            worst = xr
        elif f(xr.c()) < f(worst.c()):
                worst = xr
                c = (worst + mid)/2
                if f(c.c()) < f(worst.c()):
                    worst = c
        elif f(xr.c()) < f(best.c()):

            # expansion
            xe = mid + gamma * (xr - mid)
            if f(xe.c()) < f(xr.c()):
                worst = xe
            else:
                worst = xr
        elif f(xr.c()) > f(good.c()) and f(xr.c()) < f(worst.c()):
            
            # contraction
            xc = mid + beta * (worst - mid)
            if f(xc.c()) < f(worst.c()):
                worst = xc
        elif f(xr.c()) > f(worst.c()):
    
            #reduction
            worst = (worst + best)/2
            good = (good + best)/2

        # update points
        v1 = worst
        v2 = good
        v3 = best
    return best

print("Result of Nelder-Mead algorithm: ")
xk = nelder_mead()
print("Best points is: %s"%(xk))
print("Min is:", f(xk.c()))




 