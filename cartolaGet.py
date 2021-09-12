import requests
import json
from tabulate import _table_formats, tabulate
from os import path
import os
import datetime

turno1 = {"Mateus": 1259.86,
		 "Philippe": 1035.92,
		 "Lucas": 1129.01,
		 "Lucas Lopes": 1221.7,
		 "Rafael Paiva": 969.69,
		 "Bruno": 1179.94,
		 "Bernardo": 1011.37,
		 "Guilherme": 1188.36,
		 "Anderson": 1056.63,
		 "Vinícius": 834.719,
		 "Alexandre": 922.25,
		 "Cneri": 873.54,
		 "Bismarck": 1119.03,
		 "Dedé": 856.15,
		 "Farlin": 1082.07
}

boeia = {"Mateus": ["1132784", "https://s2.glbimg.com/pkzuRLsPtYPY-Ji8Xk6AFHBv5zo=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_188/escudo/6b/14/31/008ef9c265-84b5-4e00-94d8-345d9d589b6b20210525081431", "FlaDelRey"],
		 "Philippe": ["3181812", "https://s2.glbimg.com/Bjyewyr55XEjG1F-rnf_kuMxrlI=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_166/escudo/fb/39/45/00905c944b-c962-43bc-8b1d-4316994f5bfb20200726173945", "NABUCODONOSO F. C."],
		 "Lucas": ["1584372", "https://s2.glbimg.com/OsRjlmBvDw9Ilg_JivKVkyVlJgI=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_173/escudo/90/15/53/0080652d80-4c17-4940-95b0-292baf15d59020200809221553", "LucasFlaResende"],
		 "Lucas Lopes": ["25568007", "https://s2.glbimg.com/P2uMvBzspeg9JIL9P2g4SKxuv5M=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_183/escudo/1f/43/43/00e705cf3e-736f-4223-b541-30dab9d0b51f20210427124343", "GWR Solutions"],
		 "Rafael Paiva": ["330706", "https://s2.glbimg.com/KyEPCHx-j_CAMXrEkjoDRyEwHgg=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_141/escudo/ab/00/25/0002109047-9fa7-4f12-baec-a221179caaab20190425130025", "Paivense Cabuloso"],
		 "Bruno": ["114639", "https://s2.glbimg.com/KyEPCHx-j_CAMXrEkjoDRyEwHgg=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_141/escudo/ab/00/25/0002109047-9fa7-4f12-baec-a221179caaab20190425130025", "Resistência Azul  F. C."],
		 "Bernardo": ["32791", "https://s2.glbimg.com/GPt3ZH1w-0F2UbTG3cPoCbnIB9w=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_183/escudo/78/13/31/00a7c82419-cb7f-46ae-b01f-3875118f367820210427131331", "Becofe F.C"],
		 "Guilherme": ["26714009", "https://s2.glbimg.com/QJZUPSOOh3t-Yi4DX0JtIwSfesc=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_173/escudo/93/31/24/0040c1daf5-8473-4344-b579-c02b29369b9320200810143124", "AUGuizolaFC"],
		 "Anderson": ["28653", "https://s2.glbimg.com/6J_oLCX9oLVzSHFaNdScpGbB0eo=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_188/escudo/3d/09/09/0074c78412-cdf5-4ca8-8624-83fa95db703d20210525220909", "Bera da Praia F.C."],
		 "Vinícius": ["2914856", "https://s2.glbimg.com/tFy6U7u-w8YSG6iX6k3l0NH5uXU=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_186/escudo/eb/33/44/00f808e39b-1813-4052-8d8e-8edb66b4e2eb20210513183344", "CabulosoFC86225"],
		 "Alexandre": ["26742415", "https://s2.glbimg.com/IqDkR8z_xpagzbof0vryNilYiBA=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_175/escudo/5c/33/21/008e28948f-f1b9-4c62-91fc-292be2a6ea5c20200812183321", "SC Colaboni"],
		 "Cneri": ["2580856", "https://s2.glbimg.com/8lzNQ-d-5KJ2WdSnjxWAGaZpU3Q=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_191/escudo/02/27/01/005f580794-7b89-447a-a1c6-c6433f7ab70220210529122701", "SJDR NTC"],
		 "Bismarck":["223725", "https://s2.glbimg.com/9kj50rE46ttxbFU0dkhhxM2jJNQ=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_108/escudo/fc/06/27/006b729cd9-e97f-4ae4-a66b-c580b98a71fc20180412120627", "Los Oto Patamar FC"],
		 "Dedé":["19750020", "https://s2.glbimg.com/fn_ogvadQ5b8_kFGwUXTHJ5SNzA=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_189/escudo/1b/19/43/00a9b0937c-8dbf-4643-8b8e-aaaf1753071b20210528091943", "Casa do Viajante FC"],
		 "Farlin":["35168", "https://s2.glbimg.com/iZOCN3GayfC0TkOf_XFj__sHvwM=/https://s3.glbimg.com/v1/AUTH_58d78b787ec34892b5aaa0c7a146155f/cartola_svg_189/escudo/7a/51/23/00638989fa-284b-4e8b-9004-246802d12e7a20210526205123", "Piripake EC"]}

