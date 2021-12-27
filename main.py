def on_forever():
    basic.show_leds("""
        # . . . .
                # . . . .
                # . . . .
                # . . . #
                # # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
                . . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . . . . #
                . . . . #
                . . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . . . # #
                . . . . #
                . . . . #
                . . . . #
                # # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . . # # #
                . . . . #
                . . . . #
                . . . . #
                . # # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        . # # # #
                . . . . #
                . . . . #
                . . . . #
                . . # # #
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                . . . . #
                . . . . #
                . . . . #
                . . . # #
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                . . . . #
                . . . . #
                . . . . #
                . . . # #
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . #
                . . . . #
                . . . . #
                . . . . #
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                . . . . #
                . . . . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . .
                . . . . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . .
                # . . . .
                # . . . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . .
                # . . . .
                # . . . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                # . . . .
                # . . . .
                # . . . .
                # # . . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # .
                # . . . .
                # . . . .
                # . . . .
                # # # . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # . .
                # . . . .
                # . . . .
                # . . . .
                # # # # .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # . . .
                # . . . .
                # . . . .
                # . . . .
                # # # # #
    """)
    basic.pause(10)
basic.forever(on_forever)
