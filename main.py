# -*- coding: utf-8 -*-
"""
https://hugit.app/posts/kivy-ch1-clock-app.html
"""

from time import strftime
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = get_color_from_hex('#301216')

LabelBase.register(name='Roboto',
    fn_regular='Roboto-Thin.ttf',
    fn_bold='Roboto-Medium.ttf')

class ClockLayout(BoxLayout): 
    pass

class ClockApp(App):
    sw_seconds = 0
    sw_started =False
    def update_time(self, nap):
        self.root.time_prop.text = strftime('[b]%H[/b]:%M:%S')

    def update_clock(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            self.root.stopwatch.text = ('%02d:%02d.[size=80]%02d[/size]'%
                (int(minutes), int(seconds), int(seconds*100%100)))

    def start_stop(self):
        self.root.start_stop.text = ('Start'
            if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0
        self.root.stopwatch.text =  '00:00.[size=80]00[/size]'
    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
        Clock.schedule_interval(self.update_clock, 0)

if __name__ == '__main__':
    ClockApp().run()
