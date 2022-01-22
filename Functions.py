import math


def poly_area(x, y):
    area = 0
    for i in range(len(x)):
        if i == len(x)-1:
            area += x[i]*y[0]-x[i]*y[0]
        else:
            area += x[i]*y[i+1]-y[i]*x[i+1]
    return math.fabs(0.5*area)


print(poly_area([0, 0, 0.5, 1, 1], [0, 1, 1.5, 1, 0]))
