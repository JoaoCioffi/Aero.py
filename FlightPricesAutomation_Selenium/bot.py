from methods import Booking

def invokeBotActions(callMethod=Booking()):
    actions = {'land_first_page':callMethod.land_first_page(),
               'accept_cookies_if_exists':callMethod.acceptCookies(),
               'departure':callMethod.selectDeparture(departureLocation='São Paulo'),
               'arrival':callMethod.selectArrival(arrivalLocation='Miami'),
               # 'selectDates':callMethod.searchCalendar(departureDate='Wed Sep 21 2022',arrivalDate='Thu Sep 22 2022') # Under Development
               'direct_flights_only':callMethod.directFlightsOnly(checkbox=False),
               'click_search_button':callMethod.searchFlights(),
               'filters':callMethod.toggleFilters(filters=True)
               }
    return actions