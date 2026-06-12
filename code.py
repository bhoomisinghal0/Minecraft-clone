from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Setup player and environment
player = FirstPersonController()
Sky()

boxes = []

# Generate the initial grid
for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture='grass',     # Extention (.png) can be omitted in Ursina
            parent=scene,
            origin_y=0.5,
            collider='box'       # REQUIRED: Allows mouse hovering to work
        )
        boxes.append(box)        # FIXED: Append to the list, not the block itself

# Handle block placement and destruction
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=color.white,
                    model='cube',
                    position=box.position + mouse.normal,
                    texture='grass',
                    parent=scene,
                    origin_y=0.5,
                    collider='box' # REQUIRED: Allows interaction with new blocks
                )
                boxes.append(new) # FIXED: Append the new block to your tracker list
                
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)
                break             # Break out of loop to avoid modifying list during iteration

app.run()
