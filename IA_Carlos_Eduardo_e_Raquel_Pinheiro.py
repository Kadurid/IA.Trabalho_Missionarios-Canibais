"""
 Trabalho 1 de Inteligencia Computacional
 Instituto Federal de Brasilia
 Carlos Eduardo Pereira Santana e Raquel Pinheiro Costa
 Algoritmo feito em base ao modelo de Busca por Largura/Amplitude
"""
class Estado(objeto):
	"""
	Construtor da classe, recebe como parametros um objeto estado, e coloca nele os atributos do numero de missionarios na esquerda e na direita,
	e o numero de canibais na esquerda e na direita, junto com isso e recebido o estado do barco, podendo ser esse ='direita' ou ='esquerda', que é a margem 
	do lago em que o barco se encontra, sendo abreviacoes para esquerda e direita respectivamente. E atribui como no pai do estado null.
	"""
	def __init__(self,missionariosE, canibaisE, barco_estado, missionariosD, canibaisD ):
		self. missionariosE = missionariosE				#missionariosE = quantidade de missionarios do lado esquerdo da margem
		self.canibaisE = canibaisE						#canibaisE = quantidade de canibais do lado esquerdo da margem
		self.barco_estado = barco_estado				#barco_estado = recebe um string como 'd' ou 'e', indica localizacao do barco
		self.missionariosD = missionariosD				#missionariosD = quantidade de missionarios do lado direito da margem
		self.canibaisD = canibaisD						#canibaisD = quantidade de canibais do lado direito da margem
		self.pai = None
	"""
	Valida na criacao de um novo estado, verificando condições de existência do estado, e se cumpre requisitos para que nao se torne um
	estado que nao faz parte da solucao, não podem ter numeros negativos nas quantidades, e verifica se a quantidade de canibais em alguma
	das margens e maior que a quantidade de missionarios, alem disso, caso nao haja missionarios em algum dos lados, nao e preciso verificar
	a desigualdade.
	"""
	def Validar(self):
		if 	self.missionariosE>=0 and self.missionariosD>=0 and self.canibaisD>=0 and self.canibaisE>=0 /
			and (self.missionariosE>=self.canibaisE or missionariosE==0) /
			and (self.missionariosD>=self.canibaisD or missionariosD==0):
			return True
		else:
			return False
	#Verifica se o estado atual == estado alvo.
	def EstadoAlvo(self):
		if self.missionariosE == 0 and self.canibaisE ==0 /
		and self.missionariosD ==3 and self.canibaisD ==3:
			return True
		else:
			return False
"""
Forma os filhos para a arvore de estados
"""
def filhos(estado_atual):
	filhos=[]
	"""
	Cria um filho para cada uma das possibilidades, sendo que, para todo estado novo, o estado do barco muda para a outra
	direcao, o filho e do objeto estado, que compoe a arvore, armazenando esses filhos em uma lista
	"""
	if estado_atual = 'esquerda':
			novo_estado = Estado(estado_atual.missionariosE-1,estado_atual.canibaisE,'direita',
				estado_atual.missionariosD+1,estado_atual.canibaisD)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE,estado_atual.canibaisE-1,'direita',
				estado_atual.missionariosD,estado_atual.canibaisD+1)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE-2,estado_atual.canibaisE,'direita',
				estado_atual.missionariosD+2,estado_atual.canibaisD)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE-1,estado_atual.canibaisE-1,'direita',
				estado_atual.missionariosD+1,estado_atual.canibaisD+1)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE,estado_atual.canibaisE-2,'direita',
				estado_atual.missionariosD,estado_atual.canibaisD+2)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

	else:
		novo_estado = Estado(estado_atual.missionariosE-1,estado_atual.canibaisE,'esquerda',
			estado_atual.missionariosD+1,estado_atual.canibaisD)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE,estado_atual.canibaisE-1,'esquerda',
				estado_atual.missionariosD,estado_atual.canibaisD+1)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE-2,estado_atual.canibaisE,'esquerda',
				estado_atual.missionariosD+2,estado_atual.canibaisD)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE,estado_atual.canibaisE-2,'esquerda',
				estado_atual.missionariosD,estado_atual.canibaisD+2)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)

			novo_estado = Estado(estado_atual.missionariosE-1,estado_atual.canibaisE-1,'esquerda',
				estado_atual.missionariosD+1,estado_atual.canibaisD+1)
			if novo_estado.Validar():
				novo_estado.pai = estado_atual
				filhos.append(novo_estado)
			return filhos





	
