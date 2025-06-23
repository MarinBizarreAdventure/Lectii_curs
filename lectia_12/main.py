print("🎭 COMBINAREA *ARGS ȘI **KWARGS")
print("=" * 40)

def functie_universala(primul_argument, *args, optiune_default="standard", **kwargs):
    """
    Demonstrează combinarea tuturor tipurilor de parametri
    
    Ordinea OBLIGATORIE:
    1. Parametri pozitionali obligatorii
    2. *args (parametri pozitionali variabili)
    3. Parametri cu cuvinte cheie cu valori implicite
    4. **kwargs (parametri cu cuvinte cheie variabili)
    """
    
    rezultat = f"""
🎭 ANALIZĂ COMPLETĂ A ARGUMENTELOR
{'='*45}
Primul argument (obligatoriu): {primul_argument}
Opțiune default: {optiune_default}

Argumente poziționale suplimentare (*args):
  Tip: {type(args)}
  Valori: {args}
  Numărul: {len(args)}

Argumente cu cuvinte cheie (**kwargs):
  Tip: {type(kwargs)}
  Numărul: {len(kwargs)}
"""
    
    if kwargs:
        rezultat += "  Detalii:\n"
        for cheie, valoare in kwargs.items():
            rezultat += f"    {cheie}: {valoare}\n"
    
    return rezultat

# Teste cu diferite combinații
print("📊 TESTE CU DIFERITE COMBINAȚII:")

print("1. Doar argumentul obligatoriu:")
rezultat1 = functie_universala("test1")
print(rezultat1)

print("2. Cu toate tipurile de argumente:")
rezultat2 = functie_universala(
    "test2",                           # argument obligatoriu
    "extra1", "extra2", "extra3",      # *args
    optiune_default="personalizat",    # argument cu cuvânt cheie implicit
    email="test@email.com",            # **kwargs
    varsta=25,
    activ=True
)
print(rezultat2)

# Aplicație practică: Sistem de logging flexibil
def log_mesaj(nivel, mesaj, *detalii_extra, timestamp=None, **metadata):
    """
    Sistem de logging flexibil care acceptă:
    - nivel și mesaj (obligatorii)
    - detalii suplimentare (*args)
    - timestamp opțional
    - metadata variabilă (**kwargs)
    """
    from datetime import datetime
    
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Construim mesajul de log
    log_entry = f"[{timestamp}] {nivel.upper()}: {mesaj}"
    
    # Adăugăm detaliile extra
    if detalii_extra:
        log_entry += f" | Detalii: {', '.join(map(str, detalii_extra))}"
    
    # Adăugăm metadata
    if metadata:
        metadata_str = ', '.join(f"{k}={v}" for k, v in metadata.items())
        log_entry += f" | Metadata: {metadata_str}"
    
    return log_entry

print("📝 SISTEM DE LOGGING FLEXIBIL:")

# Diferite tipuri de log-uri
log1 = log_mesaj("info", "Aplicația a pornit")
print(f"1. {log1}")

log2 = log_mesaj("error", "Eroare de conectare", "timeout după 30s", "retry failed")
print(f"2. {log2}")

log3 = log_mesaj(
    "warning", 
    "Utilizare ridicată a memoriei",
    "RAM: 85%", "SWAP: 60%",
    user_id=12345,
    ip_address="192.168.1.100",
    session_id="abc123"
)
print(f"3. {log3}")

print("\n📋 ORDINEA PARAMETRILOR ÎN PYTHON:")
print("1. Parametri pozționali obligatorii")
print("2. *args (parametri poziționale variabili)")
print("3. Parametri cu cuvinte cheie cu valori implicite")
print("4. **kwargs (parametri cu cuvinte cheie variabili)")
print("\n⚠️ Această ordine este OBLIGATORIE!")