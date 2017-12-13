class Vector:
    def __init__(self, point):
        x, y = (point.split())
        self.x = float(x.strip())
        self.y = float(y.strip())

if __name__ == "__main__":
    v = Vector("0.12 3.14")
    print("{}, {}".format(v.x, v.y))
    print(type(v.x))