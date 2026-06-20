from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Setup player and environment
player = FirstPersonController()
# Create a tiny crosshair in the center of the screen
crosshair_center = Entity(parent=camera.ui)      # Attach it to the UI layer so it stays locked to the screen
crosshair_vertical= Entity(
    model="quad",
    color=color.gray,
    scale=(0.004,0.1),
    parent=crosshair_center
)
crosshair_horizontal=Entity(
    model="quad",
    color=color.gray,
    scale=(0.1,0.004),
    parent=crosshair_center
)
Sky()

boxes = []
# Track the current active texture name
current_texture = 'grass'
   


def update():
    # If the player falls below the world (Y coordinate less than -10)
    if player.y < -10:
        player.position = (10, 3, 10) # Teleport them safely to the middle of the map


# Generate the initial grid
for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture=current_texture,     # Extention (.png) can be omitted in Ursina
            parent=scene,
            origin_y=0.5,
            collider='box'       # REQUIRED: Allows mouse hovering to work
        )
        boxes.append(box)        # FIXED: Append to the list, not the block itself

# Handle block placement and destruction
def input(key):
    global current_texture # Tell Python we want to change the variable we made above
    
    # Switch texture based on number keys pressed
    if key == '1':
        current_texture = 'grass'
    if key == '2':
        current_texture = 'white_cube' # Built-in Ursina texture that looks like smooth stone/plaster
    if key == '3':
        current_texture = 'brick'      # Built-in Ursina red brick texture
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=color.white,
                    model='cube',
                    position=box.position + mouse.normal,
                    # Find this line inside your left-click code block:
                    texture=current_texture, # FIXED: Uses whatever texture is currently active
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
