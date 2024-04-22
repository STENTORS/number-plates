import os

#? = contridicting sourses 
regionalPrefixSystem = False #1904 – 1932 -------------------------AB 1234
threeLetterRegionalPrefix = False #1933 – 1950------------------ABC 123
flippedThreeLetterRegionalPrefix = False #1951 – 1962------123 ABC
suffixSystem = False #1963 – 1982-------------------------------------ABC 123 D
prefixSystem = False #1983 – 2000-------------------------------------A 123 BCD
currentSystem = False #2001 – current -------------------------------AB 12 CDE

count = []
def diplomatLocation(locationCode):
    # Dictionary mapping location codes to their respective countries
    diplomatLocations = {
        "101": "Afghanistan (Islamic Republic)",
        "102": "Algeria",
        "103": "Argentina",
        "104": "Australia",
        "105": "Australia",
        "106": "Australia",
        "107": "Australia",
        "108": "Australia",
        "109": "Austria",
        "110": "Bahamas",
        "111": "Bahrain",
        "112": "Bangladesh",
        "113": "Barbados",
        "114": "Belgium",
        "115": "Benin",
        "116": "Bolivia",
        "117": "Botswana",
        "118": "Brazil",
        "119": "Brazil",
        "120": "Brazil",
        "121": "Brazil",
        "122": "Brazil",
        "123": "Bulgaria",
        "124": "Myanmar (formerly Burma)",
        "125": "Burundi",
        "126": "Cameroon",
        "127": "Canada",
        "128": "Canada",
        "129": "Canada",
        "130": "Canada",
        "131": "Canada",
        "132": "Central African Republic",
        "133": "Chad",
        "134": "Chile",
        "135": "China",
        "136": "Colombia",
        "137": "Republic of the Congo",
        "138": "Costa Rica",
        "139": "Cuba",
        "140": "Cyprus",
        "141": "Czech Republic",
        "142": "Denmark",
        "143": "Dominican Republic",
        "144": "Ecuador",
        "145": "Egypt",
        "146": "Egypt",
        "147": "Egypt",
        "148": "El Salvador",
        "149": "Ethiopia",
        "150": "Fiji",
        "151": "Finland",
        "152": "France",
        "153": "France",
        "154": "France",
        "155": "France",
        "156": "France",
        "157": "Gabon",
        "158": "Gambia",
        "159": "Germany",
        "160": "Germany",
        "161": "Germany",
        "162": "Germany",
        "163": "Germany",
        "164": "East Germany",
        "165": "Ghana",
        "166": "Greece",
        "167": "Greece",
        "168": "Grenada",
        "169": "Guinea",
        "170": "Guyana",
        "171": "Haiti",
        "172": "Honduras",
        "173": "Hungary",
        "174": "Iceland",
        "175": "India",
        "176": "India",
        "177": "India",
        "178": "India",
        "179": "India",
        "180": "Indonesia",
        "181": "Iran",
        "182": "Iran",
        "183": "Iraq",
        "184": "Iraq",
        "185": "Ireland",
        "186": "Israel",
        "187": "Israel",
        "188": "Italy",
        "189": "Italy",
        "190": "Italy",
        "191": "Ivory Coast",
        "192": "Jamaica",
        "193": "Japan",
        "194": "Jordan",
        "195": "Jordan",
        "196": "Kenya",
        "197": "South Korea",
        "198": "Kuwait",
        "199": "Laos",
        "200": "Lebanon",
        "201": "Lesotho",
        "202": "Liberia",
        "203": "Libya",
        "204": "Luxembourg",
        "205": "Malawi",
        "206": "Malaysia",
        "207": "Mali",
        "208": "Malta",
        "209": "Mauritania",
        "210": "Mauritius",
        "211": "Mexico",
        "212": "Mongolia",
        "213": "Morocco",
        "214": "Nepal",
        "215": "Netherlands",
        "216": "Netherlands",
        "217": "Netherlands",
        "218": "New Zealand",
        "219": "New Zealand",
        "220": "Nicaragua",
        "221": "Niger",
        "222": "Nigeria",
        "223": "Nigeria",
        "224": "Nigeria",
        "225": "Norway",
        "226": "Oman",
        "227": "Pakistan",
        "228": "Pakistan",
        "229": "Panama",
        "230": "Papua New Guinea",
        "231": "Paraguay",
        "232": "Peru",
        "233": "Philippines",
        "234": "Poland",
        "235": "Portugal",
        "236": "Qatar",
        "237": "Romania",
        "238": "Rwanda",
        "239": "Saudi Arabia",
        "240": "Saudi Arabia",
        "241": "Senegal",
        "242": "Seychelles",
        "243": "Sierra Leone",
        "244": "Singapore",
        "245": "Somalia",
        "246": "South Africa",
        "247": "South Africa",
        "248": "Russia (originally Soviet Union)",
        "249": "Russia (originally Soviet Union)",
        "250": "Russia (originally Soviet Union)",
        "251": "Russia (originally Soviet Union)",
        "252": "Russia (originally Soviet Union)",
        "253": "Spain",
        "254": "Spain",
        "255": "Spain",
        "256": "Sri Lanka",
        "257": "Sudan",
        "258": "Eswatini",
        "259": "Sweden",
        "260": "Switzerland",
        "261": "Syria",
        "262": "Tanzania",
        "263": "Thailand",
        "264": "Togo",
        "265": "Tonga",
        "266": "Trinidad and Tobago",
        "267": "Tunisia",
        "268": "Turkey",
        "269": "United Arab Emirates",
        "270": "United States",
        "271": "United States",
        "272": "United States",
        "273": "United States",
        "274": "United States",
        "275": "Uruguay",
        "276": "Venezuela",
        "277": "Vietnam",
        "278": "Yemen",
        "279": "Yemen",
        "280": "Serbia (originally Yugoslavia)",
        "281": "Democratic Republic of the Congo (formerly Zaire)",
        "282": "Zambia",
        "283": "Dominica",
        "284": "Monaco",
        "285": "Nauru",
        "286": "Saint Lucia",
        "287": "Uganda",
        "288": "Burkina Faso",
        "289": "Saint Vincent and the Grenadines",
        "290": "Zimbabwe",
        "291": "Vatican City",
        "292": "East Caribbean",
        "293": "Belize",
        "294": "Brunei",
        "295": "Antigua and Barbuda",
        "296": "Angola",
        "297": "Guatemala",
        "298": "Mozambique",
        "299": "Namibia",
        "300": "Lithuania",
        "301": "Armenia",
        "302": "Slovenia",
        "303": "Latvia",
        "304": "Estonia",
        "305": "Croatia",
        "306": "Ukraine",
        "307": "Slovakia",
        "308": "Belarus",
        "309": "Albania",
        "310": "Azerbaijan",
        "311": "North Macedonia",
        "312": "Bosnia and Herzegovina",
        "313": "Uzbekistan",
        "314": "Eritrea",
        "315": "Kazakhstan",
        "316": "Georgia",
        "317": "Maldives",
        "318": "Turkmenistan",
        "319": "Kyrgyzstan",
        "320": "Saint Kitts and Nevis",
        "321": "Montenegro",
        "324": "San Marino",
        "328": "South Sudan",
        "330": "Kosovo",
        "350": "May be used by any embassy for security reasons",
        "351": "May be used by any embassy for security reasons",
        "352": "May be used by any embassy for security reasons",
        "353": "May be used by any embassy for security reasons",
        "354": "May be used by any embassy for security reasons",
        "355": "May be used by any embassy for security reasons",
        "356": "May be used by any embassy for security reasons",
        "357": "May be used by any embassy for security reasons",
        "358": "May be used by any embassy for security reasons",
        "359": "May be used by any embassy for security reasons",
        "360": "May be used by any embassy for security reasons",
        "361": "May be used by any embassy for security reasons",
        "362": "May be used by any embassy for security reasons",
        "363": "May be used by any embassy for security reasons",
        "364": "May be used by any embassy for security reasons",
        "365": "May be used by any embassy for security reasons",
        "366": "May be used by any embassy for security reasons",
        "367": "May be used by any embassy for security reasons",
        "368": "May be used by any embassy for security reasons",
        "369": "May be used by any embassy for security reasons",
        "370": "May be used by any embassy for security reasons",
        "371": "May be used by any embassy for security reasons",
        "372": "May be used by any embassy for security reasons",
        "373": "May be used by any embassy for security reasons",
        "374": "May be used by any embassy for security reasons",
        "375": "May be used by any embassy for security reasons",
        "376": "May be used by any embassy for security reasons",
        "377": "May be used by any embassy for security reasons",
        "378": "May be used by any embassy for security reasons",
        "379": "May be used by any embassy for security reasons",
        "380": "May be used by any embassy for security reasons",
        "381": "May be used by any embassy for security reasons",
        "382": "May be used by any embassy for security reasons",
        "383": "May be used by any embassy for security reasons",
        "384": "May be used by any embassy for security reasons",
        "385": "May be used by any embassy for security reasons",
        "386": "May be used by any embassy for security reasons",
        "387": "May be used by any embassy for security reasons",
        "388": "May be used by any embassy for security reasons",
        "389": "May be used by any embassy for security reasons",
        "390": "May be used by any embassy for security reasons",
        "391": "May be used by any embassy for security reasons",
        "392": "May be used by any embassy for security reasons",
        "393": "May be used by any embassy for security reasons",
        "394": "May be used by any embassy for security reasons",
        "395": "May be used by any embassy for security reasons",
        "396": "May be used by any embassy for security reasons",
        "397": "May be used by any embassy for security reasons",
        "398": "May be used by any embassy for security reasons",
        "399": "May be used by any embassy for security reasons",
        "600": "May be used by visiting royalty on official vehicles",
        "601": "May be used by visiting royalty on official vehicles",
        "602": "May be used by visiting royalty on official vehicles",
        "603": "May be used by visiting royalty on official vehicles",
        "604": "May be used by visiting royalty on official vehicles",
        "605": "May be used by visiting royalty on official vehicles",
        "606": "May be used by visiting royalty on official vehicles",
        "607": "May be used by visiting royalty on official vehicles",
        "608": "May be used by visiting royalty on official vehicles",
        "609": "May be used by visiting royalty on official vehicles",
        "610": "May be used by visiting royalty on official vehicles",
        "611": "May be used by visiting royalty on official vehicles",
        "612": "May be used by visiting royalty on official vehicles",
        "613": "May be used by visiting royalty on official vehicles",
        "614": "May be used by visiting royalty on official vehicles",
        "615": "May be used by visiting royalty on official vehicles",
        "616": "May be used by visiting royalty on official vehicles",
        "617": "May be used by visiting royalty on official vehicles",
        "618": "May be used by visiting royalty on official vehicles",
        "619": "May be used by visiting royalty on official vehicles",
        "620": "May be used by visiting royalty on official vehicles",
        "621": "May be used by visiting royalty on official vehicles",
        "622": "May be used by visiting royalty on official vehicles",
        "623": "May be used by visiting royalty on official vehicles",
        "624": "May be used by visiting royalty on official vehicles",
        "625": "May be used by visiting royalty on official vehicles",
        "626": "May be used by visiting royalty on official vehicles",
        "627": "May be used by visiting royalty on official vehicles",
        "628": "May be used by visiting royalty on official vehicles",
        "629": "May be used by visiting royalty on official vehicles",
        "630": "May be used by visiting royalty on official vehicles",
        "631": "May be used by visiting royalty on official vehicles",
        "632": "May be used by visiting royalty on official vehicles",
        "633": "May be used by visiting royalty on official vehicles",
        "634": "May be used by visiting royalty on official vehicles",
        "635": "May be used by visiting royalty on official vehicles",
        "636": "May be used by visiting royalty on official vehicles",
        "637": "May be used by visiting royalty on official vehicles",
        "638": "May be used by visiting royalty on official vehicles",
        "639": "May be used by visiting royalty on official vehicles",
        "640": "May be used by visiting royalty on official vehicles",
        "641": "May be used by visiting royalty on official vehicles",
        "642": "May be used by visiting royalty on official vehicles",
        "643": "May be used by visiting royalty on official vehicles",
        "644": "May be used by visiting royalty on official vehicles",
        "645": "May be used by visiting royalty on official vehicles",
        "646": "May be used by visiting royalty on official vehicles",
        "647": "May be used by visiting royalty on official vehicles",
        "648": "May be used by visiting royalty on official vehicles",
        "649": "May be used by visiting royalty on official vehicles",
        "900": "Commonwealth Secretariat",
        "901": "Council of Europe European Commission",
        "902": "Council of Europe Council of Europe",
        "903": "European Centre for Medium-Range Weather Forecasts",
        "904": "North-East Atlantic Fisheries Commission",
        "905": "Council of Europe European Parliament",
        "906": "Inter-American Development Bank",
        "907": "International Maritime Organization",
        "908": "International Cocoa Organization",
        "909": "International Coffee Organization",
        "910": "International Finance Corporation",
        "911": "International Labour Organization",
        "912": "International Sugar Organization",
        "913": "European Police College",
        "914": "International Whaling Commission",
        "915": "International Wheat Council",
        "916": "NATO North Atlantic Treaty Organization",
        "917": "United Nations",
        "918": "Western European Union",
        "919": "World Health Organization",
        "920": "Eastern Caribbean Commission",
        "921": "Joint European Torus",
        "922": "International Oil Pollution Compensation Fund",
        "923": "International Maritime Satellite Organisation",
        "924": "Commonwealth Foundation",
        "925": "International Maritime Organization (Permanent Representative)",
        "926": "Commonwealth Telecommunications Bureau",
        "927": "United Nations High Commissioner for Refugees",
        "928": "Commonwealth Agricultural Bureaux",
        "929": "International Lead and Zinc Corporation",
        "931": "Joint European Torus",
        "932": "North Atlantic Salmon Conservation Organization",
        "933": "European Investment Bank",
        "934": "European Telecommunications Satellite Organisation",
        "935": "European School (Oxford)",
        "936": "African Development Bank",
        "937": "European Bank for Reconstruction and Development",
        "938": "European Bank for Reconstruction and Development",
        "940": "European Bioinformatics Institute",
        "941": "European Medicines Agency",
        "943": "Oslo and Paris Commissions",
        "944": "European Banking Authority"
    }
    if locationCode in diplomatLocations:
        return diplomatLocations[locationCode]
    else:
        return "Unknown Location"

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
            print("Asher's Gandads car\nCustom")
            
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
            
        elif count[3] == "D" or count[3] =="X" or count[3] == "d" or count[3] == "x" and alphabet(4,6) == 0:
            diplomatOne = str(count[0] + count[1] + count[2])
            diplomatTwo = int(count[4] + count[5] + count[6])

            print(diplomatOne)
            print(diplomatTwo)

            if diplomatTwo >= 101 and diplomatTwo <= 399:
                print("Diplomat acording to the 101 - 399")
            elif diplomatTwo >= 400 and diplomatTwo <= 699:
                print("non-diplomatic staff of international organisations")
            elif diplomatTwo >= 700:
                print("consular or other non-diplomatic staff")
                
            locationDiplomatPrint = diplomatLocation(diplomatOne)
            print(f"Location of licensing for diplomat related vehicle: {locationDiplomatPrint}")
            
            if count[3] =="D" or count[3] == "d":
                print("diplomatic staff within london?")
            elif count[3] =="X" or count[3] == "x":
                print("Non-diplomatic accredited personnel / outside of London?")
            
            
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

