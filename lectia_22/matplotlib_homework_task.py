import matplotlib.pyplot as plt
import numpy as np

def create_line_plot():
    """Creează un grafic cu linii"""
    
    # Date simple
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(8,6))
    plt.plot(x,y, color="blue", marker = 'o', linewidth=2, markersize=8)
    plt.title("Grafic cu Linii", fontsize=16)
    plt.xlabel("Axa X",fontsize=12)
    plt.ylabel("Axa Y",fontsize=12)
    plt.grid(True, alpha=0.5)
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_bar_plot():
    """Creează un grafic cu bare"""
    
    # Date simple
    categories = ['A', 'B', 'C', 'D']
    values = [15, 25, 30, 20]
    
    
    plt.figure(figsize=(8,6))
    plt.bar(categories, values, color=['red','blue','green','orange'], alpha=0.7)
    plt.title('Grafic cu Bare')
    plt.xlabel('Categorii')
    plt.ylabel('Valori')
    plt.grid(True,axis='y',alpha=0.3)
 
    plt.savefig("ar_plot.png", dpi=300,bbox_inches='tight')
    plt.show()
    
\
def create_scatter_plot():
    """Creează un grafic cu puncte"""
    
    # Date aleatorii
    x = np.random.randn(50)
    y = np.random.randn(50)
    

    plt.figure(figsize=(8,6))

    plt.scatter(x,y, c='purple', alpha=0.6,s=100)
    plt.title('Grafic cu Puncte')
    plt.xlabel("Axa x")
    plt.ylabel("Axa y")
    
    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - Titlu: 'Grafic cu Puncte'
    # - xlabel: 'Axa X'
    # - ylabel: 'Axa Y'
    # - Grid cu alpha=0.3
    
    # TODO 4: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'scatter_plot.png'
    plt.savefig('scatter_plot.png', dpi=300)
    plt.show()
    

def create_subplot():
    """Creează subplot cu toate graficele împreună"""
    


    fig, axes = plt.subplots(2,2,figsize=(12,10))

    axes[0,0].plot([1,2,3,4],[1,2,3,4],"bo-")
    axes[0,0].set_title("liniii")
    axes[0,0].grid(True)

    axes[0,1].bar(["X","Y","Z"],[10,15,25],color='green')
    axes[0,1].set_title("Bare")
    axes[0,1].grid(True)

    axes[1,0].scatter([1,2,3,4],[2,3,4,1],color='red',s=100)
    axes[1,0].set_title("Puncte")
    axes[1,0].grid(True)

    axes[1,1].pie([30, 25, 20, 25], labels=['A', 'B', 'C', 'D'], autopct="%1.1f%%")
    axes[1, 1].set_title('Pie Chart')
    plt.tight_layout()
    # TODO 6: Ajustează layout-ul
    # INSTRUCȚIUNI: Folosește plt.tight_layout() pentru a ajusta automat spațierea
    # - Acest lucru previne suprapunerea elementelor
    plt.savefig("subplot.png",dpi=300)
    # TODO 7: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'subplot.png'
    # - Folosește aceleași setări ca la celelalte grafice
    plt.show()
    
    pass

def main():
    """Funcția principală"""
    
    print("📊 Matplotlib Demo")
    print("=" * 20)
    
    print("Creez grafic cu linii...")
    # create_line_plot()
    
    print("Creez grafic cu bare...")
    # create_bar_plot()
    
    print("Creez grafic cu puncte...")
    # create_scatter_plot()
    
    print("Creez subplot...")
    create_subplot()
    
    print("✅ Toate graficele au fost create!")

if __name__ == "__main__":
    main()

