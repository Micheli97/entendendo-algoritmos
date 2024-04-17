grafo = {} 
grafo['inicio'] = {}
grafo['inicio']['a'] = 5 
grafo['inicio']['b'] =  2

grafo['a'] = { }
grafo['a']['c'] = 4 
grafo['a']['d'] = 2 

grafo['b'] = {}
grafo['b']['a'] = 8  
grafo['b']['d'] = 7 

grafo['c'] = {}
grafo['c']['d'] = 6  
grafo['c']['fim'] = 3

grafo['d'] = {}
grafo['d']['fim'] = 1

grafo ['fim'] ={} 
  
  
infinito=float('inf')
custos ={}
custos['a']=5
custos['b']=2
custos['c'] = infinito
custos['d'] = infinito
custos['fim']=infinito

pais={}
pais['a']='inicio'
pais['b']='inicio'
pais['c'] = 'a'
pais['d'] = None
pais['fim']=None

processados=[]

def ache_no_custo_mais_baixo(custos):
    custos_mais_baixo =float('inf')
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custos_mais_baixo and nodo not in processados:
            custos_mais_baixo = custo 
            nodo_custo_mais_baixo = nodo
            
    return nodo_custo_mais_baixo

nodo=ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo 
            pais[n] = nodo 
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print(custos)