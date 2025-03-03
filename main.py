def on_countdown_end():
    pass
info.on_countdown_end(on_countdown_end)

def on_on_score():
    game.game_over(True)
info.on_score(2, on_on_score)

def on_on_overlap(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
    sprite2.say_text("Got it!")
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

game.show_long_text("Welcome to my game!", DialogLayout.CENTER)
pause(100)
game.show_long_text("You are in a small room, and there is no escape. Stay alive for 25 seconds to defeat the beast. If the beast runs into you, the game ends... ",
    DialogLayout.CENTER)
pause(100)
game.show_long_text("Ready?", DialogLayout.CENTER)
pause(100)
NewSprite = sprites.create(assets.image("""
    Hero
"""), SpriteKind.player)
NewSprite.x = randint(10, 150)
controller.move_sprite(NewSprite)
NewSprite.set_stay_in_screen(True)
EvilPerson1 = sprites.create(assets.image("""
    EvilPerson
"""), SpriteKind.enemy)
EvilPerson2 = sprites.create(assets.image("""
    EvilPerson
"""), SpriteKind.enemy)
NewFood = sprites.create(assets.image("""
    Burger
"""), SpriteKind.food)
New_Food2 = sprites.create(assets.image("""
    Burger
"""), SpriteKind.food)
NewFood.x = randint(10, 150)
New_Food2.x = randint(10, 150)
info.set_score(0)
info.start_countdown(25)
EvilPerson1.x = randint(1, 1)
EvilPerson1.y = randint(1, 1)
EvilPerson2.x = randint(20, 20)
EvilPerson2.y = randint(20, 20)
EvilPerson1.follow(NewSprite, 60)
EvilPerson2.follow(NewSprite, 60)