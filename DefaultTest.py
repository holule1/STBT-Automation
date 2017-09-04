import PythonClasses.Detection as detectPy
import PythonClasses.Menu as menuPy
import PythonClasses.Functions as functionsPy


class Default(object):

    @staticmethod
    def start():
        function = functionsPy.Functions("Default Test")
        menu = menuPy.Menu()
        detect = detectPy.Detection()

        function.setlog("Start Default Test:")

        # Icon Test
        function.setlog("Icon Test")
        if not function.proof(menu.check_top_icons()):
            return function.getlog() + menu.getlog()

        # Test 1
        # function.setlog("Step 1. Navigate to the Top Menu")
        # if not function.proof(menu.navigate_top_menu()):
        #    return function.getlog() + menu.getlog()

        # Test 2
        # function.setlog("Step 2. Navigate to Pro7")
        # if not function.proof(menu.navigate_top_icon("prosieben")):
        #    return function.getlog() + menu.getlog()

        # Random Video Test
        # function.setlog("TEST 1. Navigate to any Random Video")
        # if not function.proof(menu.navigate_to_random_video()):
        #    return function.getlog() + menu.getlog()

        # function.setlog("TEST 2. Check if the Random Video runs correctly")
        # function.timer(10)
        # if not function.proof(detect.motion()):
        #    function.setlog(detect.getlog())
        #    return function.getlog()

        # in any Case return the log
        return function.getlog() + menu.getlog()
