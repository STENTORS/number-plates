import pandas as pd

data = {
    'Number': [],
    'Country or Organisation': []
}

import pandas as pd

data = {
    "Number": list(range(101, 293)) + list(range(294, 326)) + list(range(328, 331)) + list(range(350, 400)) + [600] + list(range(601, 650)) + [900] + list(range(901, 939)),
    "Country or Organisation": [
        "Afghanistan (Islamic Republic)", "Algeria", "Argentina", "Australia", "Australia", "Australia", "Australia", "Australia", "Australia",
        "Austria", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", "Benin", "Bolivia", "Botswana", "Brazil", "Brazil", "Brazil", "Brazil", "Brazil",
        "Bulgaria", "Myanmar (formerly Burma)", "Burundi", "Cameroon", "Canada", "Canada", "Canada", "Canada", "Canada",
        "Central African Republic", "Chad", "Chile", "China ", "Colombia", "Republic of the Congo", "Costa Rica", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic",
        "Ecuador", "Egypt", "Egypt", "Egypt", "El Salvador", "Ethiopia", "Fiji", "Finland", "France", "France", "France", "France", "France",
        "Gabon", "Gambia", "Germany", "Germany", "Germany", "Germany", "Germany", "Ghana", "Greece", "Greece", "Grenada", "Guinea",
        "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "India", "India", "India", "India",
        "Indonesia", "Iran", "Iran", "Iraq", "Iraq", "Ireland", "Israel", "Israel", "Italy", "Italy", "Italy",
        "Ivory Coast", "Jamaica", "Japan", "Jordan", "Jordan", "Kenya", "South Korea", "Kuwait", "Laos", "Lebanon",
        "Lesotho", "Liberia", "Libya", "Luxembourg", "Malawi", "Malaysia", "Mali", "Malta", "Mauritania", "Mauritius",
        "Mexico", "Mongolia", "Morocco", "Nepal", "Nepal", "Netherlands", "Netherlands", "Netherlands", "New Zealand", "New Zealand",
        "Nicaragua", "Niger", "Nigeria", "Nigeria", "Nigeria", "Norway", "Oman", "Pakistan", "Pakistan", "Panama",
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Rwanda", "Saudi Arabia",
        "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Somalia", "South Africa", "South Africa", "Russia",
        "Russia", "Russia", "Russia", "Russia", "Spain", "Spain", "Spain", "Sri Lanka", "Sudan", "Eswatini", "Sweden",
        "Switzerland", "Syria", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "United Arab Emirates",
        "United Arab Emirates", "United States", "United States", "United States", "United States", "United States", "Uruguay", "Venezuela", "Vietnam",
        "Vietnam", "Yemen", "Yemen", "Serbia", "Democratic Republic of the Congo", "Zambia", "Dominica", "Monaco", "Nauru",
        "Saint Lucia", "Uganda", "Burkina Faso", "Saint Vincent and the Grenadines", "Zimbabwe", "Vatican City", "East Caribbean",
        "Belize", "Brunei", "Antigua and Barbuda", "Angola", "Guatemala", "Mozambique", "Namibia", "Lithuania", "Armenia",
        "Slovenia", "Latvia", "Estonia", "Croatia", "Ukraine", "Slovakia", "Belarus", "Albania", "Azerbaijan", "North Macedonia",
        "Bosnia and Herzegovina", "Uzbekistan", "Eritrea", "Kazakhstan", "Georgia", "Maldives", "Turkmenistan", "Kyrgyzstan", "Saint Kitts and Nevis",
        "Montenegro", "San Marino", "South Sudan", "Kosovo", "May be used by any embassy for security reasons", "May be used by any embassy for security reasons",
        "May be used by any embassy for security reasons", "May be used by any embassy for security reasons", "May be used by any embassy for security reasons",
        "May be used by visiting royalty on official vehicles", "May be used by visiting royalty on official vehicles", "May be used by visiting royalty on official vehicles",
        "May be used by visiting royalty on official vehicles", "May be used by visiting royalty on official vehicles", "Commonwealth Secretariat",
        "Council of Europe European Commission", "Council of Europe Council of Europe", "European Centre for Medium-Range Weather Forecasts", "North-East Atlantic Fisheries Commission",
        "Council of Europe European Parliament", "Inter-American Development Bank", "International Maritime Organization", "International Cocoa Organization", "International Coffee Organization",
        "International Finance Corporation", "International Labour Organization", "International Sugar Organization", "European Police College", "International Whaling Commission",
        "International Wheat Council", "NATO North Atlantic Treaty Organization", "United Nations", "Western European Union", "World Health Organization", "Eastern Caribbean Commission",
        "Joint European Torus", "International Oil Pollution Compensation Fund", "International Maritime Satellite Organisation", "Commonwealth Foundation", "International Maritime Organization (Permanent Representative)",
        "Commonwealth Telecommunications Bureau", "United Nations High Commissioner for Refugees", "Commonwealth Agricultural Bureaux", "International Lead and Zinc Corporation", "Joint European Torus",
        "North Atlantic Salmon Conservation Organization", "European Investment Bank", "European Telecommunications Satellite Organisation", "European School (Oxford)", "African Development Bank",
        "European Bank for Reconstruction and Development", "European Bank for Reconstruction and Development", "European Bioinformatics Institute", "European Medicines Agency", "Oslo and Paris Commissions",
        "European Banking Authority"
    ]
}


data['Number'].extend(number_data)
data['Country or Organisation'].extend(country_data)

df = pd.DataFrame(data)

df.to_csv('diplomat.csv')
