from manim import *
import numpy as np

class BlackBodyRadiation(Scene):
    def planck_law(self, wavelength, T):
        h = 6.626e-34  # Planck's constant (J*s)
        c = 3.0e8       # Speed of light (m/s)
        k = 1.381e-23   # Boltzmann constant (J/K)
        
        return ( (8 * np.pi * h * c) / (wavelength**5) ) / (np.exp((h * c) / (wavelength * k * T)) - 1)

    def construct(self):
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1.2, 0.2],
            x_length=7,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False
        ).add_coordinates()
        
        x_label = axes.get_x_axis_label("Wavelength (\\mu m)")
        y_label = axes.get_y_axis_label("Intensity (arb. units)")
        labels = VGroup(x_label, y_label)
        
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE]
        temperatures = [3000, 4000, 5000, 6000, 7000]
        
        curves = VGroup()
        wavelengths = np.linspace(0.1e-6, 3e-6, 200)
        max_intensity = max(self.planck_law(wavelengths, 7000))
        
        for i, T in enumerate(temperatures):
            intensities = self.planck_law(wavelengths, T) / max_intensity
            points = [axes.c2p(w * 1e6, I) for w, I in zip(wavelengths, intensities)]
            curve = VMobject().set_points_smoothly(points).set_color(colors[i])
            curves.add(curve)
            
        legend = VGroup(
            *[Dot(color=colors[i]).next_to(Tex(f"{T}K"), LEFT) for i, T in enumerate(temperatures)],
            *[Tex(f"{T}K").set_color(colors[i]) for i, T in enumerate(temperatures)]
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        
        self.play(Create(axes), Write(labels))
        self.play(*[Create(curve) for curve in curves], Write(legend))
        self.wait(3)
