import streamlit as st 
import requests

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
        print(f"{montant} {from_devise} = {resultat:.2f} {to_devise} (Taux: {taux:.4f})")
        return resultat
    else:
        print("Erreur API :", data.get("error-type", "Inconnue"))
        return None



# -------------------integration dans streamlit------------------
col1, col2, col3 = st.columns(3)

with col1 :
    montant = st.number_input("Entrez le montant")

with col2 : 
    from_devise = st.selectbox("devise source", codes_devises)

with col3 : 
    to_devise = st.selectbox("devise cible", codes_devises)

if st.button("convertir"):
    st.success(convertir_devise(montant, from_devise, to_devise))