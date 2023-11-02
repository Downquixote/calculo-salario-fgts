'''
PyQt5 -> uma ligação Python do kit de ferramentas Qt.

uic -> Interfaca de controle do usuário.

QtWidgets -> armazena diversos tipos de layout (itens da tela).
'''

from PyQt5 import uic, QtWidgets

def principal():
    # salario chama caixa de texto na variável "formulario".

    salario = formulario.txtSalario.text()
    salario = float(salario)
    desconto = formulario.txtDescontos.text()
    desconto = float(desconto)
    resultado = (-salario / 100 * desconto) + salario
    fgtsMensal = salario / 100 * 8
    fgtsAnual = (salario / 100 * 8) * 12 

    formulario.lblResultado.setText(str(f'R$ {resultado:.2f}'))
    formulario.lblFgtsMensal.setText(str(f'R$ {fgtsMensal:.2f}'))
    formulario.lblFgtsAnual.setText(str(f'R$ {fgtsAnual:.2f}'))

# QtWidgets.QApplication([]) -> ([]) > para ativar
app = QtWidgets.QApplication([])    

# uic.loadUi() -> informar o nome da tela que deseja carregar. 
formulario = uic.loadUi('Tela_salario.ui')   

# Chamando o botão Calcular com um clique e conectando a função "principal".
formulario.btnCalcular.clicked.connect(principal)

formulario.show()
app.exec()