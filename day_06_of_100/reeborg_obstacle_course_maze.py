"""day 6 of 100 days of code 
this is the reeborg course, the goal of this course is to solve the maze at random starting positions facing random directions
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
   
    if wall_on_right():
        
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
    if front_is_clear():
        move()
            
