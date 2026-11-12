s = "abcdefgh"

# estrtura do slicing s[start:stop:step]
print(s[3:6])# -> "def" 
print(s[3:6:2]) # -> "df"

# quando omitimos 'start' e 'stop' o interpretador assume que start = 0 e stop = len(s) - 1
print(s[:]) # -> "abcdefgh"

# ao usar step negativos, tenha cuidado de garantir que start >= stop. 
print(s[::-1]) # -> "hgfedcba"
print(s[4:1:-2]) # -> "ec"

# caso contrário resulta em uma string vazia
print(s[1:4:-2])

new_s = "ABC d3f ghi"

print(new_s[3:len(new_s) - 1])
print(new_s[4:0:-1])

# string vazia, start precisa ser menor que stop quando step é positivo
print(new_s[6:3]) 