# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:43:17 2019

@author: Rodrigo Alves and Hananias Daniel
"""
from random import randint
import logging

class CamadaR:
    def __init__(self, idOrigem, idDestino, quantNos, Pacote):
        self.idOrigem = idOrigem
        self.idDestino = idDestino
        self.quantNos = quantNos
        self.Pacote = Pacote
        self.rotaDSR = []
        self.contPacote = []
        self.arrayVizinho = []
        
    def getPacote(self):
        return self.contPacote
    
    def setPacote(self, x):
        self.contPacote = x
        
    def getDestino(self):
        return self.idDestino
         
    def getOrigem(self):
        return self.idOrigem
    
    def getRota(self):
        return self.rotaDSR
    
    def encontraVizinho(self):
        
        for i in range (self.quantNos):
            if i != self.idOrigem:
                if abs((matriz[self.idOrigem].getPosicao() - matriz[i].getPosicao() == 2) or (matriz[i].getPosicao() - matriz[self.idOrigem].getPosicao() == 2)):
                    self.arrayVizinho.append(i)
                    
        #print(f'Os vizinhos de {self.idOrigem} são {self.arrayVizinho}')
     
    
    def DynamicSourceRouting(self, idOrigem, idDestino):
        logging.debug('Aplicando o DSR para descobrimento de rotas!!')
        k = self.idOrigem
        m = 0
        n = 0
        if(k < self.idDestino):
            for i in range ((self.idDestino-self.idOrigem)+1):
                n = n + 1
                if (n == 0):
                    continue
                
                logging.debug('Request sendo enviado para {}'.format(k))
                m = m + 1
                matriz[i + 2].infoSolicitacoes = (1,0,m)
                matriz[i - 2].infoSolicitacoes = (1,0,m)
                self.rotaDSR.append(k)
                if (k == self.idDestino):
                    logging.debug('Request chegou no destino')
                    for i in range (self.idDestino, self.idOrigem, -1):
                        if (i == self.idOrigem+1):
                            self.rotaDSR.reverse()
                            logging.debug('Reply sendo enviado pela rota {}'.format(self.getRota()))
                            matriz[i].infoSolicitacoes = (0,1,m)
                            self.rotaDSR.reverse()
                k = k + 1
        else:
            n = 0
            for i in range (self.idOrigem, self.idDestino-1, -1):
                n = n + 1
                if (n == 0):
                    continue
                
                logging.debug('Request sendo enviado para {}'.format(i))
                m = m + 1
                matriz[i + 2].infoSolicitacoes = (1,0,m)
                matriz[i - 2].infoSolicitacoes = (1,0,m)
                self.rotaDSR.append(i)
                if (i == self.idDestino):
                    logging.debug('Request chegou no destino')
                    for i in range (self.idDestino, self.idOrigem, 1):
                        if (i == self.idOrigem - 1):
                            self.rotaDSR.reverse()
                            logging.debug('Reply sendo enviado por {}'.format(self.getRota()))
                            matriz[i].infoSolicitacoes = (0,1,m)
                            self.rotaDSR.reverse()
                k = k + 1
            
        
    def getVizinhos(self):
        return self.arrayVizinho
                    
    def enviaPacoteRE(self, Pacote, idOrigem, idDestino):
        #percorre todo array dos vizinhos
        #self.encontraVizinho()
        n = 0
        for i in self.arrayVizinho:
            n = n + 1
            if(n == 2):
                self.Pacote.removeCabecalho()
                
            matriz[self.idDestino].infoNo(self.idDestino, Pacote)
            self.Pacote.adicionaCabecalho(self.idOrigem, self.idDestino, 2)
            logging.debug('Cabeçalho da camada de Rede adicionado!!')
        print("Enviando REDE -> ENLACE") 
    
    def recebePacoteRE(self, idOrigem , Pacote, vizinhoDestino):
        print(f'Pacote:{self.Pacote.getPacote()}')
 

class CamadaE:
    def __init__(self, idOrigem, idDestino, quantNos, Pacote):
        self.idOrigem = idOrigem
        self.idDestino = idDestino
        self.quantNos = quantNos
        self.arrayVizinho = []
        self.Pacote = Pacote
        self.contPacote = []
        
    def getPacote(self):
        return self.contPacote
    
    def setPacote(self, x):
        self.contPacote = x
        
    def getDestino(self):
        return self.idDestino
         
    def getOrigem(self):
        return self.idOrigem
    
    def encontraVizinho(self):
        
        for i in range (self.quantNos):
            if i != self.idOrigem:
                if abs((matriz[self.idOrigem].getPosicao() - matriz[i].getPosicao() == 2) or (matriz[i].getPosicao() - matriz[self.idOrigem].getPosicao() == 2)):
                    self.arrayVizinho.append(i)
                
    def enviaPacoteEF(self, Pacote, idOrigem, idDestino):
        #percorre todo array dos vizinhos
        #self.encontraVizinho()
        n = 0
        for i in self.arrayVizinho:
            n = n + 1
            if (n == 2):
                self.Pacote.removeCabecalho()
            matriz[self.idDestino].infoNo(self.idDestino, Pacote)
            logging.debug('Cabeçalho da camada de Enlace adicionado!!')
            self.Pacote.adicionaCabecalho(self.idOrigem, self.idDestino, 1)
        print("Enviando ENLACE -> FISICA")   
        
    def enviaPacoteER(self, Pacote, idOrigem, idDestino):
        #percorre todo array dos vizinhos
        #self.encontraVizinho()
        
        for i in self.arrayVizinho:
            matriz[self.idDestino].infoNo(self.idDestino, Pacote)
        print("Enviando ENLACE -> REDE")                 
    
    def recebePacoteEF(self, idOrigem , Pacote, vizinhoDestino):
        print(f'Pacote :{self.Pacote.getPacote()} ')

    
    def recebePacoteER(self, idOrigem , Pacote, vizinhoDestino):
        print(f'Pacote:{self.Pacote.getPacote()}')
       

class CamadaF:
    def __init__(self, idOrigem, idDestino, quantNos, Pacote):
        self.idOrigem = idOrigem
        self.idDestino = idDestino
        self.quantNos = quantNos
        self.arrayVizinho = []
        self.Pacote = Pacote
        self.contPacote = []
        
    def getPacote(self):
        return self.contPacote
    
    def setPacote(self, x):
        self.contPacote = x
        
    def getDestino(self):
        return self.idDestino
         
    def getOrigem(self):
        return self.idOrigem
    
    def encontraVizinho(self):
        for i in range (self.quantNos):
            if i != self.idOrigem:
                if abs((matriz[self.idOrigem].getPosicao() - matriz[i].getPosicao() == 2) or (matriz[i].getPosicao() - matriz[self.idOrigem].getPosicao() == 2)):
                    self.arrayVizinho.append(i)
    
    def enviaPacoteFF(self, Pacote, idOrigem, idDestino):
        #percorre todo array dos vizinhos
        #self.encontraVizinho()
        n = 0
        for i in self.arrayVizinho:
            n = n + 1
            if(n == 2):
              self.Pacote.removeCabecalho()  
            matriz[self.idDestino].infoNo(self.idDestino, Pacote)
            self.Pacote.adicionaCabecalho(self.idOrigem, self.idDestino, 0)
            logging.debug('Cabeçalho da camada Física adicionado!!')
        print("Enviando FISICA -> FISICA")                      
    
    def enviaPacoteFE(self, Pacote, idOrigem, idDestino):
        #percorre todo array dos vizinhos
        #self.encontraVizinho() 
        for i in self.arrayVizinho:
            matriz[self.idDestino].infoNo(self.idDestino, Pacote)
        print("Enviando FISICA -> ENLACE")           
    
    def recebePacoteFF(self, idOrigem , Pacote, vizinhoDestino):
        print(f'Pacote:{self.Pacote.getPacote()}')      

    def recebePacoteFE(self, idOrigem , Pacote, vizinhoDestino):
        print(f'Pacote:{self.Pacote.getPacote()}')


class Pacote:
    def __init__(self):
        self.pacote = []
    
    def iniciaDados(self):
        for i in range (3):
            self.pacote.append(randint(0, 100))
            
    def getPacote(self):
        return self.pacote
    
    def adicionaCabecalho(self, idOrigem, idDestino, camada):
        for i in range (3):
            if(i == 0):
                self.pacote.append(idOrigem)
            if(i == 1):
                self.pacote.append(idDestino)
            if(i == 2):
                self.pacote.append(camada)
    
    def removeCabecalho(self):
        n = len(self.pacote)
        for i in range (10):
            if (i > 2):
                break
            else:
                self.pacote.pop((n-1)-i)
        #print(self.pacote)
        
        
class TopologiaRede:
    def __init__(self, posi):
        self.posi = posi
        self.idNo = posi
        self.bufferNo = 0
        self.bufferRREP = 0
        self.bufferRREQ = 0

    def getNo(self):
        return self.idNo
    
    def infoNo(self, idNo, pacote):
        self.idNo = idNo
        self.bufferNo = pacote
    
    def infoSolicitacoes(self, RREQ, RREP, idRREQ):
        self.bufferRREQ = RREQ
        self.bufferRREP = RREP
        self.idRREQ = idRREQ
        
    def getPosicao(self):
        return self.posi


matriz = []
buffer = []
obj1 = []
obj2 = []
obj3 = []
v = []

logging.basicConfig(filename='meuLog.log', level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def main():
        
        nos = int(input("Insira a quantidade de nos da rede: "))
        
        for i in range (nos+2):
            matriz.append(TopologiaRede(i))
        
        for i in range (nos):
            print(f'Nó:{matriz[i].getNo()} está na posição {matriz[i].getPosicao()}')
            
        while(1):    
            
            pac = Pacote()
            pac.iniciaDados()
            
            ori = int(input("Enviar de quem: "))
            dest = int(input("Para quem: "))
            print("\n")
            
            obj1 = CamadaR(ori,dest, nos, pac)
            obj2 = CamadaE(1,4, nos, pac)
            obj3 = CamadaF(1,4, nos, pac)
            obj1.DynamicSourceRouting(ori,dest)
            print(f'Rota a ser seguida: {obj1.getRota()}')
            print("\n")
            
            obj1.encontraVizinho()
            obj2.encontraVizinho()
            obj3.encontraVizinho()
            
            for i in range (len(obj1.getRota())-1):
                
                print(f'Enviando do Nó: ->{obj1.rotaDSR[i]}<- para o Nó: ->{obj1.rotaDSR[i+1]}<-')
                logging.debug('Nó ->{}<- enviando para ->{}<-'.format(obj1.rotaDSR[i],obj1.rotaDSR[i+1]))
            
                obj1.enviaPacoteRE(pac,ori,dest)     ##Rede -> Enlace
                obj2.recebePacoteER(ori,pac, obj1.rotaDSR[i])   ##N remove
                
                
                obj2.enviaPacoteEF(pac, ori, dest)   ##Enlace -> Fisica
                obj3.recebePacoteFE(ori,pac, obj1.rotaDSR[i])    ##N remove
                
                obj3.enviaPacoteFF(pac,ori,dest)     ##Fisica -> Fisica
                obj3.recebePacoteFF(ori,pac, obj1.rotaDSR[i])    ##Remove
                logging.debug('Removendo cabeçalho!!')
                pac.removeCabecalho()
                
                obj3.enviaPacoteFE(pac,ori,dest)     ## Fisica -> Enlace
                obj2.recebePacoteEF(ori,pac, obj1.rotaDSR[i])    ##Remove
                logging.debug('Removendo cabeçalho!!')
                pac.removeCabecalho()
                
                obj2.enviaPacoteER(pac,ori,dest)     ##Enlace -> Rede
                obj1.recebePacoteRE(ori,pac, obj1.rotaDSR[i])    ##Remove
                logging.debug('Removendo cabeçalho!!')
                pac.removeCabecalho()
                
                logging.debug('Pacote recebido!')
                
                print("\n\n")
            
            logging.debug('O pacote foi recebido no Destino e seu valor eh: {} '.format(pac.getPacote()))
            
            print(f'O conteúdo eh:{pac.getPacote()}')
    
        
    
if __name__ == "__main__":
    main()
