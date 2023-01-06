import colorgram
#image path
image_path = "/home/fishbone/-100_days_of_code/day_18_of_100/hirst1.jpeg"
color_set = []
def get_color(_path):
    rgb = []
    colors = colorgram.extract(_path,20)
    for color in colors:
        x = color.rgb
        r = x.r
        g = x.g
        b = x.b
        color_element = (r,g,b)
        rgb.append(color_element)
    return rgb
    
color_set = get_color(image_path)
print(color_set)   

