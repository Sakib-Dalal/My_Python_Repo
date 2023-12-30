import math


def paint_cal(height, width, cover):
    num_of_can = (height * width) / cover
    print(f"number of can required: {math.ceil(num_of_can)}")


test_h = int(input("Enter Height of Wall: "))
test_w = int(input("Enter Width of Wall: "))
coverage = 5

paint_cal(height=test_h, width=test_w, cover=coverage)
