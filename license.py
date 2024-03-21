regionalPrefixSystem = False #1904 – 1932
threeLetterRegionalPrefix = False #1933 – 1950
flippedThreeLetterRegionalPrefix = False #1951 – 1962
suffixSystem = False #1963 – 1982
prefixSystem = False #1983 – 2000
currentSystem = False #2001 – current 

count = []

def alphabet(startRange, rangeCheck):
    numberOfAlpha = 0
    for i in range(startRange,rangeCheck): 
        memoryTagCheck = count[i].isalpha()
        if not memoryTagCheck:
            numberOfAlpha = numberOfAlpha
        else:
            numberOfAlpha += 1
    return numberOfAlpha
    
#checks which model of licence
def year(licence):
    numberOfAlpha = 0
    global count
    count = [x for x in licence]

    if len(count) == 6:
        #print(6, "alphabetical charachter(s)")
        if alphabet(0,3) == 2 and alphabet(2,5) == 0:
            regionalPrefixSystem = True
            print("regionalPrefixSystem 1904 – 1932")
        
        elif alphabet(0,3) == 3 and alphabet(3,5) == 0:
            threeLetterRegionalPrefix = True
            print("threeLetterRegionalPrefix 1933 – 1950")
                
        elif alphabet(0,2) == 0 and alphabet(3,5) == 2:
            flippedThreeLetterRegionalPrefix = True
            print("flippedThreeLetterRegionalPrefix 1951 – 1962")
        else:
            print("Custom Licence")

    elif len(count) == 7:
        #print(7, "alphabetical charachter(s)")
        if alphabet(0,2) == 1 and alphabet(2,3) == 0:
                print("Suffix System 1963 to 1982")
                suffixSystem = True
                
        elif alphabet(0,2) == 0 and alphabet(3,6) == 3:
            print("Prefix System 1983 to 2000")
            prefixSystem = True
        #modern AB 12 CDE
        if alphabet(0,2) == 2 and alphabet(2,3) == 0 and alphabet(4,6) == 2:
            print("Current")
        else:
            print("Custom Licence")
            

while True:
    inVal = input("\nLicence Number UK (no Space): ")
    if len(inVal) <= 8:
        print("Processesing Licence...\n")
        break
    else:
        print("Invalid Licence or possibly a custom one")
year(inVal)

#https://www.belinus.co.uk/uk-number-plates.php
#https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom
#https://vehicleenquiry.service.gov.uk/?locale=en
#https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom#Registration_plate_styles
#https://www.newreg.co.uk/dvla-number-plate-identifiers/
#https://realpython.com/python-gui-tkinter/
