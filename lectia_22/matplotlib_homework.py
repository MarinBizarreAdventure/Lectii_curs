import matplotlib.pyplot as plt
import numpy as np

def create_line_plot():
    """Creează un grafic cu linii"""
    
    # Date simple
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    # TODO 1: Creează figura
    plt.figure(figsize=(8, 6))
    
    # TODO 2: Creează plot-ul cu linii
    plt.plot(x, y, color='blue', marker='o', linewidth=2, markersize=8)
    
    # TODO 3: Adaugă titlu, labels și grid
    plt.title('Grafic cu Linii', fontsize=16, fontweight='bold')
    plt.xlabel('Axa X', fontsize=12)
    plt.ylabel('Axa Y', fontsize=12)
    plt.grid(True)
    
    # TODO 4: Salvează și afișează graficul
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_bar_plot():
    """Creează un grafic cu bare"""
    
    # Date simple
    categories = ['A', 'B', 'C', 'D']
    values = [15, 25, 30, 20]
    
    # TODO 1: Creează figura
    plt.figure(figsize=(8, 6))
    
    # TODO 2: Creează plot-ul cu bare
    plt.bar(categories, values, color=['red', 'green', 'blue', 'orange'], alpha=0.7)
    
    # TODO 3: Adaugă titlu, labels și grid
    plt.title('Grafic cu Bare', fontsize=16, fontweight='bold')
    plt.xlabel('Categorii', fontsize=12)
    plt.ylabel('Valori', fontsize=12)
    plt.grid(True, axis='y', alpha=0.3)
    
    # TODO 4: Salvează și afișează
    plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_scatter_plot():
    """Creează un grafic cu puncte"""
    
    # Date aleatorii
    x = np.random.randn(50)
    y = np.random.randn(50)
    
    # TODO 1: Creează figura
    plt.figure(figsize=(8, 6))
    
    # TODO 2: Creează plot-ul cu puncte
    plt.scatter(x, y, c='purple', alpha=0.6, s=100)
    
    # TODO 3: Adaugă titlu, labels și grid
    plt.title('Grafic cu Puncte', fontsize=16, fontweight='bold')
    plt.xlabel('Axa X', fontsize=12)
    plt.ylabel('Axa Y', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # TODO 4: Salvează și afișează
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_subplot():
    """Creează subplot cu toate graficele împreună"""
    
    # TODO 1: Creează figura cu subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # TODO 2: Subplot 1 (sus-stânga): Grafic cu linii
    axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3], 'bo-')
    axes[0, 0].set_title('Linii')
    axes[0, 0].grid(True)
    
    # TODO 3: Subplot 2 (sus-dreapta): Grafic cu bare
    axes[0, 1].bar(['X', 'Y', 'Z'], [10, 20, 15], color='green')
    axes[0, 1].set_title('Bare')
    axes[0, 1].grid(True)
    
    # TODO 4: Subplot 3 (jos-stânga): Grafic cu puncte
    axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4], color='red', s=100)
    axes[1, 0].set_title('Puncte')
    axes[1, 0].grid(True)
    
    # TODO 5: Subplot 4 (jos-dreapta): Pie chart
    axes[1, 1].pie([30, 25, 20, 25], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
    axes[1, 1].set_title('Pie Chart')
    
    # TODO 6: Ajustează layout-ul
    plt.tight_layout()
    
    # TODO 7: Salvează și afișează
    plt.savefig('subplot.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Funcția principală"""
    
    print("📊 Matplotlib Demo")
    print("=" * 20)
    
    print("Creez grafic cu linii...")
    create_line_plot()
    
    print("Creez grafic cu bare...")
    create_bar_plot()
    
    print("Creez grafic cu puncte...")
    create_scatter_plot()
    
    print("Creez subplot...")
    create_subplot()
    
    print("✅ Toate graficele au fost create!")

if __name__ == "__main__":
    main()