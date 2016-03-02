def rectangleArea(width, height):
    return width * height


rectangle = 20, 30
# print apply(rectangleArea, rectangle)
print rectangleArea(*rectangle)
