from PyQt5 import uic, QtWidgets
import pymysql

banco = pymysql.connect (
    host="localhost",
    user="root",
    passwd="1234",
    database="gerenciamentoProdutos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    disponibilidade = ""
    
    if formulario.radioButton.isChecked():
        print("Produto indisponível no estoque.")
        disponibilidade = "Nao"
    elif formulario.radioButton_2.isChecked():
        print("Produto disponível no estoque.")
        disponibilidade = "Sim"

    print("Nome",linha1)
    print("Descrição",linha2)
    print("Valor",linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (nome, descricao, valor, disponibilidade) VALUES (%s, %s, %s, %s)"
    dados = (linha1, linha2, linha3, disponibilidade)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chamaSegundaTela():
    segundaTela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dadosLidos = cursor.fetchall()

    segundaTela.tableWidget.setRowCount(len(dadosLidos))
    segundaTela.tableWidget.setColumnCount(5)

    for i in range(0, len(dadosLidos)):
        for j in range(0,5):
            segundaTela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosLidos[i][j])))



def excluirDados():
    linha = segundaTela.tableWidget.currentRow()
    segundaTela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dadosLidos = cursor.fetchall()
    valorId = dadosLidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+str(valorId))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segundaTela=uic.loadUi("listarDados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chamaSegundaTela)
segundaTela.pushButton.clicked.connect(excluirDados)

formulario.show()
app.exec()

#tabela

""" create table produtos (
id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao VARCHAR(50),  
preco DOUBLE,
categoria VARCHAR(20),
PRIMARY KEY (id)
);  """

#registros

#INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (123,"impressora",500.00,"informatica"); 