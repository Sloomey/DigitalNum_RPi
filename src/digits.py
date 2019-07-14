import LEDarea as area

def digit(num):
    if num == 0:
        area.MIDDLE_TOP()
        area.RIGHT_TOP()
        area.LEFT_TOP()
        area.LEFT_BOTTOM()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 1:
        area.RIGHT_TOP()
        area.RIGHT_BOTTOM()
    elif num == 2:
        area.MIDDLE_TOP()
        area.RIGHT_TOP()
        area.MIDDLE_MIDDLE()
        area.LEFT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 3:
        area.MIDDLE_TOP()
        area.RIGHT_TOP()
        area.MIDDLE_MIDDLE()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 4:
        area.LEFT_TOP()
        area.RIGHT_TOP()
        area.MIDDLE_MIDDLE()
        area.RIGHT_BOTTOM()
    elif num == 5:
        area.MIDDLE_TOP()
        area.LEFT_TOP()
        area.MIDDLE_MIDDLE()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 6:
        area.MIDDLE_TOP()
        area.LEFT_TOP()
        area.MIDDLE_MIDDLE()
        area.LEFT_BOTTOM()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 7:
        area.MIDDLE_TOP()
        area.RIGHT_TOP()
        area.RIGHT_BOTTOM()
    elif num == 8:
        area.MIDDLE_TOP()
        area.LEFT_TOP()
        area.RIGHT_TOP()
        area.MIDDLE_MIDDLE()
        area.LEFT_BOTTOM()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    elif num == 9:
        area.MIDDLE_TOP()
        area.LEFT_TOP()
        area.RIGHT_TOP()
        area.MIDDLE_MIDDLE()
        area.RIGHT_BOTTOM()
        area.MIDDLE_BOTTOM()
    else:
        print("Not a valid option.")
