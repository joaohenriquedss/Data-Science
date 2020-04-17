# Distância Levenshtein

Em teoria da informação, a distância Levenshtein ou distância de edição entre dois "strings" (duas sequências de caracteres) é dada pelo número mínimo de operações necessárias para transformar um string no outro. Entendemos por "operações" a inserção, deleção ou substituição de um carácter. O nome advém do cientista russo Vladimir Levenshtein, que considerou esta distância já em 1965. É muito útil para aplicações que precisam determinar quão semelhantes dois strings são, como é por exemplo o caso com os verificadores ortográficos.

### Pseudocódigo
```sh
Função LevenshteinDistance(Caracter : str1[1..lenStr1], Caracter : str2[1..lenStr2]) : INTEIRO
Início
   // tab é uma tabela com lenStr1+1 linhas e lenStr2+1 colunas
   Inteiro:  tab[0..lenStr1, 0..lenStr2]
   // X e Y são usados para iterar str1 e str2
   Inteiro:  X, Y, cost
 
   Para X de 0 até lenStr1
       tab[X, 0] ← X
   Para Y de 0 até lenStr2
       tab[0, Y] ← Y
 
   Para X de 1 até lenStr1
       Para Y de 1 até lenStr2
           Se str1[X] = str2[Y] Então cost ← 0
                                Se-Não cost ← 2 // Custo da substituição deve ser 2, deleção e inserção
           tab[X, Y] := menor(
                                tab[X-1, Y  ] + 1,     // Deletar
                                tab[X  , Y-1] + 1,     // Inserir
                                tab[X-1, Y-1] + cost   // Substituir
                            )
   LevenshteinDistance ← tab[lenStr1, lenStr2]
 Fim
```
