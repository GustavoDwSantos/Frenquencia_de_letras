from collections import Counter
import matplotlib.pyplot as plt
from limpar_string import limpa_string

def main():
    with open ('./livros/nietzsche.txt') as file:
        texto_1 = file.read().lower()

    with open ('./livros/spinoza.txt') as file:
        texto_2 = file.read().lower()

      
    print (f'{len(texto_1)} Caracteres carregados antes de formatar o texto!')
    texto_formatado_1 = limpa_string(texto_1)
    print (f'{len(texto_formatado_1)} Letras carregadas pos formatar texto')    
    texto_formatado_2 = limpa_string(texto_2)

    frequencia_letras_1 = Counter(texto_formatado_1) 
    frequencia_letras_2 = Counter(texto_formatado_2)

    letra_1,qtde_1 = zip(*frequencia_letras_1.most_common(15))
    letra_2,qtde_2 = zip(*frequencia_letras_2.most_common(15))

    width = 0.4

    plt.figure(figsize = ((12, 6)))
    
    plt.subplot(2,2,1)
    bar_1 = plt.bar(letra_1,qtde_1,width=width, color= 'r', label = "Alemão")
    plt.title("Frequncia de letras 'Assim Falou Zaratustra' Em Alemão")
    
    plt.subplot(2,2,2)
    bar_2 = plt.bar(letra_2,qtde_2,width=width, color= 'b', label = "Holandes")
    plt.title("Frequncia de letras 'Etica' Em Holandes")
    plt.show()


if __name__ == "__main__":
    main()