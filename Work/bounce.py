# bounce.py
#
# Exercise 1.5

#Initialized the height of the Ball.  
Height = 100
NewHeight = Height*3/5
i=0
while i<10:
    Height = round(Height*3/5,4)
    print(i+1,Height)
    i=i+1
print('The hieght of the ball is',Height,'after',i,'bounces')