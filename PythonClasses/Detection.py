import stbt  # Framework is not available for Pycharm
import Keys


class Detection(object):

    def __init__(self):
        self.failinfo = ""
        self.key = Keys.Keys()

    def getfail(self):
        return self.failinfo

    # Looking for motion for about 300+ iterations
    def motion(self):
        try:
            if stbt.wait_for_motion(30):
                i = 0
                while stbt.wait_for_motion(10) and i < 20:  # later 300
                    print "Wait for Motion ", i
                    i += 1
                self.key.pause()
            return True

        except stbt.MotionTimeout:
            if stbt.is_screen_black():
                self.failinfo += "\nScreen is black"
            else:
                self.failinfo += "\nThere was a Problem during Playtime!"
            return False
