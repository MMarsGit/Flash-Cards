import Debug.Debug as Debug
import sys
import Classes.Scenes.FlashCardScene as FlashCardScene
from PyQt5.QtWidgets import QApplication

def load_scene(scene):

    main = scene
    
    with open("./style/main.qss", "r") as f:
        style = f.read()
    
    main.setStyleSheet(style)
    main.show()
    return main

if __name__ == "__main__":
    Debug.log("--Starting program--")
    #setting up Qt app
    app = QApplication(sys.argv)

    #setting up scene
    scene = FlashCardScene.FlashCards()
    main = load_scene(scene)

    #run
    sys.exit(app.exec_())