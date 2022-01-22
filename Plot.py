# import math as Math
from numpy import zeros
import matplotlib.pyplot as plt
from math import *
import matplotlib.pyplot as plt
from numpy import linspace

# this generates 1001 equally spaced numbers so we have 1000 intervals of equal size
t = linspace(0, 1, 1001)
# print(Math.atan(1)*180/Math.pi)

# print(atan(1)*180/pi)
y = 10*t-5*t*t
# print(y)
plt.plot(t, y)
plt.xlabel('t(s)')
plt.ylabel('y(m)')
plt.title("The graph")
plt.savefig('graph.png')
plt.savefig('graph.pdf')
plt.savefig('graph.jpg')
plt.savefig('graph.eps')
# PNG format # PDF format # JPG format
# Encanspulated PostScript format
# plt.show()

# h = zeros(4)
# h[0] = 1.60
# h[1] = 1.85
# h[2] = 1.75
# h[3] = 1.80
# H = zeros(4)
# H[0] = 0.50
# H[1] = 0.70
# H[2] = 1.90
# H[3] = 1.75
# family_member_no = zeros(4)
# family_member_no[0] = 0
# family_member_no[1] = 1
# family_member_no[2] = 2
# family_member_no[3] = 3
# plt.plot(family_member_no, h, family_member_no, H)
# plt.xlabel('Family member number')
# plt.ylabel('Height(m)')
# plt.show()
