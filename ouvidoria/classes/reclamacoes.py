import mysql.connector

class Reclamacoes :
    
    ReclamacoesIDs = []
    
    def __init__(self):
        pass
   

    def inserir(self, descricao):
         conexaoBD = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "ouvidoria",
         )
         cursor = conexaoBD.cursor()
         codigoSql = 'INSERT INTO ocorrencias(tipo,descricao) VALUES (%s, %s)'
         dados = ('Reclamacoes', descricao)
         cursor.execute(codigoSql, dados)
         conexaoBD.commit()
         cursor.close()
         print('Reclamação inserida com sucesso!')
         conexaoBD.close()


    def listar(self):
         self.ReclamacoesIDs = []
         count = 1
        
         conexaoBD = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "ouvidoria",
         )
         cursor = conexaoBD.cursor()
         codigoSql = 'SELECT * FROM ocorrencias WHERE tipo = "Reclamacoes"'
         cursor.execute(codigoSql)
         resultado = cursor.fetchall()
         cursor.close()
         
         if len(resultado) == 0:
            print('\nNão há Reclamações para listar\n')
         else:
           for itemBD in resultado:
             print('='*100)
             print('Reclamações'.center(100))
             print(f'{count} | {itemBD[1]} | {itemBD[2]}')
             print('-'*100)
             self.ReclamacoesIDs.append(itemBD[0])
             count += 1
         conexaoBD.close()
  

    def apagar(self, id):
        conexaoBD = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "ouvidoria",
         )
        cursor = conexaoBD.cursor()
        
        if id == 0:
            codigoSql = 'DELETE FROM ocorrencias WHERE tipo = "Reclamacoes"'
            cursor.execute(codigoSql)
            conexaoBD.commit()
            cursor.close()
            print('Todas as Reclamações foram apagadas!')
        
        elif id > len(self.ElogiosIDs):
            print('Erro! Reclamação não encontrada.')
        else:
         idBancoDeDados = self.ElogiosIDs[id - 1]
         
         codigoSql = 'DELETE FROM ocorrencias WHERE id=%s'
         dados = (idBancoDeDados,)
         cursor.execute(codigoSql, dados)
         conexaoBD.commit()
         cursor.close()
         print('Reclamação apagada com sucesso!')


    def editar(self, id, novaDescricao):
        conexaoBD = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "ouvidoria",
         )
        
        
        
        if id == 0 or id > len(self.ElogiosIDs):
            print('\n#Erro# Elogio não encontrao.\n')
        else:
           indice= self.ElogiosIDs[id - 1]
           codigoSql = 'UPDATE ocorrencias SET descricao = %s WHERE id = %s'
           dados = (novaDescricao, indice)
           
           cursor = conexaoBD.cursor()
           cursor.execute(codigoSql, dados)
           conexaoBD.commit()
           cursor.close() 
        
           print('\nReclamação editada com sucesso.\n')