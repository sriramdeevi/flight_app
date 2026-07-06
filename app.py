import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    
    app = QApplication(sys.argv)
    
    
    window = QWidget()
    window.resize(1600, 800)
    window.setWindowTitle('Flight Sim Test Window')
    
    
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()