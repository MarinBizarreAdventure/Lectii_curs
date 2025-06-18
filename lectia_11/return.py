print("📊 EXERCIȚIUL 2: ANALIZATORUL DE TEXT")
print("=" * 40)

def numara_cuvinte(text):
    """Numără cuvintele dintr-un text"""
    return len(text.split())

def numara_caractere(text, include_spatii=True):
    """Numără caracterele dintr-un text"""
    if include_spatii:
        return len(text)
    else:
        return len(text.replace(' ', ''))

def numara_vocale(text):
    """Numără vocalele dintr-un text"""
    vocale = "aeiouAEIOU"
    return sum(1 for char in text if char in vocale)

def numara_consoane(text):
    """Numără consoanele dintr-un text"""
    return sum(1 for char in text if char.isalpha() and char not in "aeiouAEIOU")

def gaseste_cuvant_cel_mai_lung(text):
    """Găsește cel mai lung cuvânt din text"""
    cuvinte = text.split()
    if not cuvinte:
        return ""
    return max(cuvinte, key=len)

def inverseaza_cuvinte(text):
    """Inversează ordinea cuvintelor în text"""
    return ' '.join(text.split()[::-1])

def analizeaza_text_complet(text):
    """
    Analizează complet un text folosind toate funcțiile de mai sus
    
    Args:
        text: textul de analizat
    
    Returns:
        Dicționar cu toate statisticile
    """
    return {
        'text_original': text,
        'numar_cuvinte': numara_cuvinte(text),
        'numar_caractere_cu_spatii': numara_caractere(text),
        'numar_caractere_fara_spatii': numara_caractere(text, False),
        'numar_vocale': numara_vocale(text),
        'numar_consoane': numara_consoane(text),
        'cuvant_cel_mai_lung': gaseste_cuvant_cel_mai_lung(text),
        'text_inversat': inverseaza_cuvinte(text)
    }

# Testarea analizatorului
text_exemplu = "Python este un limbaj de programare fantastic"
analiza = analizeaza_text_complet(text_exemplu)

print("Analiza completă a textului:")
print(f"Text original: '{analiza['text_original']}'")
print(f"Număr cuvinte: {analiza['numar_cuvinte']}")
print(f"Caractere cu spații: {analiza['numar_caractere_cu_spatii']}")
print(f"Caractere fără spații: {analiza['numar_caractere_fara_spatii']}")
print(f"Vocale: {analiza['numar_vocale']}")
print(f"Consoane: {analiza['numar_consoane']}")
print(f"Cel mai lung cuvânt: '{analiza['cuvant_cel_mai_lung']}'")
print(f"Text cu cuvinte inversate: '{analiza['text_inversat']}'")