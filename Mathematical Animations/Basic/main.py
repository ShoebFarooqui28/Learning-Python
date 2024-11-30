from manim import *

class Basic(Scene):
    def construct(self):
        name = Tex("Shoeb").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)
        rect = Rectangle(width=1, height=0.5, fill_color=RED, fill_opacity=1)
        
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.play(Create(rect))
        self.wait()
        
    