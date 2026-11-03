
total_linhas = 0

divisoes = []
bairros = []
setores = []
quarteiroes = []
ceps = []
num_enderecos = []
metragem_testada = []
l_mt_testada = []
areas_reais = []
l_areas_reais=[]
areas_construidas = []
l_areas_construidas=[]
areas_corrigidas = []
l_areas_corrigidas=[]
valores_terreno = []
l_valores_terreno=[]
valores_construidos = []
l_valores_construidos=[]
valores_imovel=[]
l_valores_imovel=[]
aliquota_iptu=[]
l_aliquota_iptu=[]
valores_iptu = []
l_valores_iptu=[]
valores_tcl=[]
l_valores_tcl=[]

with open ('iptu_2025_fase1.txt','r') as arq:
    for linha in arq:
        
        nova = linha.strip().split('\t')
        divisao=float(nova[0])
        bairro=nova[1]
        setor=float(nova[2])
        quarteirao=float(nova[3])
        cep=float(nova[4])
        num_end=float(nova[5])
        metragem_testada=float(nova[6])
        areas_reais=float(nova[7])
        areas_construidas=float(nova[8])
        areas_corrigidas=float(nova[9])
        valores_terreno=float(nova[10])
        valores_construidos=float(nova[11])
        valores_imovel=float(nova[12])
        aliquota_iptu=float(nova[13])
        valores_iptu=float(nova[14])
        valores_tcl=float(nova[15])

        total_linhas += 1

        divisoes.append(divisao)
        bairros.append(bairro)
        setores.append(setor)
        quarteiroes.append(quarteirao)
        ceps.append(cep)
        num_enderecos.append(num_end)
        l_mt_testada.append(metragem_testada)
        l_areas_reais.append(areas_reais)
        l_areas_construidas.append(areas_construidas)
        l_areas_corrigidas.append(areas_corrigidas)
        l_valores_terreno.append(valores_terreno)
        l_valores_construidos.append(valores_construidos)
        l_valores_imovel.append(valores_imovel)
        l_aliquota_iptu.append(aliquota_iptu)
        l_valores_iptu.append(valores_iptu)
        l_valores_tcl.append(valores_tcl)
        
        #print(f'Divisão: {divisao} | Bairro: {bairro} | Setor: {setor} | Quarteirão: {quarteirao} | CEP: {cep} | Num do Endereço: {num_end} | Metragem Testada: {metragem_testada} | Área Real: {areas_reais} | Área Construída: {areas_construidas} | Área Corrigida: {areas_corrigidas} | Valor do Terreno: {valores_terreno} | Valor das Construções: {valores_construidos} | Valor do Imóvel: {valores_imovel} | Alíquota do IPTU: {aliquota_iptu} | Valor do IPTU: {valores_iptu} | Valor do TCL: {valores_tcl}')

media_num_endereco = sum(num_enderecos) / len(num_enderecos)
minimo_area_testada = min(l_mt_testada)
maximo_area_testada = max(l_mt_testada)
media_area_testada = sum(l_mt_testada) / len(l_mt_testada)
minimo_area_real = min(l_areas_reais)
maximo_area_real = max(l_areas_reais)
media_area_real = sum(l_areas_reais) / len(l_areas_reais)
minimo_area_construida = min(l_areas_construidas)
maximo_area_construida = max(l_areas_construidas)
media_area_construida = sum(l_areas_construidas) / len(l_areas_construidas)
minimo_area_corrigida = min(l_areas_corrigidas)
maximo_area_corrigida = max(l_areas_corrigidas)
media_area_corrigida = sum(l_areas_corrigidas) / len(l_areas_corrigidas)
minimo_valor_terreno = min(l_valores_terreno)
maximo_valor_terreno = max(l_valores_terreno)
media_valor_terreno = sum(l_valores_terreno) / len(l_valores_terreno)
minimo_valor_construido = min(l_valores_construidos)
maximo_valor_construido = max(l_valores_construidos)
media_valor_construido = sum(l_valores_construidos) / len(l_valores_construidos)
minimo_valor_imovel = min(l_valores_imovel)
maximo_valor_imovel = max(l_valores_imovel)
media_valor_imovel = sum(l_valores_imovel) / len(l_valores_imovel)
minimo_aliquota_iptu = min(l_aliquota_iptu)
maximo_aliquota_iptu = max(l_aliquota_iptu) 
media_aliquota_iptu = sum(l_aliquota_iptu) / len(l_aliquota_iptu)
minimo_valor_iptu = min(l_valores_iptu)
maximo_valor_iptu = max(l_valores_iptu)
media_valor_iptu = sum(l_valores_iptu) / len(l_valores_iptu)
minimo_valor_tcl = min(l_valores_tcl)
maximo_valor_tcl = max(l_valores_tcl)
media_valor_tcl = sum(l_valores_tcl) / len(l_valores_tcl)


