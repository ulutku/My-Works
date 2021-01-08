from manimlib.imports import *
import numpy as np


def quadrat(a, b, c, d, x):
    return a*np.power(x+c, 1/b)+d


def func_updater(func):
    func = FunctionGraph(lambda x: quadrat(a_value.get_value(), b_value.get_value(
    ), c_value.get_value(), d_value.get_value(), x), x_min=-(c_value.get_value()), x_max=100, step_size=0.001)


class graphx(GraphScene):
    CONFIG = {
        "x_min": -50,
        "x_max": 100,
        "y_min": -20,
        "y_max": 20,
        "x_tick_frequency": 10,
        "y_tick_frequency": 10,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "y_axis_height": 4.5,
        "axes_color": WHITE,
        "graph_origin": 1.5*DOWN+2*LEFT,
        "exclude_zero_label": False,
    }
    # defining graph function

    def construct(self):
        self.setup_axes(animate=True)
        equation = TexMobject("a\\sqrt[b]{c+x}+d")
        equation.to_edge(UP+LEFT)
        a_value = ValueTracker(1)
        b_value = ValueTracker(2)
        c_value = ValueTracker(0)
        d_value = ValueTracker(0)
        a_label = TextMobject("a","=")
        #a_label[0].set_color(RED)
        b_label = TextMobject("b","=")
        #b_label[0].set_color(ORANGE)
        c_label = TextMobject("c","=")
        #c_label[0].set_color(GREEN)
        d_label = TextMobject("d","=")
        #d_label[0].set_color(PINK)
        a_value_label = DecimalNumber(a_value.get_value()).add_updater(
            lambda v: v.set_value(a_value.get_value()))
        b_value_label = DecimalNumber(b_value.get_value()).add_updater(
            lambda v: v.set_value(b_value.get_value()))
        c_value_label = DecimalNumber(c_value.get_value()).add_updater(
            lambda v: v.set_value(c_value.get_value()))
        d_value_label = DecimalNumber(d_value.get_value()).add_updater(
            lambda v: v.set_value(d_value.get_value()))
        labels = VGroup(a_label, a_value_label, b_label, b_value_label, c_label, c_value_label, d_label, d_value_label)
        VGroup(a_value_label, b_value_label, c_value_label, d_value_label).arrange_submobjects(DOWN)
        a_label.next_to(a_value_label, LEFT, buff=0.15)
        b_label.next_to(b_value_label, LEFT, buff=0.15)
        c_label.next_to(c_value_label, LEFT, buff=0.15)
        d_label.next_to(d_value_label, LEFT, buff=0.15)
        labels.to_edge(UP+RIGHT)

        func = self.get_graph(lambda x: quadrat(a_value.get_value(), b_value.get_value(), c_value.get_value(
        ), d_value.get_value(), x), x_min=-(c_value.get_value()), x_max=100, step_size=0.001, stroke_width=1)
        func.set_color(BLUE)
        func.add_updater(
            lambda mob: mob.become(
                self.get_graph(lambda x: quadrat(a_value.get_value(), b_value.get_value(), c_value.get_value(), d_value.get_value(), x), x_min=-(c_value.get_value()), x_max=100, step_size=0.001, color=BLUE, stroke_width=1))
        )
        self.play(ShowCreation(func), run_time=2)
        self.wait()
        self.play(Write(equation), run_time=2)
        self.wait(0.5)
        self.play(Write(labels))
        self.play(
            a_value.set_value, 3,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            a_value.set_value, 0.2,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            a_value.set_value, 1,
            rate_func=smooth,
            run_time=3
        )
        self.wait(3)
        self.play(
            b_value.set_value, 4,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            b_value.set_value, 1,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            b_value.set_value, 3,
            rate_func=smooth,
            run_time=3
        )
        self.wait(3)
        self.play(
            c_value.set_value, -8,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            c_value.set_value, 8,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            c_value.set_value, 0,
            rate_func=smooth,
            run_time=3
        )
        self.wait(3)
        self.play(
            d_value.set_value, 4,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            d_value.set_value, -4,
            rate_func=smooth,
            run_time=3
        )
        self.wait()
        self.play(
            d_value.set_value, 0,
            rate_func=smooth,
            run_time=3
        )
        self.wait(3)
