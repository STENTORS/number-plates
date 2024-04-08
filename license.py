import os

regionalPrefixSystem = False #1904 – 1932 -------------------------AB 1234
threeLetterRegionalPrefix = False #1933 – 1950---------------------ABC 123
flippedThreeLetterRegionalPrefix = False #1951 – 1962--------------123 ABC
suffixSystem = False #1963 – 1982----------------------------------ABC 123 D
prefixSystem = False #1983 – 2000----------------------------------A 123 BCD
currentSystem = False #2001 – current -----------------------------AB 12 CDE

count = []

def licenseLocation(location):
    regionID = {
        "Anglia": {
            "Peterborough": ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"],
            "Norwich": ["AO", "AP", "AR", "AS", "AT", "AU"],
            "Ipswich": ["AV", "AW", "AX", "AY"]
        },
        "Birmingham": {
            "Birmingham": ["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO",
                           "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"]
        },
        "Cymru": {
            "Cardiff": ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL", "CM", "CN", "CO"],
            "Swansea": ["CP", "CR", "CS", "CT", "CU", "CV"],
            "Bangor": ["CW", "CX", "CY"]
        },
        "Deeside to Shrewsbury": {
            "Chester": ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DJ", "DK"],
            "Shrewsbury": ["DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY"]
        },
        "Essex": {
            "Chelmsford": ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO",
                           "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY"]
        },
        "Forest and Fens": {
            "Nottingham": ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", "FK", "FL", "FM", "FN", "FP"],
            "Lincoln": ["FR", "FS", "FT", "FV", "FW", "FX", "FY"]
        },
        "Garden of England": {
            "Maidstone": ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO"],
            "Brighton": ["GP", "GR", "GS", "GT", "GU", "GV", "GX", "GY"]
        },
        "Hampshire and Dorset": {
            "Bournemouth": ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ"],
            "Portsmouth": ["HK", "HL", "HM", "HN", "HO", "HP", "HR", "HS", "HT", "HU", "HV", "HX", "HY"],
            "Portsmouth (Isle of Wight)": ["HW"]
        },
        "Luton": {
            "Luton": ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ", "KK", "KL"]
        },
        "Northampton": {
            "Northampton": ["KM", "KN", "KO", "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY"]
        },
        "London": {
            "Wimbledon": ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LJ"],
            "Stanmore": ["LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT"],
            "Sidcup": ["LU", "LV", "LW", "LX", "LY"]
        },
        "Manchester and Merseyside": {
            "Manchester": ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MO", "MP",
                           "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY"]
        },
        "North": {
            "Newcastle": ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO"]
        },
        "Stockton": {
            "Stockton": ["NP", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY"]
        },
        "Oxford": {
            "Oxford": ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM", "ON", "OO", "OP",
                       "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY"]
        },
        "Preston": {
            "Preston": ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PJ", "PK", "PL", "PM", "PN", "PO", "PP",
                        "PR", "PS", "PT"],
            "Carlisle": ["PU", "PV", "PW", "PX", "PY"]
        },
        "Reading": {
            "Reading": ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP",
                        "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY"]
        },
        "Scotland": {
            "Glasgow": ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ"],
            "Edinburgh": ["SK", "SL", "SM", "SN", "SO"],
            "Dundee": ["SP", "SR", "SS", "ST"],
            "Aberdeen": ["SU", "SV", "SW"],
            "Inverness": ["SX", "SY"]
        },
        "Severn Valley": {
            "Worcester": ["VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", "VN", "VO", "VP",
                          "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY"]
        },
        "West of England": {
            "Exeter": ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WJ"],
            "Truro": ["WK", "WL"],
            "Bristol": ["WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY"]
        },
        "Yorkshire": {
            "Leeds": ["YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YJ", "YK"],
            "Sheffield": ["YL", "YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU"],
            "Beverley": ["YV", "YW", "YX", "YY"]
        }
    }

    for region, offices in regionID.items():
        for office, tags in offices.items():
            if location in tags:
                return region, office
    return "Unknown", "Unknown"  

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
    print("‾‾‾‾‾‾‾‾‾")

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
            
        elif licence == "A14EMC" or licence == "a14emc":
            print("EXAMPLE OF MOT DATA\nCustom")
            
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
        
        if yearOne >= 5:
            yearOne = yearOne - 5
            print("Second half of:")
        else:
            print("First half of:")
        yearOne = str(yearOne)
        
        year = "20"+yearOne+yearTwo
        print("year", year)

        #Local memory tag check
        location = count[0] + count[1]
        region, office = licenseLocation(location)
        print("Region:", region)
        print("DVLA Office:", office)

#A14EMC

