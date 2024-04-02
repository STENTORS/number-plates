import os

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
    global regionalPrefixSystem
    global threeLetterRegionalPrefix
    global flippedThreeLetterRegionalPrefix
    global suffixSystem
    global prefixSystem
    global currentSystem
    count = [x for x in licence]

    print("_________")
    print("|", licence,"|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

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

        #example of details from MOT checker
        elif licence == "A14EMC" or licence == "a14emc":
            print("Vehicle make: TOYOTA\nDate of first registration: March 2008\nYear of manufacture: 2008")
            print("Cylinder capacity: 1497 cc\nCO₂ emissions: 104 g/km\nFuel type: HYBRID ELECTRIC")
            print("Vehicle status: Taxed\nVehicle colour: SILVER\nVehicle type approval: M1")
            print("Wheelplan: 2 AXLE RIGID BODY\nDate of last V5C (logbook) issued: 1 June 2020")
            
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
            
        elif count[3] == "D" or count[3] =="X" or count[3] == "d" or count[3] == "d" and alphabet(4,6) == 0:
            diplomatOne = int(count[0] + count[1] + count[2])
            diplomatTwo = int(count[4] + count[5] + count[6])

            print(diplomatOne)
            print(diplomatTwo)

            if diplomatTwo >= 101:
                print("Diplomat acording to the 101 - 399")
            elif diplomatTwo >= 400:
                print("non-diplomatic staff of international organisations")
            elif diplomatTwo >= 700:
                print("consular or other non-diplomatic staff")

                
            if diplomatOne == 101:
                print("Afghanistan (Islamic Republic")
            
            if count[3] =="D" or "d":
                print("diplomats")
            else:
                print("Non-diplomatic accredited personnel")
            
            
        #modern AB 12 CDE
        elif alphabet(0,2) == 2 and alphabet(2,3) == 0 and alphabet(4,6) == 2:
            currentSystem = True
            print("Current")

        else:
            print("Custom Licence")
            
while True:
    while True:
        inVal = input("\nLicence Number UK (no Space): ")
        if len(inVal) <= 8:
            print("Processesing Licence...\n")
            break
        else:
            print("Invalid Licence or possibly a custom one")

    year(inVal)
    

    #calculate the year
    if (currentSystem):
        yearOne = count[2]
        yearTwo = count[3]
        yearOne = int(yearOne)
        
        if yearOne > 5:
            yearOne = yearOne - 5
            print("Second half of:")
        else:
            print("First half of:")
        yearOne = str(yearOne)
        
        year = "20"+yearOne+yearTwo
        print("year", year)

#A14EMC

