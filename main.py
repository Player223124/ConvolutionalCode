from PyQt5 import QtWidgets, QtCore
from ui import Ui_MainWindow
from encoder import ConvolutionalEncoder

def create():
    try:
        global column_count
        column_count = int(ui.register_count_text.toPlainText()) #Количество регистров
        global row_count
        row_count = int(ui.adder_count_text.toPlainText()) #Количество сумматоров
        ui.table.setRowCount(row_count)
        ui.table.setColumnCount(column_count)
    except:
        ui.output_text.setText('Input error')

def start():
    try:
        comm = []
        for row_ind in range(row_count):
            adder_list = []
            for column_ind in range(column_count):
                adder_list.append(int(ui.table.item(row_ind, column_ind).text()))
            comm.append(adder_list)
        print('Entered adders:\n', comm)    
        coder = ConvolutionalEncoder(comm)

        if ui.encode_radio.isChecked():
            print('\nEncoding option is choosen')

            i = list(ui.input_text.toPlainText().replace(' ',''))
            i = list(map(int, i))
            print('\nEntered word:\n', i)

            result = str(coder.encode(i))
            ui.output_text.setText(result)
            print('\nOutput:\n', result, '\n', '-'*30)

        elif ui.decode_radio.isChecked():
            print('\nDecoding option is choosen')

            C = list(ui.input_text.toPlainText().replace(' ',''))
            C = list(map(int, C))
            print('\nEntered word:\n', C)

            result = str(coder.decode(C))
            ui.output_text.setText(result)
            print('\nOutput:\n', result, '\n', '-'*30)

        else:
            ui.output_text.setText('Choose an option using radio buttons')

    except:
        ui.output_text.setText('Input error')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.create_button.clicked.connect(lambda: create())
    ui.start_button.clicked.connect(lambda: start())
    sys.exit(app.exec_())