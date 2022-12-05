import mysql.connector

class Elogio :
    
    ElogiosIDs = []
    
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
         dados = ('Elogio', descricao)
         cursor.execute(codigoSql, dados)
         conexaoBD.commit()
         cursor.close()
         print('Elogio inserido com sucesso!')
         conexaoBD.close()


    def listar(self):
         self.ElogiosIDs = []
         count = 1
        
         conexaoBD = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "ouvidoria",
         )
         cursor = conexaoBD.cursor()
         codigoSql = 'SELECT * FROM ocorrencias WHERE tipo = "Elogio"'
         cursor.execute(codigoSql)
         resultado = cursor.fetchall()
         cursor.close()
         
         if len(resultado) == 0:
            print('\nNão há Elogios para listar\n')
         else:
           for itemBD in resultado:
             print('='*100)
             print('Elogio'.center(100))
             print(f'{count} | {itemBD[1]} | {itemBD[2]}')
             print('-'*100)
             self.ElogiosIDs.append(itemBD[0])
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
            codigoSql = 'DELETE FROM ocorrencias WHERE tipo = "Elogio"'
            cursor.execute(codigoSql)
            conexaoBD.commit()
            cursor.close()
            print('Todos os Elogios foram apagados!')
        
        elif id > len(self.ElogiosIDs):
            print('Erro! Elogio não encontrado.')
        else:
         idBancoDeDados = self.ElogiosIDs[id - 1]
         
         codigoSql = 'DELETE FROM ocorrencias WHERE id=%s'
         dados = (idBancoDeDados,)
         cursor.execute(codigoSql, dados)
         conexaoBD.commit()
         cursor.close()
         print('Elogio apagado com sucesso!')


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
        
           print('\nElogio editado com sucesso.\n')