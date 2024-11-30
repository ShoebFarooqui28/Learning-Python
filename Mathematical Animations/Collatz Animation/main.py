from manim import *

class Graph2D(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 20, 2],
            y_range=[0, 20, 2],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=6
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axes_coords = axes.add_coordinates(font_size = 16)
        
        origin_label = MathTex("0").scale(0.4).next_to(axes.c2p(0,0), DOWN * 0.5 + LEFT * 0.5)
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(axes_coords))
        self.play(Create(origin_label))
        self.wait(10)

