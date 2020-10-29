import numpy as np
import time
# print(np.arange(10))

km = np.loadtxt(fname='data/carros-km.txt', dtype = int)
# print(type(km))

dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
# print(dados)

acessorios = np.array(dados)
# print(acessorios)
# print(acessorios.shape)
# print(km.shape)

# o array do numpy é mais rapido que as listas
np_array = np.arange(1000000)
# print(np_array)
py_list = list(range(1000000))
# print(py_list)

# for _ significa ignorar a variavel
tinicio = time.time()
for _ in range(100): np_array *= 2
print('Array levou '+str(time.time()-tinicio)+'s')

tinicio = time.time()
for _ in range(100): py_list = [x * 2 for x in py_list]
print('Lista levou '+str(time.time()-tinicio)+'s')