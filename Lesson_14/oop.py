
'''
class ClassName(parent_list):
    body_of_class
'''


class Point:
    xx = 23
    yy = 0

    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y


pt1 = Point(3, 6)
# print(id(pt1))
# print(pt1.x)
# print(pt1.xx)
pt2 = Point()
# print(id(pt2))
#
# print(pt1.x)
# print(pt1.y)
# pt1.x = 9
# print(pt1.x)
# print(pt2.x)

print(pt1.xx)
print(pt2.xx)
Point.xx = 125
print(pt1.xx)
print(pt2.xx)
