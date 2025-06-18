print("🔄 CODUL FĂRĂ FUNCȚII - REPETITIV ȘI INEFICIENT")
print("=" * 50)

# Fără funcții - cod repetitiv
numar1 = 10
numar2 = 14
numar3 = 3
numar4 = 6

print("Dublul numarului", numar1, "este:", numar1 * 2)
print("Dublul numarului", numar2, "este:", numar2 * 2)
print("Dublul numarului", numar3, "este:", numar3 * 2)
print("Dublul numarului", numar4, "este:", numar4 * 2)

print("\n🚀 CODUL CU FUNCȚII - ELEGANT ȘI EFICIENT")
print("=" * 45)

# Cu funcții - cod optimizat
def printDublu(x):
    print("Dublul numarului", x, "este:", x * 2)

numar1 = 10
numar2 = 14
numar3 = 3
numar4 = 6

printDublu(numar1)
printDublu(numar2)
printDublu(numar3)
printDublu(numar4)

print("\n🎯 CONCLUZIA:")
print("Funcțiile fac codul REUTILIZABIL și UȘOR DE ÎNTREȚINUT!")