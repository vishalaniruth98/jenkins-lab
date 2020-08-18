class Calculator:
    """Calculator"""
    def __init__(self):
        pass

    def add(self, num_x, num_y):
        """Addition"""
        return num_x + num_y

    def minus(self, num_x, num_y):
        """Minus"""
        return num_x - num_y

    def multiple(self, num_x, num_y):
        """Multiple"""
        return num_x * num_y

    def devide(self, num_x, num_y):
        """Divide"""
        return num_x/num_y

    def issame(self, num_x, num_y):
        return num_x == num_y

    def isSubstring(self, string, sub_str):
        return (string.find(sub_str) == -1)
