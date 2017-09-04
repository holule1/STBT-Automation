import stbt
import time
import Functions
import random
import Keys


class Menu(object):

    def __init__(self):

        # Counter
        self.counter = 0

        # Random
        self.random = 0

        # Errorlog
        self.error_active = True
        self.errorlog = Functions.Functions(None, True)

        # Keys
        self.key = Keys.Keys()

        # Top menu
        self.topProsieben = "TopProsieben.png"
        self.topSixx = "TopSixx.png"
        self.topHerz = "TopHerz.png"
        self.topHome = "TopHome.png"
        # Top active
        self.topHomeActive = "TopHomeActive.png"
        self.topProsiebenActive = "TopProsiebenActive.png"
        self.topSateinsActive = "TopSateinsActive.png"
        self.topKabelActive = "TopKabelActive.png"
        self.topSixxActive = "TopSixxActive.png"
        self.topMaxxActive = "TopMaxxActive.png"
        self.topGoldActive = "TopGoldActive.png"
        self.topHerzActive = "TopHerzActive.png"
        self.topSettingsActive = "TopSettingsActive.png"
        # Top selected Fett
        self.topHomeSelected1 = "TopHomeSelected.png"
        self.topProsiebenSelected1 = "TopProsiebenSelected.png"
        self.topSateinsSelected1 = "TopSateinsSelected.png"
        self.topKabelSelected1 = "TopKabelSelected.png"
        self.topSixxSelected1 = "TopSixxSelected.png"
        self.topMaxxSelected1 = "TopMaxxSelected.png"
        self.topGoldSelected1 = "TopGoldSelected.png"
        self.topHerzSelected1 = "TopHerzSelected.png"
        self.topSettingsSelected1 = "TopSettingsSelected.png"
        # Top selected not Fett
        self.topHomeSelected2 = "TopHomeSelected2.png"
        self.topProsiebenSelected2 = "TopProsiebenSelected2.png"
        self.topSateinsSelected2 = "TopSateinsSelected2.png"
        self.topKabelSelected2 = "TopKabelSelected2.png"
        self.topSixxSelected2 = "TopSixxSelected2.png"
        self.topMaxxSelected2 = "TopMaxxSelected2.png"
        self.topGoldSelected2 = "TopGoldSelected2.png"
        self.topHerzSelected2 = "TopHerzSelected2.png"
        self.topSettingsSelected2 = "TopSettingsSelected2.png"

    # Return the Errorlog
    def getlog(self):
        return self.errorlog.getlog()

    # Set the Errorlog
    def __setlog(self, message):
        self.errorlog.setlog(message)

    # Check if one of these two pictures match within the screen
    def check(self, picture, picture_two=None):
        i = 0
        while i < 5:
            if picture_two is None:
                if stbt.match(picture, None, stbt.MatchParameters(None, None, None, 0.7)):
                    return True
            else:
                if (stbt.match(picture, None, stbt.MatchParameters(None, None, None, 0.7)) and stbt.match(picture_two, None, stbt.MatchParameters(None, None, None, 0.7))):
                    return True
            i += 1
        return False

    # Navigate to a specific Video
    def navigate_to_specific_video(self, name):
        # not implemented yet!
        pass

    # Navigate to any random Video
    def navigate_to_random_video(self):
        if self.navigate_top_menu():
            if self.navigate_top_icon("random"):
                down = random.randint(1, 4)
                right = random.randint(0, 5)
                i = 0
                while i < down:
                    self.key.down()
                    i += 1
                i = 0
                while i < right:
                    self.key.right()
                    i += 1
                self.key.ok()
                self.key.ok()
                self.key.ok()
                return True
        return False

    # Navigate back till the Picture match
    def navigate_back_till(self, picture, picture_two=None):
        i = 0
        while i < 5:
            if self.check(picture, picture_two):
                return True
            self.key.back()
            time.sleep(5)
            i += 1
        if self.error_active:
            self.__setlog("\nERROR in Function navigate_back_till, after 5 back klicks no Goal reached")
        return False

    # Navigate to the top menu
    def navigate_top_menu(self):
        i = 0
        if self.navigate_back_till(self.topProsieben) or self.navigate_back_till(self.topHerz):
            while not self.__check_top_menu():
                self.key.up()
                i += 1
                if i == 2:
                    if self.error_active:
                        error = "\nERROR in Function navigate_top_menu, after to many upklicks no Goal reached."
                        self.__setlog(error)
                    return False
            return True
        return False

    # Navigate to a specific point in the top menu. Available Options: home, prosieben, sateins, kabel, sixx, maxx, gold, heart, settings
    def navigate_top_icon(self, name):
        namelist = ("home", "prosieben", "sateins", "kabel", "sixx", "maxx", "gold", "heart", "settings", "random")
        if namelist.__contains__(name):

            should = self.__check_top_position(name)
            position = self.__check_top_position(str(self.__check_top_icon()))

            if should == 404 or position == 404:
                if self.error_active:
                    error = "\nERROR in Function navigate_top_icon, should or position on 404"
                    self.__setlog(error)
                return False

            if position == 123:
                return False

            if self.random != 0:
                should = self.random
            else:
                self.random = should

            move = should - position

            i = 0
            if move > 0:
                while i < move:
                    self.key.right()
                    i += 1
            elif move < 0:
                while i > move:
                    self.key.left()
                    i -= 1
            else:
                self.counter = 0
                self.random = 0
                self.key.ok()
                return True

            if self.counter < 5:
                self.counter += 1
                return self.navigate_top_icon(name)
            else:
                self.counter = 0
                self.random = 0
                if self.error_active:
                    self.__setlog("ERROR in Function navigate_top_icon.. after 5 Trys the Goal is not reached!")
                return False
        else:
            if self.error_active:
                self.__setlog("\nERROR in Function navigate_top_icon -> " + name + " does not match!")
                self.__setlog("\nPlease choose on of those Options: home, prosieben, sateins, kabel, sixx, maxx, gold, heart, settings")
            return False

    # Check if the Cursor is on the Top Menu
    def __check_top_menu(self):
        if self.check(self.topHomeSelected1) or self.check(self.topHomeSelected2):
            return True
        elif self.check(self.topProsiebenSelected1) or self.check(self.topProsiebenSelected2):
            return True
        elif self.check(self.topSateinsSelected1) or self.check(self.topSateinsSelected2):
            return True
        elif self.check(self.topKabelSelected1) or self.check(self.topKabelSelected2):
            return True
        elif self.check(self.topSixxSelected1) or self.check(self.topSixxSelected2):
            return True
        elif self.check(self.topMaxxSelected1) or self.check(self.topMaxxSelected2):
            return True
        elif self.check(self.topGoldSelected1) or self.check(self.topGoldSelected2):
            return True
        elif self.check(self.topHerzSelected1) or self.check(self.topHerzSelected2):
            return True
        elif self.check(self.topSettingsSelected1) or self.check(self.topSettingsSelected2):
            return True
        else:
            return False

    # check which icon is selected
    def __check_top_icon(self):
        if self.check(self.topHomeSelected1) or self.check(self.topHomeSelected2):
            return "home"
        elif self.check(self.topProsiebenSelected1) or self.check(self.topProsiebenSelected2):
            return "prosieben"
        elif self.check(self.topSateinsSelected1) or self.check(self.topSateinsSelected2):
            return "sateins"
        elif self.check(self.topKabelSelected1) or self.check(self.topKabelSelected2):
            return "kabel"
        elif self.check(self.topSixxSelected1) or self.check(self.topSixxSelected2):
            return "sixx"
        elif self.check(self.topMaxxSelected1) or self.check(self.topMaxxSelected2):
            return "maxx"
        elif self.check(self.topGoldSelected1) or self.check(self.topGoldSelected2):
            return "gold"
        elif self.check(self.topHerzSelected1) or self.check(self.topHerzSelected2):
            return "heart"
        elif self.check(self.topSettingsSelected1) or self.check(self.topSettingsSelected2):
            return "settings"
        else:
            if self.navigate_top_menu():
                return self.__check_top_icon()
            else:
                return "nothing"

    # check on which position the icon is
    def __check_top_position(self, name):

        switcher = {
            "home": 1,
            "prosieben": 2,
            "sateins": 3,
            "kabel": 4,
            "sixx": 5,
            "maxx": 6,
            "gold": 7,
            "heart": 8,
            "settings": 9,
            "nothing": 123,
            "random": random.randint(1, 7)
        }
        return switcher.get(name, 404)

    # check if there any Problems with the Icons.png's
    # This Test can take a while. Normal time about 20 Minutes
    def check_top_icons(self):

        self.error_active = False
        print "Error log is ", self.error_active

        self.__setlog("\n\n------------ ICON Test ------------")

        self.__setlog("\nStep 1/2. Navigation: \n")
        home = self.__get_navigate_state("home")
        prosieben = self.__get_navigate_state("prosieben")
        sateins = self.__get_navigate_state("sateins")
        kabel = self.__get_navigate_state("kabel")
        sixx = self.__get_navigate_state("sixx")
        maxx = self.__get_navigate_state("maxx")
        gold = self.__get_navigate_state("gold")
        heart = self.__get_navigate_state("heart")
        settings = self.__get_navigate_state("settings")

        self.__setlog("\nStep 2/2. Icons Bold:\n")
        self.__get_bold_icon_state(home, "home", self.topHomeSelected1)
        self.__get_bold_icon_state(prosieben, "prosieben", self.topProsiebenSelected1)
        self.__get_bold_icon_state(sateins, "sateins", self.topSateinsSelected1)
        self.__get_bold_icon_state(kabel, "kabel", self.topKabelSelected1)
        self.__get_bold_icon_state(sixx, "sixx", self.topSixxSelected1)
        self.__get_bold_icon_state(maxx, "maxx", self.topMaxxSelected1)
        self.__get_bold_icon_state(gold, "gold", self.topGoldSelected1)
        self.__get_bold_icon_state(heart, "heart", self.topHerzSelected1)
        self.__get_bold_icon_state(settings, "settings", self.topSettingsSelected1)

        self.__setlog("\n------------ ICON Test END ------------")

        self.error_active = True

    def __get_icon_state(self, name):
        if self.check(name):
            self.__setlog(name + " - Success")
        else:
            self.__setlog(name + " - FAIL")

    def __get_navigate_state(self, name):
        if self.navigate_top_icon(name):
            self.__setlog(name + " - Success")
            return True
        else:
            self.__setlog(name + " - FAIL\tLooks like both Icons are corrupt!")
            return False

    def __get_bold_icon_state(self, state, name, icon_name):
        if state:
            if self.navigate_top_icon(name):
                if self.navigate_top_menu():
                    self.__get_icon_state(icon_name)
            else:
                self.__setlog(name + " - FAIL\tLooks like both Icons are corrupt!")