base_url = "https://api.cartolafc.globo.com/time/id"
base_url_pontuacao = "https://api.cartolafc.globo.com/atletas/pontuados"
to_send = "https://cartolafc.globo.com/#!/time/"
base_url_partidas = "https://api.cartolafc.globo.com/partidas"

JOGOS = requests.get(base_url_partidas).json()['partidas'];

def getPerRound(id, rodada):
	url = base_url + "/" + str(id) + "/" + str(rodada)
	return requests.get(url).json()

def getPontuadores():
	return requests.get(base_url_pontuacao).json()

def printTabelaRodada(pontos_times, header):
	table = []
	for time in pontos_times:
		row = []
		row.append(time)
		for p in pontos_times[time]:
			row.append(p)
		table.append(row)

	print(tabulate(table,header))

def printTabelaTotal(pontos_times, header):
	table = []
	for time in pontos_times:
		row = []
		row.append(time)
		row.append(pontos_times[time])
		table.append(row)

	print(tabulate(table,header))
			
def getTabelaCompleta(pontos_p_r, rodada_atual, lim_col, prefix, time_partials):
	tabela_completa = []
	header_completo = ["Time"]
	rodada_added = []

	for time in pontos_p_r:
		row = []
		row.append(time)
		total = 0
		rodada = 0
		for ponto in pontos_p_r[time]:
			if rodada >= (rodada_atual - 2):
				if rodada not in rodada_added:
					if rodada == (rodada_atual-1):
						header_completo.append("("+str(rodada + 1)+")"+prefix)
					else:
						header_completo.append("("+str(rodada + 1)+")")
					rodada_added.append(rodada)
				row.append(ponto)
			rodada += 1
			total += ponto
		row.append(total)
		tabela_completa.append(row)
	
	header_completo.append("Total")
	sorter = lambda x: (x[len(x) - 1])
	tabela_ordenada = sorted(tabela_completa, key=sorter, reverse=True)

	## Get HTML JSON TAble
	now = datetime.datetime.now()
	cols = len(tabela_ordenada[0])
	tabela_obj = {}
	tabela_obj['current'] = rodada_atual
	tabela_obj['parcial'] = prefix
	tabela_obj['updated_at'] = str(datetime.datetime.strftime(now, '%d/%m/%Y %H:%M:%S'))
	tabela_obj['times'] = []

	print(tabela_ordenada)
	for row in tabela_ordenada:
		time_object = {}
		time_object['time_url'] = "https://cartolafc.globo.com/#!/time/" + str(boeia[row[0]][0])  + "/" + str(rodada_atual)
		time_object["cartoleiro"] = row[0]
		time_object["url_escudo"] = boeia[row[0]][1]
		time_object["time"] = boeia[row[0]][2]
		for i in range(1, 3):
			if i == rodada_atual and prefix == "*":
				time_object[str(i)] = str(round(row[i], 2)) + "["+str(time_partials[row[0]])+"]"
			else:
				time_object[str(i)] = str(round(row[i], 2))
		time_object["total"] = str(round(row[-1], 2))
		time_object["total1"] = str(round(turno1[row[0]],2))
		time_object["total2"] = str(round(row[-1] - turno1[row[0]],2))

		tabela_obj['times'].append(time_object)

	with open("./data.json", 'w') as f:
		json.dump(tabela_obj, f)
	print(tabulate(tabela_ordenada, header_completo))

