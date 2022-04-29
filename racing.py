import arcade
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Need For Speed"
CAR_SPEED = 5
CAR_ANGLE = 20
WALL_SPEED = 5
class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 56:
            self.left = 56
        if self.right > SCREEN_WIDTH - 56:
            self.right = SCREEN_WIDTH - 56

class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT+random.randint(0,SCREEN_HEIGHT)
            self.center_x = random.randint(168,SCREEN_WIDTH-168)
            window.score+=1
class My_game(arcade.Window):
    def __init__(self, width , height , title):
        super().__init__(width, height , title)
        self.bg = arcade.load_texture("bg.png")
        self.car = Car("yellow_car.png",0.25)
        self.wall = Wall("blue_car.png",0.8)
        self.game = True
        self.wasted = arcade.load_texture("wasted.png")
        self.score = 0


    def setup(self):
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 100
        self.wall.center_x = random.randint(168,SCREEN_WIDTH-168)
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.change_y = WALL_SPEED

    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.car.draw()
        self.wall.draw()
        if not self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 + 28,SCREEN_WIDTH - 100,200,self.wasted)
            # arcade.draw_rectangle_filled(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 + 28,SCREEN_WIDTH,100,arcade.color.GRAY)
            # arcade.draw_text("Wasted",SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2, arcade.color.RED, font_size=60)
        arcade.draw_text(f"счет: {self.score}",SCREEN_WIDTH - 160,SCREEN_HEIGHT - 40,arcade.color.RED,font_size=30)


    def update(self, delta_time):
        self.car.update()
        if self.game:
            self.wall.update()
        if arcade.check_for_collision(self.car,self.wall):
            self.game = False

    def on_key_press(self,key,modifires):
        if self.game:
            if key == arcade.key.A:
                self.car.change_x = -CAR_SPEED
                self.car.angle = CAR_ANGLE
            if key == arcade.key.D:
                self.car.change_x = CAR_SPEED
                self.car.angle = -CAR_ANGLE
    def on_key_release(self,key,modifires):
        if key == arcade.key.A:
            self.car.change_x = 0
            self.car.angle = 0
        if key == arcade.key.D:
            self.car.change_x = 0
            self.car.angle = 0






window = My_game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()