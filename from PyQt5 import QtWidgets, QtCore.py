from PyQt5 import QtGui, QtWidgets, QtCore
import sys

class TranslationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.myColor = '#dee9ef'  
        self.myColor2= '#d3ecfa'
        self.myColor3='#8de0d1'
        self.myColor4='#d3ecfa'
        self.myColor5='#a67b19'
        self.myColor6='#a67b19'

        self.notification = "M57"  # Assuming m().M57 returns a string
        self.nam = "Taraz Software_313 بِسْمِ اللهِ الرَّحْمنِ الرَّحِیم"
        self.myColor = '#dee9ef'
        
        self.setWindowTitle(self.nam)
        self.setGeometry(100, 100, 1100, 669)
        self.setStyleSheet(f"background-color: {self.myColor};")
        
        books = ["قرآن", 'نهج البلاغه', "اصول کافی", "نهج الفصاحه", "حافظ", "سه دقیقه در قیامت"]
        self.book_box = QtWidgets.QComboBox(self)
        self.book_box.addItems(books)
        self.book_box.setFont(QtGui.QFont('Arial', 11, QtGui.QFont.Bold))
        self.book_box.setStyleSheet(f"background-color: {self.myColor4};")
        
        self.var = QtCore.Qt.Unchecked
        self.correction = QtWidgets.QCheckBox("اصلاح لغت فارسی", self)
        self.correction.stateChanged.connect(self.aktive_correction)
        
        fonts = ["Arial", 'Arial (Arabic)', 'Simplified Arabic Fixed',
        'Courier New (Arabic)', 'Urdu Typesetting', 'Sakkal Majalla',
        'Simplified Arabic', 'Traditional Arabic']
        self.font_box = QtWidgets.QComboBox(self)
        self.font_box.addItems(fonts)
        self.font_box.currentTextChanged.connect(self.update_font)

        # Text size dropdown
        self.size_box = QtWidgets.QComboBox(self)
        self.size_box.addItems([str(i) for i in range(8, 90)])
        self.size_box.currentTextChanged.connect(self.update_font)

        # Notification console
        self.notif_console = QtWidgets.QTextEdit(self)
        self.notif_console.setGeometry(10, 487, 777, 30)  # Set position and size
        self.notif_console.setStyleSheet("background-color: white; color: red;")
        self.notif_console.setFont(QtGui.QFont('Arial', 19))
        self.notif_console.setReadOnly(True)
        # ... previous code ...

    # ... previous __init__ method ...

        # Assuming you have defined self.myColor2 and self.myColor4 somewhere in your code
        button_style = "QPushButton { font: bold 11px; background-color: %s; }" % self.myColor2

        # File Button
        self.file_button = QtWidgets.QPushButton("File", self)
        self.file_button.setStyleSheet(button_style)
       # self.file_button.clicked.connect(self.select_file)

        # Translate Button
        self.translate_button = QtWidgets.QPushButton("Translate", self)
        self.translate_button.setStyleSheet(button_style)
       # self.translate_button.clicked.connect(self.translate_button_hit)

        # ... rest of your buttons ...

        # Labels
        self.source_language_label = QtWidgets.QLabel("From language:", self)
        self.source_language_label.setFont(QtGui.QFont('Arial', 10, QtGui.QFont.Bold))

        self.target_language_label = QtWidgets.QLabel("To language:", self)
        self.target_language_label.setFont(QtGui.QFont('Arial', 10, QtGui.QFont.Bold))

    # ... rest of your methods ...

# ... rest of your code ...


    def update_font(self):
        selected_font = self.font_box.currentText()
        selected_size = int(self.size_box.currentText())
        self.new_font = QtGui.QFont(selected_font, selected_size)

    def aktive_correction(self, state):
        if state == QtCore.Qt.Checked:
            self.coorrect_aktive=True
            self.search_Active=True
            self.info2(m().M128)
            self.correct.set(m().M128)
        else:
            self.correct.set(m().M133)
            self.info2(" ")
            self.coorrect_aktive=False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = TranslationWindow()
    mainWin.show()
    sys.exit(app.exec_())
