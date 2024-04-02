import webbrowser
import time

urls = [
    "https://www.belinus.co.uk/uk-number-plates.php",
    "https://www.belinus.co.uk/plates-format-history.php",
    "https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom",
    "https://vehicleenquiry.service.gov.uk",
    "https://www.newreg.co.uk/dvla-number-plate-identifiers/",
    "https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom#Registration_plate_styles",
    "https://realpython.com/python-gui-tkinter/"
]

for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(1)
