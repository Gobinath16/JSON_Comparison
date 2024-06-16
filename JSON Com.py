import os
import json
import sip
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QWidget, QCheckBox, QTextEdit, QLabel
import sys
MASTER_FOLDER_PATH = ""    // Local Directory path where the JSON was stored
def show_warning(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Alert")
    msg.setText(message)
    msg.exec_()
def search_clicked(input_box):
    folder_name = input_box.text().strip()
    if folder_name == "":
        show_warning("Please enter a folder name.")
        return

    folder_path = os.path.join(MASTER_FOLDER_PATH, folder_name)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
        if files:
            show_warning("Files found in folder '{}':\n{}".format(folder_name, ", ".join(files)))
        else:
            show_warning("No JSON files found in folder '{}'.".format(folder_name))
    else:
        show_warning("Folder '{}' not found.".format(folder_name))

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 800, 500)
    win.setWindowTitle("Comparator")
    win.setStyleSheet("background-color: light-blue;")
    input_box = QLineEdit(win)
    input_box.setPlaceholderText("Enter the MTID")
    input_box.setGeometry(50, 20, 400, 35)  # Adjust the geometry as needed
    input_box.setStyleSheet("padding: 10px; border-radius: 10px; background-color: white;")

  
    search_button = QPushButton("Search", win)
    search_button.setGeometry(460, 20, 60, 35)  # Adjust the geometry as needed
    search_button.setStyleSheet(
        """
        QPushButton {
            padding: 10px;
            background-color: lightgray;
            border: none;
            border-radius: 10px; /* Adjust the value as needed */
        }
        QPushButton:hover {
            background-color: lightgreen;
        }
        """
    )
   
    search_button.clicked.connect(lambda: search_clicked(input_box))

  
    show_raw_checkbox = QCheckBox("", win)  # No text
    show_raw_checkbox.setGeometry(50, 60, 30, 30)  # Adjust the geometry as needed
   
    show_raw_checkbox.setStyleSheet(
        """
        QCheckBox::indicator {
            width: 25px;
            height: 25px;
        }
        QCheckBox::indicator:checked {
            image: "C:\\Users\\Gobinath M\\Documents\\Python\\Tool\\icons\\check-mark.png"; /* Replace 'check_mark.png' with your checkmark icon */
        }
        """
    )

 
    show_raw_label = QLabel("Show Raw Data", win)
    show_raw_label.setGeometry(80, 60, 120, 30)  # Adjust the geometry as needed


    compare_button = QPushButton("Compare", win)
    compare_button.setGeometry(540, 20, 70, 35)  # Adjust the geometry as needed
    compare_button.setStyleSheet(
        """
        QPushButton {
            padding: 10px;
            background-color: lightgray;
            border: none;
            border-radius: 10px; /* Adjust the value as needed */
        }
        QPushButton:hover {
            background-color: lightgreen;
        }
        """
    )

    
    text_edit1 = QTextEdit(win)
    text_edit1.setGeometry(50, 100, 350, 300)  # Adjust the geometry as needed
    text_edit1.setStyleSheet("padding: 10px; border-radius: 10px; background-color: white;")

   
    text_edit2 = QTextEdit(win)
    text_edit2.setGeometry(410, 100, 350, 300)  # Adjust the geometry as needed
    text_edit2.setStyleSheet("padding: 10px; border-radius: 10px; background-color: white;")
    
    win.show()
    sys.exit(app.exec_())

window()