ordenados_area_testada = sorted(l_mt_testada)
n = len(ordenados_area_testada)
if n % 2 == 1:
    mediana_area_testada = ordenados_area_testada[n // 2]
else:
    mediana_area_testada = (ordenados_area_testada[n // 2 - 1] + ordenados_area_testada[n // 2]) / 2

ordenados_area_real = sorted(l_areas_reais)
n = len(ordenados_area_real)
if n % 2 == 1:
    mediana_area_real = ordenados_area_real[n // 2]
else:
    mediana_area_real = (ordenados_area_real[n // 2 - 1] + ordenados_area_real[n // 2]) / 2

ordenados_area_construida = sorted(l_areas_construidas)
n = len(ordenados_area_construida)
if n % 2 == 1:
    mediana_area_construida = ordenados_area_construida[n // 2]
else:
    mediana_area_construida = (ordenados_area_construida[n // 2 - 1] + ordenados_area_construida[n // 2]) / 2

ordenados_area_corrigida = sorted(l_areas_corrigidas)
n = len(ordenados_area_corrigida)
if n % 2 == 1:
    mediana_area_corrigida = ordenados_area_corrigida[n // 2]
else:
    mediana_area_corrigida = (ordenados_area_corrigida[n // 2 - 1] + ordenados_area_corrigida[n // 2]) / 2

ordenados_valor_terreno = sorted(l_valores_terreno)
n = len(ordenados_valor_terreno)
if n % 2 == 1:
    mediana_valor_terreno = ordenados_valor_terreno[n // 2]
else:
    mediana_valor_terreno = (ordenados_valor_terreno[n // 2 - 1] + ordenados_valor_terreno[n // 2]) / 2

ordenados_valor_construido = sorted(l_valores_construidos)
n = len(ordenados_valor_construido)
if n % 2 == 1:
    mediana_valor_construido = ordenados_valor_construido[n // 2]
else:
    mediana_valor_construido = (ordenados_valor_construido[n // 2 - 1] + ordenados_valor_construido[n // 2]) / 2

ordenados_valor_imovel = sorted(l_valores_imovel)
n = len(ordenados_valor_imovel)
if n % 2 == 1:
    mediana_valor_imovel = ordenados_valor_imovel[n // 2]
else:
    mediana_valor_imovel = (ordenados_valor_imovel[n // 2 - 1] + ordenados_valor_imovel[n // 2]) / 2

ordenados_aliquota_iptu = sorted(l_aliquota_iptu)
n = len(ordenados_aliquota_iptu)
if n % 2 == 1:
    mediana_aliquota_iptu = ordenados_aliquota_iptu[n // 2]
else:
    mediana_aliquota_iptu = (ordenados_aliquota_iptu[n // 2 - 1] + ordenados_aliquota_iptu[n // 2]) / 2

ordenados_valor_iptu = sorted(l_valores_iptu)
n = len(ordenados_valor_iptu)
if n % 2 == 1:
    mediana_valor_iptu = ordenados_valor_iptu[n // 2]
else:
    mediana_valor_iptu = (ordenados_valor_iptu[n // 2 - 1] + ordenados_valor_iptu[n // 2]) / 2

ordenados_valor_tcl = sorted(l_valores_tcl)
n = len(ordenados_valor_tcl)
if n % 2 == 1:
    mediana_valor_tcl = ordenados_valor_tcl[n // 2]
else:
    mediana_valor_tcl = (ordenados_valor_tcl[n // 2 - 1] + ordenados_valor_tcl[n // 2]) / 2

soma_areas_testadas = 0
for valor in l_mt_testada:
    soma_areas_testadas += (valor - media_area_testada) ** 2
variancia_areas_testadas = soma_areas_testadas / len(l_mt_testada)
desvio_padrao_areas_testadas = variancia_areas_testadas ** 0.5

soma_areas_reais = 0
for valor in l_areas_reais:
    soma_areas_reais += (valor - media_area_real) ** 2
variancia_areas_reais = soma_areas_reais / len(l_areas_reais)
desvio_padrao_areas_reais = variancia_areas_reais ** 0.5

soma_areas_construidas = 0
for valor in l_areas_construidas:
    soma_areas_construidas += (valor - media_area_construida) ** 2
variancia_areas_construidas = soma_areas_construidas / len(l_areas_construidas)
desvio_padrao_areas_construidas = variancia_areas_construidas ** 0.5

soma_areas_corrigidas = 0
for valor in l_areas_corrigidas:
    soma_areas_corrigidas += (valor - media_area_corrigida) ** 2
variancia_areas_corrigidas = soma_areas_corrigidas / len(l_areas_corrigidas)
desvio_padrao_areas_corrigidas = variancia_areas_corrigidas ** 0.5

soma_valores_terreno = 0
for valor in l_valores_terreno:
    soma_valores_terreno += (valor - media_valor_terreno) ** 2
variancia_valores_terreno = soma_valores_terreno / len(l_valores_terreno)
desvio_padrao_valores_terreno  = variancia_valores_terreno ** 0.5

soma_valores_construidos = 0
for valor in l_valores_construidos:
    soma_valores_construidos += (valor - media_valor_construido) ** 2
variancia_valores_construidos = soma_valores_construidos / len(l_valores_construidos)
desvio_padrao_valores_construidos = variancia_valores_construidos ** 0.5

soma_valores_imovel = 0
for valor in l_valores_imovel:
    soma_valores_imovel += (valor - media_valor_imovel) ** 2
variancia_valores_imovel = soma_valores_imovel / len(l_valores_imovel)
desvio_padrao_valores_imovel = variancia_valores_imovel ** 0.5

soma_aliquota_iptu = 0
for valor in l_aliquota_iptu:
    soma_aliquota_iptu += (valor - media_aliquota_iptu) ** 2   
variancia_aliquota_iptu = soma_aliquota_iptu / len(l_aliquota_iptu)
desvio_padrao_aliquota_iptu = variancia_aliquota_iptu ** 0.5

soma_valores_iptu = 0
for valor in l_valores_iptu:
    soma_valores_iptu += (valor - media_valor_iptu) ** 2
variancia_valores_iptu = soma_valores_iptu / len(l_valores_iptu)
desvio_padrao_valores_iptu = variancia_valores_iptu ** 0.5

soma_valores_tcl = 0
for valor in l_valores_tcl:
    soma_valores_tcl += (valor - media_valor_tcl) ** 2
variancia_valores_tcl = soma_valores_tcl / len(l_valores_tcl)
desvio_padrao_valores_tcl = variancia_valores_tcl ** 0.5


contagem_divisoes = {}
for divisao in divisoes:
    if divisao in contagem_divisoes:
        contagem_divisoes[divisao] += 1
    else:
        contagem_divisoes[divisao] = 1
moda_divisao = max(contagem_divisoes, key=contagem_divisoes.get)

contagem_bairros = {}
for bairro in bairros:
    if bairro in contagem_bairros:
        contagem_bairros[bairro] += 1
    else:
        contagem_bairros[bairro] = 1
moda_bairro = max(contagem_bairros, key=contagem_bairros.get)

contagem_setores = {}
for setor in setores:
    if setor in contagem_setores:
        contagem_setores[setor] += 1
    else:
        contagem_setores[setor] = 1
moda_setor = max(contagem_setores, key=contagem_setores.get)

contagem_quarteiroes = {}
for quarteirao in quarteiroes:  
    if quarteirao in contagem_quarteiroes:
            contagem_quarteiroes[quarteirao] += 1
    else:
        contagem_quarteiroes[quarteirao] = 1
moda_quarteirao = max(contagem_quarteiroes, key=contagem_quarteiroes.get)

contagem_ceps = {}
for cep in ceps:
    if cep in contagem_ceps:
        contagem_ceps[cep] += 1
    else:
        contagem_ceps[cep] = 1
moda_cep = max(contagem_ceps, key=contagem_ceps.get)

contagem_num_enderecos = {}
for num_end in num_enderecos:
    if num_end in contagem_num_enderecos:
        contagem_num_enderecos[num_end] += 1
    else:
        contagem_num_enderecos[num_end] = 1
moda_num_endereco = max(contagem_num_enderecos, key=contagem_num_enderecos.get)

contagem_areas_testadas = {}
for area in l_mt_testada:
    if area in contagem_areas_testadas:
        contagem_areas_testadas[area] += 1
    else:
        contagem_areas_testadas[area] = 1
moda_area_testada = max(contagem_areas_testadas, key=contagem_areas_testadas.get)

contagem_areas_reais = {}
for area in l_areas_reais:
    if area in contagem_areas_reais:
        contagem_areas_reais[area] += 1
    else:
        contagem_areas_reais[area] = 1
moda_area_real = max(contagem_areas_reais, key=contagem_areas_reais.get)

contagem_areas_construidas = {}
for area in l_areas_construidas:
    if area in contagem_areas_construidas:
        contagem_areas_construidas[area] += 1
    else:
        contagem_areas_construidas[area] = 1
moda_area_construida = max(contagem_areas_construidas, key=contagem_areas_construidas.get)

contagem_areas_corrigidas = {}
for area in l_areas_corrigidas:
    if area in contagem_areas_corrigidas:
        contagem_areas_corrigidas[area] += 1
    else:
        contagem_areas_corrigidas[area] = 1
moda_area_corrigida = max(contagem_areas_corrigidas, key=contagem_areas_corrigidas.get)

contagem_valores_terreno = {}
for valor in l_valores_terreno:
    if valor in contagem_valores_terreno:
        contagem_valores_terreno[valor] += 1
    else:
        contagem_valores_terreno[valor] = 1
moda_valor_terreno = max(contagem_valores_terreno, key=contagem_valores_terreno.get)

contagem_valores_construidos = {}
for valor in l_valores_construidos:
    if valor in contagem_valores_construidos:
        contagem_valores_construidos[valor] += 1
    else:
        contagem_valores_construidos[valor] = 1
moda_valor_construido = max(contagem_valores_construidos, key=contagem_valores_construidos.get)

contagem_valores_imovel = {}
for valor in l_valores_imovel:
    if valor in contagem_valores_imovel:
        contagem_valores_imovel[valor] += 1
    else:
        contagem_valores_imovel[valor] = 1
moda_valor_imovel = max(contagem_valores_imovel, key=contagem_valores_imovel.get)

contagem_aliquota_iptu = {}
for valor in l_aliquota_iptu:
    if valor in contagem_aliquota_iptu:
        contagem_aliquota_iptu[valor] += 1
    else:
        contagem_aliquota_iptu[valor] = 1
moda_aliquota_iptu = max(contagem_aliquota_iptu, key=contagem_aliquota_iptu.get)

contagem_valores_iptu = {}
for valor in l_valores_iptu:
    if valor in contagem_valores_iptu:
        contagem_valores_iptu[valor] += 1
    else:
        contagem_valores_iptu[valor] = 1
moda_valor_iptu = max(contagem_valores_iptu, key=contagem_valores_iptu.get)

contagem_valores_tcl = {}
for valor in l_valores_tcl:
    if valor in contagem_valores_tcl:
        contagem_valores_tcl[valor] += 1
    else:
        contagem_valores_tcl[valor] = 1
moda_valor_tcl = max(contagem_valores_tcl, key=contagem_valores_tcl.get)


qtd_divisoes = len(set(divisoes))
qtd_bairros = len(set(bairros))
qtd_setores = len(set(setores))
qtd_quarteiroes = len(set(quarteiroes))
qtd_ceps = len(set(ceps))
qtd_num_enderecos = len(set(num_enderecos))
qtd_areas_testadas = len(set(l_mt_testada))
qtd_areas_reais = len(set(l_areas_reais))
qtd_areas_construidas = len(set(l_areas_construidas))
qtd_areas_corrigidas = len(set(l_areas_corrigidas))
qtd_valores_terreno = len(set(l_valores_terreno))
qtd_valores_construidos = len(set(l_valores_construidos))
qtd_valores_imovel = len(set(l_valores_imovel))
qtd_aliquota_iptu = len(set(l_aliquota_iptu))
qtd_valores_iptu = len(set(l_valores_iptu))
qtd_valores_tcl = len(set(l_valores_tcl))


print(f'Total de linhas: {total_linhas}')
print(f'Divisão - Qtd distintos: {qtd_divisoes}, Moda: {moda_divisao}')
print(f'Bairro - Qtd distintos: {qtd_bairros}, Moda: {moda_bairro}')
print(f'Setor - Qtd distintos: {qtd_setores}, Moda: {moda_setor}')
print(f'Quarteirão - Qtd distintos: {qtd_quarteiroes}, Moda: {moda_quarteirao}')
print(f'CEP - Qtd distintos: {qtd_ceps}, Moda: {moda_cep}')
print(f'Número do Endereço - Qtd distintos: {qtd_num_enderecos}, Moda: {moda_num_endereco}')
print(f'Área Testada - Qtd distintos: {qtd_areas_testadas}, Mínimo: {minimo_area_testada}, Máximo: {maximo_area_testada}, Média: {media_area_testada:.2f}, Mediana: {mediana_area_testada}, Moda: {moda_area_testada}, Desvio Padrão: {desvio_padrao_areas_testadas:.2f}')
print(f'Área Real - Qtd distintos: {qtd_areas_reais}, Mínimo: {minimo_area_real}, Máximo: {maximo_area_real}, Média: {media_area_real:.2f}, Mediana: {mediana_area_real}, Moda: {moda_area_real}, Desvio Padrão: {desvio_padrao_areas_reais:.2f}')
print(f'Área Construída - Qtd distintos: {qtd_areas_construidas}, Mínimo: {minimo_area_construida}, Máximo: {maximo_area_construida}, Média: {media_area_construida:.2f}, Mediana: {mediana_area_construida}, Moda: {moda_area_construida}, Desvio Padrão: {desvio_padrao_areas_construidas:.2f}')
print(f'Área corrigida - Qtd distintos: {qtd_areas_corrigidas}, Mínimo: {minimo_area_corrigida}, Máximo: {maximo_area_corrigida}, Média: {media_area_corrigida:.2f}, Mediana: {mediana_area_corrigida}, Moda: {moda_area_corrigida}, Desvio Padrão: {desvio_padrao_areas_corrigidas:.2f}')
print(f'Valor do Terreno - Qtd distintos: {qtd_valores_terreno}, Mínimo: {minimo_valor_terreno}, Máximo: {maximo_valor_terreno}, Média: {media_valor_terreno:.2f}, Mediana: {mediana_valor_terreno}, Moda: {moda_valor_terreno}, Desvio Padrão: {desvio_padrao_valores_terreno:.2f}')
print(f'Valor Construções - Qtd distintos: {qtd_valores_construidos}, Mínimo: {minimo_valor_construido}, Máximo: {maximo_valor_construido}, Média: {media_valor_construido:.2f}, Mediana: {mediana_valor_construido}, Moda: {moda_valor_construido}, Desvio Padrão: {desvio_padrao_valores_construidos:.2f}')
print(f'Valor do Imóvel - Qtd distintos: {qtd_valores_imovel}, Mínimo: {minimo_valor_imovel}, Máximo: {maximo_valor_imovel}, Média: {media_valor_imovel:.2f}, Mediana: {mediana_valor_imovel}, Moda: {moda_valor_imovel}, Desvio Padrão: {desvio_padrao_valores_imovel:.2f}')
print(f'Alíquota do IPTU - Qtd distintos: {qtd_aliquota_iptu}, Mínimo: {minimo_aliquota_iptu}, Máximo: {maximo_aliquota_iptu}, Média: {media_aliquota_iptu:.2f}, Mediana: {mediana_aliquota_iptu}, Moda: {moda_aliquota_iptu}, Desvio Padrão: {desvio_padrao_aliquota_iptu:.2f}')
print(f'Valor do IPTU - Qtd distintos: {qtd_valores_iptu}, Mínimo: {minimo_valor_iptu}, Máximo: {maximo_valor_iptu}, Média: {media_valor_iptu:.2f}, Mediana: {mediana_valor_iptu}, Moda: {moda_valor_iptu}, Desvio Padrão: {desvio_padrao_valores_iptu:.2f}')
print(f'Valor do TCL - Qtd distintos: {qtd_valores_tcl}, Mínimo: {minimo_valor_tcl}, Máximo: {maximo_valor_tcl}, Média: {media_valor_tcl:.2f}, Mediana: {mediana_valor_tcl}, Moda: {moda_valor_tcl}, Desvio Padrão: {desvio_padrao_valores_tcl:.2f}')
print('----------------------------------------------------------------------------------------------------')
