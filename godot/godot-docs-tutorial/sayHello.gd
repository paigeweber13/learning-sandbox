extends Panel

var accum = 0
var accum2 = 0

func _ready() -> void:
	get_node("Button").connect("pressed", self, "_on_Button_pressed")
	
func _on_Button_pressed() -> void:
	get_node("Label").text = "Hello!"

func _process(delta) -> void:
	accum += delta
	get_node("Label2").text = "Process accumulated time: " + str(accum)

func _physics_process(delta) -> void:
	accum2 += delta
	get_node("Label3").text = "Physics accumulated time: " + str(accum2)
