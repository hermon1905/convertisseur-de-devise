import streamlit as st 
import requests
import pandas as pd 


# ------------configuration de la page -------------------
st.set_page_config(
    page_title="Convertisseur de Devises",
    page_icon="💸"
)

#api_key = 'ac5a593d3046a9e670eed9c5'

# url = "https://v6.exchangerate-api.com/v6/ac5a593d3046a9e670eed9c5/latest/USD"
# response = requests.get(url)
# data = response.json()

codes_devises = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
    "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
    "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
    "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP",
    "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND",
    "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]


def convertir_devise(montant, from_devise, to_devise):
    url = f"https://v6.exchangerate-api.com/v6/ac5a593d3046a9e670eed9c5/pair/{from_devise}/{to_devise}/{montant}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["result"] == "success":
        taux = data["conversion_rate"]
        resultat = data["conversion_result"]
        return f"{montant} {from_devise} = {resultat:.2f} {to_devise} (Taux: {taux:.4f})"
    else:
        print("Erreur API :", data.get("error-type", "Inconnue"))
        return None



# -------------------integration dans streamlit------------------

st.title(" :blue[Application de conversion de devises]")



# Tableau complet des devises 
data = {
    "Code Devise": [
        "AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN",
        "BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL",
        "BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY",
        "COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP",
        "ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS",
        "GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF",
        "IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD",
        "JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT",
        "LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD",
        "MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN",
        "NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK",
        "PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR",
        "SBD","SCR","SDG","SEK","SGD","SHP","SLE","SOS","SRD","SSP",
        "STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD",
        "TVD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND",
        "VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"
    ],
    "Pays / Territoire": [
        "UAE","Afghanistan","Albania","Armenia","Netherlands Antillean guilder (Curaçao etc.)",
        "Angola","Argentina","Australia (plus Kiribati, Tuvalu, etc.)","Aruba","Azerbaijan",
        "Bosnia & Herzegovina","Barbados","Bangladesh","Bulgaria","Bahrain","Burundi","Bermuda",
        "Brunei","Bolivia","Brazil","Bahamas","Bhutan","Botswana","Belarus","Belize","Canada",
        "DR Congo","Switzerland & Liechtenstein","Chile","China","Colombia","Costa Rica","Cuba",
        "Cabo Verde","Czechia","Djibouti","Denmark & territories","Dominican Republic","Algeria",
        "Egypt","Eritrea","Ethiopia","Euro‑area (ex : France, Germany, etc.)","Fiji","Falkland Is.","Faroe Is.",
        "UK & dependencies (Jersey, Guernsey, Isle‑of‑Man etc.)","Georgia","Guernsey","Ghana","Gibraltar",
        "Gambia","Guinea","Guatemala","Guyana","Hong Kong","Honduras","Croatia","Haiti","Hungary",
        "Indonesia","Israel","Isle of Man (GBP)","India","Iraq","Iran","Iceland","Jersey (GBP)",
        "Jamaica","Jordan","Japan","Kenya","Kyrgyzstan","Cambodia","Kiribati (AUD)","Comoros","South Korea",
        "Kuwait","Cayman Is.","Kazakhstan","Laos","Lebanon","Sri Lanka","Liberia","Lesotho","Libya",
        "Morocco & Western Sahara","Moldova","Madagascar","North Macedonia","Myanmar","Mongolia","Macau",
        "Mauritania","Mauritius","Maldives","Malawi","Mexico","Malaysia","Mozambique","Namibia","Nigeria",
        "Nicaragua","Norway","Nepal","New Zealand & Pacific","Oman","Panama","Peru","Papua New Guinea",
        "Philippines","Pakistan","Poland","Paraguay","Qatar","Romania","Serbia","Russia","Rwanda",
        "Saudi Arabia","Solomon Is.","Seychelles","Sudan","Sweden","Singapore","Saint Helena","Sierra Leone",
        "Somalia","Suriname","South Sudan","São Tomé & Príncipe","Syria","Eswatini","Thailand","Tajikistan",
        "Turkmenistan","Tunisia","Tonga","Turkey","Trinidad & Tobago","Tuvalu (AUD)","Taiwan","Tanzania",
        "Ukraine","Uganda","USA & territories","Uruguay","Uzbekistan","Venezuela","Vietnam","Vanuatu",
        "Samoa","Central African CFA (Cameroon, Gabon, etc.)","East Caribbean Dollar (XCD: Antigua…)",
        "SDR (FMI)","West African CFA (XOF: Ivory Coast, Côte d’Ivoire…)","CFP Franc (XPF: French Pacific)",
        "Yemen","South Africa","Zambia","Zimbabwe"
    ]
}


# Convertir en DataFrame
df_devises = pd.DataFrame(data)


# ------------------info a remplir -------------------------

col1, col2, col3 = st.columns(3)

with col1 :
    montant = st.number_input("Entrez le montant", min_value=0, max_value=None, step=10, value=None)

with col2 : 
    from_devise = st.selectbox("devise source", codes_devises)

with col3 : 
    to_devise = st.selectbox("devise cible", codes_devises)

if st.button("convertir"):
    st.success(convertir_devise(montant, from_devise, to_devise))


st.info("toutes les devises prises en charge par l'application sont dans le tableau ci-dessous .")
st.dataframe(df_devises)