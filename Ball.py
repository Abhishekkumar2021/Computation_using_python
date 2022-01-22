
# we first take input for the initial velocity of the ball when it is thrown from the ground
u = int(input('Please provide the initial velocity of the ball:  '))
t = int(input(
    'Please provide the time at which you want to get statistics about the ball: '))
g = 9.81
s = u*t - g*t*t
v = u-g*t
T = 2*u/g
if s < 0:
    print(f"Ball has already reached to the ground")
else:
    print(f"The time period of the ball is {T} seconds")
    print(
        f"The velocity of ball is {v} and the distance from the ground is {s}")
