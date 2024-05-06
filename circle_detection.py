def find_circle_boarder(image):
    circle_sum_x = 0
    circle_sum_y = 0

    circle_min_x = 0
    circle_max_y = 0
    circle_max_x = 0

    circle_count = 0
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y,x] is not [0,0,0]:
                circle_count += 1

                circle_sum_x += x
                circle_sum_y += y

                circle_min_x = min(circle_min_x, x)
                circle_max_x = max(circle_max_y, y)

    if circle_count == 0:
        raise Exception()
    else:
        circle_center_x = circle_sum_x / circle_count
        circle_center_y = circle_sum_y / circle_count
        circle_radius = (circle_max_x - circle_min_x) / 2
        return (int(circle_center_x), int(circle_center_y)), int(circle_radius)