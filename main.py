def on_on_overlap(sprite, otherSprite):
    game.game_over(False)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

NewSprite = sprites.create(assets.image("""
    Hero
"""), SpriteKind.player)
controller.move_sprite(NewSprite)
NewSprite.set_stay_in_screen(True)
NewFood = sprites.create(assets.image("""
    Burger
"""), SpriteKind.food)
NewFood.x = 20
NewFood.y = 20
NewFood.x = randint(10, 150)
NewFood.y = randint(10, 80)
EvilPerson = sprites.create(assets.image("""
    EvilPerson
"""), SpriteKind.enemy)
EvilPerson.x = randint(10, 150)
EvilPerson.x = randint(10, 80)
EvilPerson.follow(NewSprite, 60)