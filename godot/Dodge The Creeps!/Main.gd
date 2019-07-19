extends Node

export (PackedScene) var Mob
var score

func _ready():
	randomize()

func game_over():
	$ScoreTimer.stop()
	$MobTimer.stop()
	
func new_game():
	score = 0
	$Player.start($StartPosition.position)
	$StartTimer.start()

func _on_StartTimer_timeout():
	$MobTimer.start()
	$ScoreTimer.start()

func _on_ScoreTimer_timeout():
	score += 1

func _on_MobTimer_timeout():
	# Choose a random location on MobPath
	$MobPath/MobSpawnLocation.set_offset(randi())
	# create an instance of Mob and add it to scene
	var mob = Mob.instance()
	add_child(mob)
	# set the mob's position perpendicular to the path direction
	var direction = $MobPath/MobSpawnLocation.rotation + PI/2
	# set the mob's position to a random location
	mob.position = $MobPath/MobSpawnLocation.position
	# randomize direction a bit
	direction += rand_range(-PI/4, PI/4)
	mob.rotation = direction
	# set the velocity (speed and direction)
	mob.linear_velocity = Vector2(rand_range(mob.min_speed, mob.max_speed), 0)
	mob.linear_velocity = mob.linear_velocity.rotated(direction)
