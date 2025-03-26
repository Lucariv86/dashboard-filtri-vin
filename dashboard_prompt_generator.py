import streamlit as st

# Titolo
st.title("Generatore di Prompt per Ricerca Filtri da VIN")

# Input VIN e marca
vin = st.text_input("Inserisci il VIN del veicolo")
marca = st.selectbox("Seleziona la marca", ["Toyota", "Fiat (in arrivo)", "Renault (in arrivo)", "Altro (non supportato)"])

# Funzione per generare il prompt per Toyota
def prompt_toyota(vin):
    return f"""
Riceverai in input un codice VIN di un veicolo Toyota.

Accedi al sito https://partsouq.com, incolla il VIN nella barra di ricerca e apri il relativo catalogo ricambi.

Dovrai cercare tre filtri in tre sezioni specifiche del catalogo. Riporta **tutti i risultati trovati** per ogni filtro. Non fare scelte, non riassumere. Riporta anche codici simili, duplicati o alternative.

Per ciascun risultato mostra:
- Nome parte
- Codice parte
- Descrizione (se presente)
- Link diretto alla parte (se disponibile)

---

1. **Filtro olio**
   - Vai alla pagina `1502: OIL FILTER`
   - Cerca tutte le voci che includono: **Filter Sub-assy Oil**

2. **Filtro aria**
   - Vai alla pagina `1703: AIR CLEANER`
   - Cerca tutte le voci che includono: **Element Sub-assy Air Cleaner Filter**

3. **Filtro abitacolo**
   - Usa la funzione di ricerca: clicca su **SEARCH** accanto a "CATEGORIES"
   - Scrivi: **FILTER, CLEAN AIR**
   - Esegui la ricerca nel catalogo corrispondente al VIN
   - Leggi **tutti i risultati** che compaiono. Non saltare quelli con nomi simili.
   - Cerca di includere anche risultati che potrebbero avere variazioni nel nome tipo:
     - Filter, CleanAir
     - Air Filter (Cabin)
     - Filter Sub-Assy Air Conditioner
   - Mostra ogni risultato su una riga separata.

---

**Formato output:**
```
[MARCHIO]: Toyota

[FILTRO OLIO]
1. Codice: XXXX | Nome: ... | Descrizione: ... | Link: ...

[FILTRO ARIA]
...

[FILTRO ABITACOLO]
...
```

VIN di input:
```
{vin}
```
"""

# Generazione del prompt
if vin and marca == "Toyota":
    st.subheader("Prompt generato")
    st.code(prompt_toyota(vin), language="markdown")
elif vin and "in arrivo" in marca:
    st.warning("Il supporto per questa marca verrà aggiunto a breve.")
elif vin and marca == "Altro (non supportato)":
    st.error("Marca non supportata al momento.")