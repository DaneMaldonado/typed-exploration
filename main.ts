sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    game.gameOver(true)
})
let NewSprite = sprites.create(assets.image`
    Hero
`, SpriteKind.Player)
controller.moveSprite(NewSprite)
NewSprite.setStayInScreen(true)
let NewFood = sprites.create(assets.image`
    Burger
`, SpriteKind.Food)
NewFood.x = 20
NewFood.y = 20
NewFood.x = randint(10, 150)
NewFood.y = randint(10, 80)
let EvilPerson = sprites.create(assets.image`
    EvilPerson
`, SpriteKind.Enemy)
EvilPerson.x = randint(10, 150)
EvilPerson.x = randint(10, 80)
EvilPerson.follow(NewSprite, 60)
