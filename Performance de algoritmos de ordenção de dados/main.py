import timeit
import copy
from Bubble import bubble_sort
from Selection import selection_sort
from Insertion import insertion_sort

if __name__ == '__main__':

    arquivos = ['10k_20%_desordenado.csv','10k_50%_desordenado.csv','10k_100%_desordenado.csv','10k_100%_ordenado.csv',
                '20k_20%_desordenado.csv','20k_50%_desordenado.csv','20k_100%_desordenado.csv','20k_100%_ordenado.csv',
                '30k_20%_desordenado.csv','30k_50%_desordenado.csv','30k_100%_desordenado.csv','30k_100%_ordenado.csv']
 
    
    for arquivo in arquivos:
        arrayValores = []
        ref_arquivo = open("APS/arquivos/"+str(arquivo),"r")
        for linha in ref_arquivo:
            valores = linha.split(";")
            if valores[0] == "nomeImagem":
                continue
            arrayValores.append(int(valores[2].replace("\n","")))
        ref_arquivo.close()

        arrayInsertion = copy.copy(arrayValores)
        arrayBubble = copy.copy(arrayValores)
        arraySelection = copy.copy(arrayValores)

        print(f"\nMétodo Bubble_sort: {arquivo}")
        ini = timeit.default_timer()
        bubble_sort(arrayBubble)
        fim = timeit.default_timer()
        print(f"Levou {fim-ini:.4f}")
        print("=" * 20)
        
        
        print(f"Método Selection_sort: {arquivo}")
        ini = timeit.default_timer()
        selection_sort(arraySelection)
        fim = timeit.default_timer()
        print(f"Levou {fim-ini:.4f}")
        print("=" * 20)
        
        
        
        print(f"Método Insertion_sort {arquivo}")
        ini = timeit.default_timer()
        insertion_sort(arrayInsertion)
        fim = timeit.default_timer()
        print(f"Levou {fim-ini:.4f}")
        print("=" * 20)
    

        arrayInsertion.clear()
        arrayBubble.clear()
        arraySelection.clear()
        arrayValores.clear()
        print("=" * 80)

        
        

