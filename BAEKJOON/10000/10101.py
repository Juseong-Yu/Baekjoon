Angle_1 = int(input())
Angle_2 = int(input())
Angle_3 = int(input())
if Angle_1 == Angle_2 == Angle_3 == 60:
    print('Equilateral')
elif Angle_1 + Angle_2 + Angle_3 == 180 and (Angle_1 == Angle_2 or Angle_1 == Angle_3 or Angle_2 == Angle_3):
    print('Isosceles')
elif  Angle_1 + Angle_2 + Angle_3 == 180:
    print('Scalene')
else:
    print('Error')