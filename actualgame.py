import pyglet

window=pyglet.window.Window(
	width=600,
	height=900,
	caption="actualgame")

label = pyglet.text.Label(
    "Hello, World!",
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center"
)

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event       
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
   if on_mouse_drag

def on_update(dt):
	print("bobert")
pyglet.clock.schedule_interval(on_update, 1/1.0)


pyglet.app.run()	