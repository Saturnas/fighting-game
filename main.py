import kivy.app
import kivy.animation
import time
import random
import kivy.core.audio
import os
import kivy.uix.screenmanager



class TestApp(kivy.app.App):

    # game settings
    music_dir = os.getcwd() + "/music/"
    bg_music = kivy.core.audio.SoundLoader.load(music_dir+"background.mp3")
    bg_music.loop = True
    bg_music.play()
    checks = []
    checks2 = []
    health = 5
    enemy_health = 5
    level = 0

    def screen_num(self, arg):
        self.level = (arg)

    # on reset health goes to full
    def reset(self, arg):
        self.health = (arg)
        self.enemy_health = (arg)

    # checking if enemy and player health is not 0
    def test(self):
        if self.health >=0 and self.enemy_health >=0:
            return True
    
    # player images at the end of movement
    # if player health goes to 0 player image changes to RIP
    def char_animation_completed(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image']
        if self.health > 0:
            character_image.im_num = 61
        else:
            character_image.im_num = 86

    # get player image settings from kv file
    def change_char_im(self):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image']
        character_image.source = str(int(character_image.im_num)) + ".png"

    # player image changing timer
    def start_char_animation(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image = curr_screen.ids['character_image']
            character_image.im_num = 61
            char_animation0 = kivy.animation.Animation(pos_hint={'x': 0.05,\
             'y':0.16}, duration=1.1)
            char_animation1 = kivy.animation.Animation(pos_hint={'x':0.28,\
             'y':0.16}, size_hint=(0.35, 0.35), duration=2, im_num=85)
            char_animation11 = kivy.animation.Animation(pos_hint={'x':0.28,\
             'y':0.16}, size_hint=(0.35, 0.35), duration=1.2, im_num=85)
            music_dir = os.getcwd() + "/music/"
            self.f_music = kivy.core.audio.SoundLoader.load(music_dir+\
            "fighting.mp3")
            self.f_music.play()
            if self.health > 0:
                char_animation2 = kivy.animation.Animation(pos_hint={'x': 0.05,\
                 'y':0.16}, size_hint=(0.35, 0.35), duration=1.5, im_num=61)
            else:
                char_animation2 = kivy.animation.Animation(pos_hint={'x':0.3,\
                 'y':0.16}, size_hint=(0.26, 0.26), duration=0 ,im_num=86)
            all_anim = char_animation0 + char_animation1 +char_animation11+\
             char_animation2
            all_anim.bind(on_complete=self.char_animation_completed)
            all_anim.start(character_image)

    # enemy images at the end of movement, level 2
    # if enemy health goes to 0 enemy image changes to RIP
    def char_animation_completed22(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image22']
        if self.enemy_health > 0:
            character_image.im_num = 601
        else:
            character_image.im_num = 53

    # get enemy image settings from kv file, level 2
    def change_char_im22(self):
        curr_screen = self.root.screens[self.level]
        character_image22 = curr_screen.ids['character_image22']
        character_image22.source = str(int(character_image22.im_num)) + ".png"

    # enemy image changing time, level 2
    def start_char_animation22(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image22 = curr_screen.ids['character_image22']
            character_image22.im_num = 601
            char_animation0 = kivy.animation.Animation(pos_hint={'x': 0.65,\
             'y':0.15}, duration=1.1)
            char_animation1 = kivy.animation.Animation(pos_hint={'x':0.4,\
             'y':0.15}, size_hint=(0.32, 0.32), duration=2, im_num=617)
            char_animation11 = kivy.animation.Animation(pos_hint={'x':0.4,\
             'y':0.15},size_hint=(0.32, 0.32), duration=1.2, im_num=617)
            if self.enemy_health > 0:
                char_animation2 = kivy.animation.Animation(pos_hint={'x': 0.65,\
                 'y':0.15},size_hint=(0.32, 0.32), duration=1.5, im_num=601)
            else:
                char_animation2 = kivy.animation.Animation(pos_hint={'x':0.48,\
                 'y':0.18},size_hint=(0.22, 0.22), duration=0, im_num=53)
            all_anim = char_animation0 + char_animation1 +char_animation11+\
             char_animation2
            all_anim.bind(on_complete=self.char_animation_completed22)
            all_anim.start(character_image22)

    # enemy images at the end of movement, level 1
    # if enemy health goes to 0 enemy image changes to RIP
    def char_animation_completed2(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image2']
        if self.enemy_health > 0:
            character_image.im_num = 30
        else:
            character_image.im_num = 53

    # get enemy image settings from kv file, level 1
    def change_char_im2(self):
        curr_screen = self.root.screens[self.level]
        character_image2 = curr_screen.ids['character_image2']
        character_image2.source = str(int(character_image2.im_num)) + ".png"

    # enemy image changing time, level 1
    def start_char_animation2(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image2 = curr_screen.ids['character_image2']
            character_image2.im_num = 30
            char_animation0 = kivy.animation.Animation(pos_hint={'x': 0.7,\
             'y':0.16},duration=1.1)
            char_animation1 = kivy.animation.Animation(pos_hint={'x':0.33,\
             'y':0.16},size_hint=(0.35, 0.35), duration=2, im_num=52)
            char_animation11 = kivy.animation.Animation(pos_hint={'x':0.33,\
             'y':0.16},size_hint=(0.35, 0.35), duration=1.2, im_num=52)
            if self.enemy_health > 0:
                char_animation2 = kivy.animation.Animation(pos_hint={'x': 0.7,\
                 'y':0.16},size_hint=(0.35, 0.35), duration=1.5, im_num=30)
            else:
                char_animation2 = kivy.animation.Animation(pos_hint={'x':0.48,\
                 'y':0.18},size_hint=(0.22, 0.22), duration=0, im_num=53)
            all_anim = char_animation0 + char_animation1 +char_animation11+\
             char_animation2
            all_anim.bind(on_complete=self.char_animation_completed2)
            all_anim.start(character_image2)

    # judge animation at the end of movement
    def judge_animation_completed(self, *args):
        curr_screen = self.root.screens[self.level]
        judge_image = curr_screen.ids['judge']
        judge_image.im_num = 101

    # get judge image settings from kv file
    def change_judge_im(self):
        curr_screen = self.root.screens[self.level]
        judge_image = curr_screen.ids['judge']
        judge_image.source = str(int(judge_image.im_num)) + ".png"

    # judge image changing time
    def start_judge_animation(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            judge_image = curr_screen.ids['judge']
            judge_image.im_num = 101
            judge_animation1 = kivy.animation.Animation(duration=1, im_num=117)
            all_anim = judge_animation1
            all_anim.bind(on_complete=self.judge_animation_completed)
            all_anim.start(judge_image)

    # blood effect animation
    def char_animation_completed3(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image3']
        character_image.im_num = 200

    # get blood effect image settings from kv file
    def change_char_im3(self):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image3']
        character_image.source = str(int(character_image.im_num)) + ".png"

    # blood animation changing time
    def start_char_animation3(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image = curr_screen.ids['character_image3']
            character_image.im_num = 200
            char_animation0 = kivy.animation.Animation(pos_hint={'x': 0.2,\
             'y': 0.08},duration=3)
            char_animation1 = kivy.animation.Animation(pos_hint={'x': 0.2,\
             'y': 0.08},duration=1.5, im_num=215)
        
            all_anim = char_animation0 + char_animation1
            all_anim.bind(on_complete=self.char_animation_completed3)
            all_anim.start(character_image)

    # animated FIGHT writing on screen
    def char_animation_completed4(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image4']
        character_image.im_num = 300

    # get animated FIGHT image settings from kv file
    def change_char_im4(self):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image4']
        character_image.source = str(int(character_image.im_num)) + ".png"

    # animated FIGHT changing time
    def start_char_animation4(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image = curr_screen.ids['character_image4']
            character_image.im_num = 300
            char_animation0 = kivy.animation.Animation(pos_hint={'x': 0.2,\
             'y': 0.35},duration=0.4)
            char_animation1 = kivy.animation.Animation(pos_hint={'x': 0.2,\
             'y': 0.35},duration=2, im_num=345)
            
            all_anim = char_animation0 + char_animation1
            all_anim.bind(on_complete=self.char_animation_completed4)
            all_anim.start(character_image)

    # player health bar
    def char_animation_completed5(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image5']
        if self.health == 5:
            character_image.im_num = 401
        elif self.health == 4:
            character_image.im_num = 404
        elif self.health == 3:
            character_image.im_num = 406
        elif self.health == 2:
            character_image.im_num = 409
        elif self.health == 1:
            character_image.im_num = 411
        else:
            character_image.im_num = 412

    # get player health bar image settings from kv file
    def change_char_im5(self):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image5']
        character_image.source = str(int(character_image.im_num)) + ".png"

    # checking player current health
    def start_char_animation5(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image = curr_screen.ids['character_image5']
            if self.health == 5:
                character_image.im_num = 401
                char_animation1 = kivy.animation.Animation(duration=4)
            elif self.health == 4:
                character_image.im_num = 401
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=404)
            elif self.health == 3:
                character_image.im_num = 404
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=406)
            elif self.health == 2:
                character_image.im_num = 406
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=409)
            elif self.health == 1:
                character_image.im_num = 409
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=411)
            else:
                character_image.im_num = 411
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=412)

            try:
                all_anim = char_animation0 + char_animation1
                all_anim.bind(on_complete=self.char_animation_completed5)
                all_anim.start(character_image)
            except:
                pass

    # enemy health bar
    def char_animation_completed6(self, *args):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image6']
        if self.enemy_health == 5:
            character_image.im_num = 501
        elif self.enemy_health == 4:
            character_image.im_num = 504
        elif self.enemy_health == 3:
            character_image.im_num = 506
        elif self.enemy_health == 2:
            character_image.im_num = 509
        elif self.enemy_health == 1:
            character_image.im_num = 511
        else:
            character_image.im_num = 512

    # get enemy health bar image settings from kv file
    def change_char_im6(self):
        curr_screen = self.root.screens[self.level]
        character_image = curr_screen.ids['character_image6']
        character_image.source = str(int(character_image.im_num)) + ".png"

    # checking enemy current health
    def start_char_animation6(self):
        if self.test() == True:
            curr_screen = self.root.screens[self.level]
            character_image = curr_screen.ids['character_image6']
            if self.enemy_health == 5:
                character_image.im_num = 501
                char_animation1 = kivy.animation.Animation(duration=4)
            elif self.enemy_health == 4:
                character_image.im_num = 501
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=504)
            elif self.enemy_health == 3:
                character_image.im_num = 504
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=506)
            elif self.enemy_health == 2:
                character_image.im_num = 506
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=509)
            elif self.enemy_health == 1:
                character_image.im_num = 509
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=511)
            else:
                character_image.im_num = 511
                char_animation0 = kivy.animation.Animation(duration=3)
                char_animation1 = kivy.animation.Animation(duration=1,\
                 im_num=512)
            try:
                all_anim = char_animation0 + char_animation1
                all_anim.bind(on_complete=self.char_animation_completed5)
                all_anim.start(character_image)
            except:
                pass

    # random choice which part of player body enemy attacks and part he defends
    def random_choices(self):
        x = ["Head", "Chest", "Hips", "Legs"]
        z = random.choice(x)
        string1="".join(str(elem) for elem in self.checks)
        if z != string1 and string1 != "":
            self.enemy_health -= 1
            print(self.enemy_health)
            print('enemy damaged')
        else:
            print('enemy defended')

        y = ["Head", "Chest", "Hips", "Legs"]
        z1 = random.choice(y)
        print(z1)
        string2="".join(str(elem) for elem in self.checks2)
        if z1 == string2:
            print('You defended')
        else:
            self.health -= 1
            print(self.health)
            print('You failed defence')
    
    # player choise which part of enemy body to attack   
    def checkbox_click(self, instance, value, topping):
        if value == True:
            TestApp.checks.append(topping)
            tops = ''
            for x in TestApp.checks:
                tops = f'{tops} {x}'
            curr_screen = self.root.screens[self.level]
            curr_screen.ids.output_label.text = f'Attacking: {tops}'
        else:
            TestApp.checks.remove(topping)
            tops = ''
            for x in TestApp.checks:
                tops = f'{tops} {x}'
            curr_screen = self.root.screens[self.level]
            curr_screen.ids.output_label.text = f'Attacking: {tops}'

    # player choise which part of enemy body to defend
    def checkbox_click2(self, instance, value, topping):
        if value == True:
            TestApp.checks2.append(topping)
            tops = ''
            for x in TestApp.checks2:
                tops = f'{tops} {x}'
            curr_screen = self.root.screens[self.level]
            curr_screen.ids.output_label2.text = f'Defending: {tops}'
        else:
            TestApp.checks2.remove(topping)
            tops = ''
            for x in TestApp.checks2:
                tops = f'{tops} {x}'
            curr_screen = self.root.screens[self.level]
            curr_screen.ids.output_label2.text = f'Defending: {tops}'

class Level1(kivy.uix.screenmanager.Screen):
    pass
class Level2(kivy.uix.screenmanager.Screen):
    pass
class MainScreen(kivy.uix.screenmanager.Screen):
    pass

app = TestApp()
app.run()
