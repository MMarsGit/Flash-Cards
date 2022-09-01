from asyncio.windows_events import NULL
from tkinter import Y
from Classes.Core.Scrape import search_PolishEng
import Debug.Debug as Debug
import Classes.Core.Objects.Card as Card
import Classes.Core.ProcessFile as ProcessFile
import time
import Classes.Core.database as Database
from datetime import date, datetime, timedelta

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

#Scene class
class FlashCards(QWidget):
    def __init__(self):
        super().__init__()

        #Default variables
        self.WIDTH = 1024
        self.HEIGHT = 640
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
    
    #Links actions to functions
    def WidgetActions(self):
        Debug.log("Preparing widget actions")
        self.generateButton.clicked.connect(self.generateButtonPressed)
        self.flipButton.clicked.connect(self.flipButtonPressed)
        self.wrongButton.clicked.connect(self.wrongButtonPressed)
        self.correctButton.clicked.connect(self.correctButtonPressed)

    #Code to be executed at the start
    def onLoad(self):
        Debug.isDebug = True
        #setup database
        self.db = Database.database()
        firstRecord = self.db.get_first_record()
        self.cardCount = int(firstRecord[0])
        self.lastid = self.db.get_last_row_id()

        #setup first card
        self.card = Card.Card()
        self.card.setWord(firstRecord[1], firstRecord[2], firstRecord[3])
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
        stringLations = ""

        #Setup card names
        dict = ProcessFile.processTxT()
        cardNames = ProcessFile.sortByFrequency(dict)

        #Wipe table
        
        self.db.delete_table()
        self.db.create_table()

        for index in range(len(cardNames)):
            #Get translations
            print(cardNames[index])
            translations = search_PolishEng(cardNames[index])
            #translations to string
            for lation in translations:
                stringLations += str(lation + ", ")
            Debug.debug("Stringlations: " + stringLations)
            stringLations = stringLations.rstrip(", ")
            #Turn to cards
            self.card.setWord("new", cardNames[index], stringLations)
            #add card to table
            self.db.insert_card(self.card)
            stringLations = ""
            time.sleep(0.5)

        #set first card to label
        self.cardStatusLabel.setText(self.card.status)
        self.cardLabel.setText(self.card.word)

    def flipButtonPressed(self):
        self.cardLabel.setText(self.card.translation)

    def wrongButtonPressed(self):
        self.cardCount+=1
        repetitions = 0
        nextAppearance = str(date.today())
        self.db.updateRepetitions(repetitions, nextAppearance, self.card.word)

        if (self.cardCount <= int(self.lastid[0])):
            #Get next card & update label - maybe add to card.py
            currentCard = self.db.get_record(self.cardCount)
            if (currentCard[5] == None):
                currentCardDate = date.today()
            else:
                print(str(currentCard[5]))
                currentCardDate = datetime.strptime(str(currentCard[5]), "%Y-%m-%d").date()
            
            if (currentCardDate <= date.today()):

                Debug.debug("Current card: " + str(currentCard))
                self.card.setWord(currentCard[1], currentCard[2], currentCard[3])
                self.cardStatusLabel.setText(self.card.status)
                self.cardLabel.setText(self.card.word)
            else:
                self.cardCount +=1

    def correctButtonPressed(self):
        
        
        currentCard = self.db.get_record(self.cardCount)
        print(currentCard)
        #Spaced repetition
        if (currentCard[4] == None):
            currentReps = 0
        else:
            currentReps = int(currentCard[4])
        if (currentReps == 0):
            repetitions = 1
            nextAppearance = str(date.today() + timedelta(days=3))
            self.db.updateRepetitions(repetitions,nextAppearance, self.card.word)

        elif (currentReps == 1):
            repetitions = 2
            nextAppearance = str(date.today() + timedelta(days=7))
            self.db.updateRepetitions(repetitions,nextAppearance, self.card.word)

        elif (currentReps == 2):
            repetitions = 3
            nextAppearance = str(date.today() + timedelta(days=30))
            self.db.updateRepetitions(repetitions,nextAppearance, self.card.word)

        self.cardCount+=1
        if (self.cardCount <= int(self.lastid[0])):
            #Get next card & update label - maybe add to card.py
            currentCard = self.db.get_record(self.cardCount)
            Debug.debug("Current card: " + str(currentCard))
            self.card.setWord(currentCard[1], currentCard[2], currentCard[3])
            self.cardStatusLabel.setText(self.card.status)
            self.cardLabel.setText(self.card.word)
        