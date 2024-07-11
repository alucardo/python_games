import colorgram

def get_color_from_image(file_name = 'hirst.jpg', number_of_colors = 8):
    colors = colorgram.extract(file_name, number_of_colors)
    color_tuples = []
    for color in colors:
        rgb = color.rgb
        color_tuples.append((rgb[0], rgb[1], rgb[2]))
    return color_tuples