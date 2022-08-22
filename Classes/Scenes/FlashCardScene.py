from Classes.Core.Scrape import search_PolishEng
import Debug.Debug as Debug
import Classes.Core.Objects.Card as Card
import Classes.Core.ProcessFile as ProcessFile
import time

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
        #Card Status
        self.cardStatusLabel = QLabel()
        self.cardStatusLabel.setProperty("class", "topRow")
        #Menu Button
        self.generateButton = QPushButton("Generate")
        self.generateButton.setProperty("class", "topRow")
        #Card lefts
        self.cardsLeftLabel = QLabel("?/?")
        self.cardsLeftLabel.setAlignment(Qt.AlignRight)
        self.cardsLeftLabel.setProperty("class", "topRow")
        #Setup top row
        topRowLayout.addWidget(self.cardStatusLabel)
        topRowLayout.addWidget(self.generateButton)
        topRowLayout.addWidget(self.cardsLeftLabel)
        parentLayout.addLayout(topRowLayout)

        #middle row
        self.cardLabel = QLabel()
        self.cardLabel.setAlignment(Qt.AlignCenter)
        self.cardLabel.setProperty("class", "middleRow")
        parentLayout.addWidget(self.cardLabel)

        #Bottom row
        bottomRowLayout = QHBoxLayout()
        #Wrong button
        self.wrongButton = QPushButton("Incorrect")
        self.wrongButton.setProperty("class", "bottomRow")
        #flip button
        self.flipButton = QPushButton("Flip")
        self.flipButton.setProperty("class", "bottomRow")
        #right button
        self.correctButton = QPushButton("Correct")
        self.correctButton.setProperty("class", "bottomRow")
        #Add to bottom row
        bottomRowLayout.addWidget(self.wrongButton)
        bottomRowLayout.addWidget(self.flipButton)
        bottomRowLayout.addWidget(self.correctButton)
        parentLayout.addLayout(bottomRowLayout)

        #set layout
        self.setLayout(parentLayout)
        
    def WidgetActions(self):
        Debug.log("Preparing widget actions")
        self.generateButton.clicked.connect(self.generateButtonPressed)
        self.flipButton.clicked.connect(self.flipButtonPressed)

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

    def generateButtonPressed(self):
        Debug.log("Generate Button Pressed")
        #intiate variables
        stringLations = []

        #Setup card names
        dict = ProcessFile.processTxT()
        cardNames = ProcessFile.sortByFrequency(dict)

        for index in range(len(cardNames)):
            #Get translations
            print(cardNames[index])
            translations = search_PolishEng(cardNames[index])
            #translations to string
            for lation in translations:
                stringLations += str(lation) + ", "
            #Turn to cards
            self.card.setWord("new", cardNames[index], stringLations)
            self.cardStatusLabel.setText(self.card.status)
            self.cardLabel.setText(self.card.word)

            time.sleep(0.5)

    def flipButtonPressed(self):
        self.cardLabel.setText(self.card.translation)
