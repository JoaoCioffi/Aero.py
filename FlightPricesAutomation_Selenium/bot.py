from methods import Booking

def invokeBotActions(callMethod=Booking()):
    actions = {'land_first_page':callMethod.land_first_page(),
               'accept_cookies_if_exists':callMethod.acceptCookies(),
               'departure':callMethod.selectDeparture(departureLocation='Los Angeles'),
               'arrival':callMethod.selectArrival(arrivalLocation='São Paulo'),
               'selectDates':callMethod.searchCalendar(departureDate='Wed Sep 21 2022',arrivalDate='Thu Sep 22 2022')}
    return actions