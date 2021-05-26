class Point(object):
    """屏幕上的点"""

    def __init__(self, x=0, y=0):
        """初始化
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算距离
        :param other: 另外一点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx*dx + dy*dy) ** 0.5

    def __str__(self):
        return f'{self.x}, {self.y}'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1, p2)
print(p1.distance_to(p2))