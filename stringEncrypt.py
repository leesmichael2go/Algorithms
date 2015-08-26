#hackerrank encryption algorithm challenge
import math
s = input()
L = len(s)
floor = math.floor(math.sqrt(L))
ceil = math.ceil(math.sqrt(L))
grids = []
for a in range(floor, ceil+1):
    for b in range(a, ceil+1):
        if a*b >= L:
            grids.append([a*b,[a,b]])
grids = sorted(grids)
dims = grids[0][1]
rows = dims[0]
cols = dims[1]

layout = []
s = list(s)
length = len(s)
while length >= cols:
    layout.append(s[0:cols])
    s = s[cols:]
    length -= cols
if length > 0:
    layout.append(s)
if len(layout[rows-1]) < cols:
    blanks = cols - (len(layout[rows-1]) % cols)
    i = 0
    while i < blanks:
        layout[rows-1].append(" ")
        i += 1
        
        
chunks = []
j = 0
while j < cols:
    chunk = []
    i = 0
    while i < rows:
        bit = layout[i][j]
        chunk.append(bit)
        i += 1
    chunks.append(chunk)    
    j += 1
finalChunks = []
for c in chunks:
    c = ''.join(c)
    finalChunks.append(c)
z = 0
while z < len(finalChunks):
    if finalChunks[z][len(finalChunks[z])-1] != " ":
        finalChunks[z] = finalChunks[z] + " "
    z += 1
lastChunk = finalChunks[cols-1]
if lastChunk[len(lastChunk)-1] == " ":
    finalChunks[cols-1] = lastChunk[:-1]
    
print(''.join(finalChunks))
