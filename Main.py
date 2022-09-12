from collections import Counter
import matplotlib.pyplot as plt
from limpar_string import limpa_string


def main():
    with open ('./livros/nietzsche.txt') as file:
        texto = file.read().lower()
        
    print (f'{len(texto)} Caracteres carregados antes de formatar o texto!')
    texto_formatado = limpa_string(texto)
    print (f'{len(texto_formatado)} Letras carregadas pos formatar texto')    
    
    frequencia_letras = Counter(texto_formatado) 
    
    letra,qtde = zip(*frequencia_letras.most_common(15))
    plt.title("Frequncia de letras 'Assim Falou Zaratustra' Em Alemão")
    plt.bar(letra, qtde)
    plt.show()


if __name__ == "__main__":
    main()