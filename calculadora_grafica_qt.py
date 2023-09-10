import sys
from PyQt5.QtWidgets import *

def calcular_divisores():
    texto_digitado = textbox_numero.text()

    if not texto_digitado.isnumeric():
        QMessageBox.critical(
            window,
            "Erro",
            "Você não digitou um número válido. Não é possível haver letras ou números negativos digitados."
        )
    else:
        numero = int(texto_digitado)

        divisores_arr = [str(i) for i in range(1, numero + 1) if numero % i == 0]
        divisores = ", ".join(divisores_arr)

        QMessageBox.information(
            window,
            "Resultado",
            f"Os divisores de {numero} são: {divisores}."
        )

def limpar_texto():
    textbox_numero.setText("")

# ------------------------------------------------ #

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Calculadora de Divisores PyQt5 Procedural")

label_boas_vindas = QLabel(
    "Bem-vindo à versão gráfica da Calculadora de Divisores!",
    window
)
label_boas_vindas.setGeometry(75, 10, 380, 20)

label_digite_numero = QLabel("Digite um número:", window)
label_digite_numero.setGeometry(10, 40, 120, 20)

textbox_numero = QLineEdit(window)
textbox_numero.setGeometry(130, 40, 160, 20)

botao_calcular = QPushButton("Calcular", window)
botao_calcular.setGeometry(300, 40, 80, 20)
botao_calcular.clicked.connect(calcular_divisores)

botao_limpar = QPushButton("Limpar", window)
botao_limpar.setGeometry(390, 40, 80, 20)
botao_limpar.clicked.connect(limpar_texto)

window.setGeometry(100, 100, 480, 75)
window.show()

sys.exit(app.exec_())
