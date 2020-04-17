def levenshtein_distance(palavra1,palavra2):
  tamanho1 = len(palavra1)
  tamanho2 = len(palavra2)
  matrix =  [[ 0 for elemento1 in range(tamanho1 + 1) ] for elemento2 in range(tamanho2 + 1) ]
  for elemento1 in range(1 , tamanho1+1):
    matrix[0][elemento1] = elemento1
  for elemento2 in range(1 , tamanho2+1):
    matrix[elemento2][0] = elemento2
  for elemento2 in range(1, tamanho2 + 1):
        for elemento1 in range(1, tamanho1 + 1):
            if (palavra1[elemento1-1] == palavra2[elemento2-1]):
              valor = 0
            else :
              valor = 1
            result = min( matrix[elemento2-1][elemento1] + 1,
                        matrix[elemento2][elemento1-1] + 1,
                        matrix[elemento2-1][elemento1-1] + valor )
            matrix[elemento2][elemento1] = result
  return matrix[tamanho2][tamanho1]

print(levenshtein_distance('boiaou','boi'))
print(levenshtein_distance('boi','boia'))
print(levenshtein_distance('booy','boy'))