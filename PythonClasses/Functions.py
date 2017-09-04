import time


class Functions(object):

    def __init__(self, name=None, concatinate=None):
        if not concatinate:
            self.__detaillog = "\n\n------------- log "+ name + " -------------\n"
        else:
            self.__detaillog = ""

    def setlog(self, text):
        print text
        self.__detaillog += "\n" + text

    def getlog(self):
        return self.__detaillog

    # Count down visible
    def timer(self, seconds):
        i = 0
        while i < seconds:
            print seconds - i, "Seconds left"
            time.sleep(1)
            i += 1

    # Proof if it was successful or even not!
    def proof(self, function):
        if function:
            print " - Success"
            self.__detaillog += " - Success"
            return True
        else:
            print " - FAIL!"
            self.__detaillog += " - FAIL!"
            return False
