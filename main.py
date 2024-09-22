from PyQt5.QtWidgets import QMenuBar, QAction,QMainWindow,QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi ERP")
        self.setGeometry(100, 100, 800, 600)
        
        # Crear la barra de menú
        menubar = self.menuBar()
        
        # Añadir menú Archivo
        file_menu = menubar.addMenu("Archivo")
        
        # Añadir acciones al menú Archivo
        new_action = QAction("Nuevo", self)
        open_action = QAction("Abrir", self)
        save_action = QAction("Guardar", self)
        exit_action = QAction("Salir", self)
        
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)
        
        # Conectar la acción de salir
        exit_action.triggered.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
