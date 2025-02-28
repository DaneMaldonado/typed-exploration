def on_on_overlap(sprite, otherSprite):
    game.game_over(False)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

game.show_long_text("Welcome to my game!", DialogLayout.BOTTOM)
pause(100)
game.show_long_text("You are in a small room, and there is no escape. Stay alive for 25 seconds to defeat the beast. If the beast runs into you, the game ends... ",
    DialogLayout.BOTTOM)
pause(100)
game.show_long_text("Ready?", DialogLayout.BOTTOM)
pause(100)
NewSprite = sprites.create(assets.image("""
    Hero
"""), SpriteKind.player)
controller.move_sprite(NewSprite)
NewSprite.set_stay_in_screen(True)
EvilPerson1 = sprites.create(assets.image("""
    EvilPerson
"""), SpriteKind.enemy)
EvilPerson2 = sprites.create(assets.image("""
    EvilPerson
"""), SpriteKind.enemy)
EvilPerson1.x = randint(10, 150)
EvilPerson1.y = randint(10, 80)
EvilPerson1.x = randint(10, 80)
EvilPerson2.y = randint(10, 80)
EvilPerson1.follow(NewSprite, 60)
EvilPerson2.follow(NewSprite, 60)