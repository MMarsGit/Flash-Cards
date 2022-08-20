import Debug.Debug as Debug
import Classes.Core.Objects.Card as Card

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

#Scene class
class FlashCards(QWidget):
    def __init__(self):
        super().__init__()

        #Default variables
        self.WIDTH = 500
        self.HEIGHT = 500
        self.XPOS = 100
        self.YPOS = 100
        self.TITLE = "Flash Cards"
        self.ICON = ""

        #Instance Variables

        #Call UI creation function
        self.initUI()

    #UI creation functions
    def setupApp(self):
        Debug.log("Setting up app")
        self.resize(self.WIDTH, self.HEIGHT)
        self.move(self.XPOS, self.YPOS)
        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QtGui.QIcon(self.ICON))

    def setupLayout(self):
        Debug.log("setting up layout")
        #main layout
        parentLayout = QVBoxLayout()

        #sub layouts
        #Top row
        topRowLayout = QHBoxLayout()
        self.cardStatusLabel = QLabel()
        self.cardStatusLabel.setProperty("class", "topRow")
        self.cardsLeftLabel = QLabel("?/?")
        self.cardsLeftLabel.setAlignment(Qt.AlignRight)
        self.cardsLeftLabel.setProperty("class", "topRow")
        topRowLayout.addWidget(self.cardStatusLabel)
        topRowLayout.addWidget(self.cardsLeftLabel)
        parentLayout.addLayout(topRowLayout)

        #middle row
        self.cardLabel = QLabel()
        self.cardLabel.setAlignment(Qt.AlignCenter)
        self.cardLabel.setProperty("class", "middleRow")
        parentLayout.addWidget(self.cardLabel)

        #Bottom row
        bottomRowLayout = QHBoxLayout()
        self.wrongButton = QPushButton("Incorrect")
        self.wrongButton.setProperty("class", "bottomRow")
        self.correctButton = QPushButton("Correct")
        self.correctButton.setProperty("class", "bottomRow")
        bottomRowLayout.addWidget(self.wrongButton)
        bottomRowLayout.addWidget(self.correctButton)
        parentLayout.addLayout(bottomRowLayout)

        #set layout
        self.setLayout(parentLayout)
        
    def WidgetActions(self):
        Debug.log("Preparing widget actions")

    def onLoad(self):
        self.card = Card.Card()
        #self.card.getCardfromDb()
        self.card.setWord("new", "Dzien Dobry", "Good Morning")
        self.cardStatusLabel.setText(self.card.status)
        self.cardLabel.setText(self.card.word)

    #UI creation function
    def initUI(self):
        self.setupApp()
        self.setupLayout()
        self.WidgetActions()
        self.onLoad()

