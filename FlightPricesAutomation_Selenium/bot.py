from methods import Booking
from dependencies import load_dependencies as ld

def invokeBotActions(arg=Booking()):
    action = arg.land_first_page()
    return action