def searchReservas(reservas, posicao_id, pontuadores):
	for a in reservas:
		club_id = a["clube_id"]
		pid = a["posicao_id"]
		aid = str(a["atleta_id"])
		if pid == posicao_id:
			if aid in pontuadores["atletas"]:
				return True, pontuadores["atletas"][aid]["pontuacao"]
	return False, 0.0

def partidaAcabou(time_id):
	for p in JOGOS:
		if time_id == p['clube_casa_id'] or time_id == p['clube_visitante_id']:
			if p['status_transmissao_tr'] == "ENCERRADA":
				return True
	return False;
			
def getPartials(time_info):
	#Load pontuadores
	amount = 0
	pontuadores_rodada = "rodadas/pontuadores_rodada_atual.json"
	pontuadores = None
	if not path.exists(pontuadores_rodada):
		pontuadores = getPontuadores()
		with open(pontuadores_rodada, 'w') as f:
			json.dump(pontuadores, f)
	else:
		with open(pontuadores_rodada) as json_file:
			pontuadores = json.load(json_file)

	partials = 0.0
	capitao_id = str(time_info["capitao_id"])
	substituidos_pos = []
	posicao_capitao_id = 0;
	time_capitao = 0
	for atleta in time_info["atletas"]:
		atleta_id = str(atleta["atleta_id"])
		if capitao_id == atleta_id:
			posicao_capitao_id = atleta["posicao_id"];
			time_capitao = atleta["clube_id"]
		if  atleta_id in pontuadores["atletas"]:
			partials += pontuadores["atletas"][atleta_id]["pontuacao"]
			amount += 1
		else:
			posicao_id = atleta["posicao_id"]
			if partidaAcabou(atleta["clube_id"]):
				if "reservas" in time_info:
					sub, value = searchReservas(time_info["reservas"], atleta["posicao_id"], pontuadores)
					if sub and posicao_id not in substituidos_pos:
						substituidos_pos.append(posicao_id)
						partials += value
						amount += 1
	
	if capitao_id in pontuadores["atletas"]:
		partials += pontuadores["atletas"][capitao_id]["pontuacao"]
		amount += 1
	else:
		if partidaAcabou(time_capitao):
			if "reservas" in time_info:
				sub, value = searchReservas(time_info["reservas"], posicao_capitao_id, pontuadores)
				if sub and posicao_id not in substituidos_pos:
					substituidos_pos.append(posicao_id)
					partials += value
					amount += 1

	return partials, amount

###############################################################################
###############################################################################
###############################################################################

rodada_atual = 20
partials = True

json_rodada_atual = "rodadas/rodada_" + str(rodada_atual) + ".json"
if not path.exists(json_rodada_atual):
	json_rodada_anterior = "rodadas/rodada_" + str((rodada_atual - 1)) + ".json"
	
	with open(json_rodada_anterior) as json_file:
		# Load json rodada anterior
		pontos_p_r = json.load(json_file)
	
		# Coleta dados rodada atual
		round_not_finished = False
		prefix = ""
		time_partials = {}
		for time in boeia:
			
			j = getPerRound(boeia[time][0], rodada_atual)
			p = j['pontos']
			if partials:
				round_not_finished = True
				prefix = "*"
				## Get paritals
				p, t = getPartials(j)
				time_partials[time] = t

			if rodada_atual - 1 == 0:
				pontos_p_r[time][0] = p
			else:
				pontos_p_r[time].append(p)
		
		if not round_not_finished:
			#salvar dados rodada atual se não for parciais
			with open(json_rodada_atual, 'w') as f:
				json.dump(pontos_p_r, f)
		else:
			print("Rodada não Finizalizada...")
			os.remove("rodadas/pontuadores_rodada_atual.json")

		getTabelaCompleta(pontos_p_r, rodada_atual, 2, prefix, time_partials)
else:
	with open(json_rodada_atual) as json_file:
		# Load json rodada atual
		pontos_p_r = json.load(json_file)
		getTabelaCompleta(pontos_p_r, rodada_atual, rodada_atual, "", None)
