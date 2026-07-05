"""
Manim scene: Adding two numbers digit by digit (column addition with carries).

Run with:
    manim -pql digit_addition.py DigitAddition      # quick preview (480p)
    manim -pqh digit_addition.py DigitAddition      # high quality (1080p)
"""

from manim import *

# ----------------------------------------------------------------------------
# The two numbers to add. Change these to animate a different addition.
# ----------------------------------------------------------------------------
NUM_A = 4859
NUM_B = 3762


class DigitAddition(Scene):
    def construct(self):
        a_digits = [int(d) for d in str(NUM_A)]
        b_digits = [int(d) for d in str(NUM_B)]
        n = max(len(a_digits), len(b_digits))
        a_digits = [0] * (n - len(a_digits)) + a_digits
        b_digits = [0] * (n - len(b_digits)) + b_digits

        # Pre-compute the addition, column by column (right to left).
        carries = [0] * (n + 1)
        results = [0] * n
        for i in range(n - 1, -1, -1):
            total = a_digits[i] + b_digits[i] + carries[i + 1]
            results[i] = total % 10
            carries[i] = total // 10
        final_carry = carries[0]

        # ------------------------------------------------------------------
        # Title
        # ------------------------------------------------------------------
        title = Text("Adding Two Numbers, Digit by Digit", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # Layout constants
        # ------------------------------------------------------------------
        digit_w = 1.0
        total_cols = n + 1  # extra column on the left for a possible final carry
        grid_width = total_cols * digit_w

        # x-position (center) of column i (0 = leftmost digit of the numbers)
        def col_x(i):
            # i ranges 0..n-1 over digits; shift right by one column to leave
            # room for a potential leading carry digit.
            offset = i + 1
            return -grid_width / 2 + (offset + 0.5) * digit_w

        carry_col_x = -grid_width / 2 + 0.5 * digit_w  # leftmost column

        row_a_y = 1.0
        row_b_y = 0.0
        line_y = -0.6
        row_r_y = -1.4
        carry_row_y = row_a_y + 0.9

        # ------------------------------------------------------------------
        # Build the digit mobjects for A and B
        # ------------------------------------------------------------------
        a_mobs = []
        for i, d in enumerate(a_digits):
            m = Text(str(d), font_size=48)
            m.move_to([col_x(i), row_a_y, 0])
            a_mobs.append(m)

        b_mobs = []
        for i, d in enumerate(b_digits):
            m = Text(str(d), font_size=48)
            m.move_to([col_x(i), row_b_y, 0])
            b_mobs.append(m)

        plus = Text("+", font_size=48)
        plus.move_to([carry_col_x, row_b_y, 0])

        line = Line(
            [-grid_width / 2, line_y, 0],
            [grid_width / 2, line_y, 0],
        )

        self.play(
            LaggedStartMap(FadeIn, VGroup(*a_mobs), shift=UP, lag_ratio=0.1),
            LaggedStartMap(FadeIn, VGroup(*b_mobs), shift=UP, lag_ratio=0.1),
            FadeIn(plus),
        )
        self.play(Create(line))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # Column-by-column addition, from rightmost digit to leftmost.
        # ------------------------------------------------------------------
        result_mobs = [None] * n
        carry_mobs = [None] * n  # carry digit shown above column i-1 (to the left)
        pending_carry = 0

        for i in range(n - 1, -1, -1):
            da, db = a_digits[i], b_digits[i]
            total = da + db + pending_carry

            # Highlight the current column (A digit, B digit).
            box_a = SurroundingRectangle(a_mobs[i], color=YELLOW, buff=0.15)
            box_b = SurroundingRectangle(b_mobs[i], color=YELLOW, buff=0.15)
            self.play(Create(box_a), Create(box_b), run_time=0.4)

            # Build the little sum expression under the numbers to narrate the math.
            carry_note = f" + carry {pending_carry}" if pending_carry else ""
            expr_text = f"{da} + {db}{carry_note} = {total}"
            expr = Text(expr_text, font_size=32, color=YELLOW)
            expr.next_to(line, DOWN, buff=1.2)
            self.play(FadeIn(expr, shift=UP * 0.3))
            self.wait(0.6)

            digit_result = total % 10
            new_carry = total // 10

            # Place the result digit under this column.
            r_mob = Text(str(digit_result), font_size=48, color=GREEN)
            r_mob.move_to([col_x(i), row_r_y, 0])
            result_mobs[i] = r_mob

            self.play(
                TransformFromCopy(expr, r_mob),
                FadeOut(expr),
            )

            # If there's a carry, show it above the next column to the left.
            if new_carry:
                c_mob = Text(str(new_carry), font_size=32, color=RED)
                if i - 1 >= 0:
                    c_mob.move_to([col_x(i - 1), carry_row_y, 0])
                else:
                    c_mob.move_to([carry_col_x, carry_row_y, 0])
                carry_label = Text("carry", font_size=20, color=RED)
                carry_label.next_to(c_mob, UP, buff=0.1)
                carry_group = VGroup(c_mob, carry_label)
                carry_mobs[i] = carry_group
                self.play(FadeIn(carry_group, shift=DOWN * 0.3))
                self.wait(0.3)

            self.play(FadeOut(box_a), FadeOut(box_b))
            pending_carry = new_carry

        # ------------------------------------------------------------------
        # If there's a final carry left over, place it as a leading digit.
        # ------------------------------------------------------------------
        if final_carry:
            fc_mob = Text(str(final_carry), font_size=48, color=GREEN)
            fc_mob.move_to([carry_col_x, row_r_y, 0])
            self.play(FadeIn(fc_mob, shift=UP * 0.3))

        self.wait(0.5)

        # ------------------------------------------------------------------
        # Wrap up: show the final equation.
        # ------------------------------------------------------------------
        final_number = NUM_A + NUM_B
        summary = Text(
            f"{NUM_A} + {NUM_B} = {final_number}", font_size=40, color=GREEN
        )
        summary.next_to(VGroup(*result_mobs), DOWN, buff=1.0)
        self.play(Write(summary))
        self.wait(2)
