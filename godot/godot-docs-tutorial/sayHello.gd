extends Panel

func _ready() -> void:
	get_node("Button").connect("pressed", self, "_on_Button_pressed")
	
func _on_Button_pressed() -> void:
	get_node("Label").text = "Hello!"
