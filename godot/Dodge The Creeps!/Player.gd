extends Area2D

export var speed: int = 400 # in pixels/second. Exporting allows us to see it in the inpsector
var screen_size: Vector2

func _ready():
	screen_size = get_viewport_rect().size
