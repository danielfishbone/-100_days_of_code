"""day 6 of 100 days of code 
this is the reeborg course, this course has random hurdle height,occurence and positions
goto https://https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
to use the reeborg world """

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    height = 0
    turn_left()
    while wall_on_right():
            move()
            height += 1
    turn_right()
    move()
    turn_right()
    while height > 0:
        move()
        height -= 1
    turn_left()
   

while not at_goal():
    if front_is_clear():
       
        move()
    if wall_in_front():
        jump()