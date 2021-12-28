from PySide2 import QtWidgets,QtGui,QtCore
from cryptosteganography import CryptoSteganography
import time
import glob, os
from secure_delete import secure_delete
from PIL import Image
import numpy as np
import shutil
import telepot
import uuid

secure_delete.secure_random_seed_init()
unique_filename = str(uuid.uuid4())

home =os.environ["HOMEPATH"]
directory = "Telegram Desktop"
parent_dir = home +"/Downloads/"
path = os.path.join(parent_dir, directory) 


def generate_random_image(width=58, height=58):
    data=np.random.randint(low=0,high=256,size=128*128*3, dtype=np.uint8)
    data=data.reshape(128,128,3)
    Image.fromarray(data,'RGB').save("base.jpg")



class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        
    def setup_ui(self):
        self.create_Widgets()
        self.create_systray()
        self.modify_widgets()
        self.create_layouts()    
        self.add_widgets_layouts()
        self.setup_connexions()
        self.te_contenu.toPlainText()
        self.setup_css()
        self.te_contenu.setPlaceholderText("Ecrit ton message ici !")
        
        
    
    def create_Widgets(self):
        self.btn_enc =QtWidgets.QPushButton("Encrypt")
        self.btn_dec =QtWidgets.QPushButton("Decrypt")
        self.te_contenu =QtWidgets.QTextEdit()
        self.btn_quit =QtWidgets.QPushButton('Quit')
        self.btn_mini =QtWidgets.QPushButton("minimise")
        self.btn_clean =QtWidgets.QPushButton('Clean')
           
    
    def create_systray(self):
        self.tray =QtWidgets.QSystemTrayIcon()
        icon_path ="C:\\telsec\\secplus.ico"
        self.tray.setIcon(QtGui.QIcon(icon_path))
        self.tray.setVisible(True)
    
    def tray_icon_click(self):
        if self.isHidden():
            self.showNormal()
        else:
            self.hide()
    
    def modify_widgets(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        
        
        radius = 60

        
        self.setStyleSheet( """
        
        color:  #262626;
        border-top-left-radius:{0}px;
        border-bottom-left-radius:{0}px;
        border-top-right-radius:{0}px;
        border-bottom-right-radius:{0}px;                 
    
                    """.format(radius) 
            )

   
    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    
    def  add_widgets_layouts(self): 
        self.main_layout.addWidget(self.btn_enc,0,1,1,1)
        self.main_layout.addWidget(self.btn_dec,0,3,1,1)
        self.main_layout.addWidget(self.te_contenu,1,1,2,3)
        self.main_layout.addWidget(self.btn_quit,3,1,1,1)
        self.main_layout.addWidget(self.btn_mini,3,3,1,1)
        self.main_layout.addWidget(self.btn_clean,0,2,1,1)
    
    def setup_css(self):

                
        self.btn_enc.setStyleSheet( """
        background-color: #1a1a1a;
        color: rgb(1, 255, 98);
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
            
                        """)
                        
        self.btn_dec.setStyleSheet( """
        background-color: #1a1a1a;
        color: rgb(0, 147, 255);
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                 """)
    
        self.te_contenu.setStyleSheet( """
        background-color: #1a1a1a;
        color: beige;
        border-style: outset;
        border-width: 20px;
        border-radius: 90px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)  
        self.btn_mini.setStyleSheet( """
        background-color: #1a1a1a;
        color: yellow;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)
        
        self.btn_quit.setStyleSheet( """
        background-color: #1a1a1a;
        color: red;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)  
       
        self.btn_clean.setStyleSheet( """
        background-color: #1a1a1a;
        color: beige;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)  

    
    def  setup_connexions(self):
        self.btn_enc.clicked.connect(self.bouton_enc_clic)  
        self.btn_dec.clicked.connect(self.bouton_dec_clic)
        self.tray.activated.connect(self.tray_icon_click)
        self.btn_quit.clicked.connect(self.bouton_quit)
        self.btn_mini.clicked.connect(self.tray_icon_click)
        self.btn_clean.clicked.connect(self.bouton_clean)
    
    def bouton_quit(self):
        folder_path = (home+"\\Downloads\\Telegram Desktop\\")
        test = os.listdir(folder_path)
        for images in test:
            if images.endswith(".png"):
                secure_delete.secure_delete(os.path.join(folder_path, images))
                self.close()
        else:
            self.close()
    
    def bouton_clean(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("succes!")
        secure_delete.secure_delete('file.png')
        folder_path = (home+"\\Downloads\\Telegram Desktop\\")
        test = os.listdir(folder_path)
        for images in test:
            if images.endswith(".png"):
                secure_delete.secure_delete(os.path.join(folder_path, images))
        secure_delete.secure_delete('file.png')
        secure_delete.secure_delete('base.jpg')
        self.te_contenu.clear()
        message_box.setText('All cleaned!')
        message_box.exec_()
    
    
       
    def bouton_enc_clic(self):

        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("succes!")
        msg_in_box = self.te_contenu.toPlainText()
        if not msg_in_box:
            return False
        generate_random_image()
        mdp_sec = ("ENCRYPTION-KEY")
        msg_secret = (msg_in_box)
        crypto_steganography = CryptoSteganography(mdp_sec)
            #il prend base.jpg et le transforme en encoded.png en cachant le message secret a l'interieur 
        crypto_steganography.hide('base.jpg',str(unique_filename +'.png'), msg_secret)    
        src1_dir = "C:\\telsec\\"
                 
        time.sleep(2)           
        secure_delete.secure_delete('base.jpg')
            #renomme le fichier encoded.png en file.png
        file_type = '*png'
        files = glob.glob(src1_dir + file_type)
        mao_file = max(files, key=os.path.getctime)
        time.sleep(2)    
             #envoie du fichier sur telegram       
        bot = telepot.Bot('ADD BOT API KEY')
        bot.sendDocument(" ADD GROUP CHAT ID",document=open(mao_file,'rb'))
        time.sleep(2)
        secure_delete.secure_delete(mao_file) 
        self.te_contenu.clear()
        message_box.setText('encrypted!')
        message_box.exec_()
        

    
    def bouton_dec_clic(self):

        src2_dir = home + "\\Downloads\\Telegram Desktop\\"
        dst2_dir = "C:\\telsec\\"
        
        file_type = '*png'
        files = glob.glob(src2_dir + file_type)
        
        try:
            max_file = max(files, key=os.path.getctime)
        except:
            aver_box = QtWidgets.QMessageBox()
            aver_box.setIcon(QtWidgets.QMessageBox.Warning)
            aver_box.setWindowTitle("Avertissement!")
            aver_box.setText("you have a not message!\nThe folder is empty!")
            aver_box.exec_()
            for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
            secure_delete.secure_delete('file.png') 
            
            self.close()
        else: 
            shutil.copy(max_file,dst2_dir)
            
            for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
            #import de la clé de chiffrement
        secret = ("ADD ENCRYPTION KEY")
        crypto_steganography = CryptoSteganography(secret)
        secret = crypto_steganography.retrieve('file.png')
            #afficche le resultat dans une fenétre separé
        self.te_contenu.setText(secret)
        secure_delete.secure_delete('file.png')
        secure_delete.secure_delete(max_file)
        
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)    


app = QtWidgets.QApplication([])
win = App()
win.show()
win.resize(380,380)
app.exec_()    