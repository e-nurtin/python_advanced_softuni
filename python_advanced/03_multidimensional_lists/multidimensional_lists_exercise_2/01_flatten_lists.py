matrix = [[x.strip() for x in row.split()] for row in input().split('|')[::-1]]
print(' '.join([el for row in matrix for el in row]))

