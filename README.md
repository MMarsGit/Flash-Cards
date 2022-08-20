# Flash-Cards
This application creates flash cards similar to the flash card program Anki. <br>
The difference is that this flash card program takes some inserted text in the txt file and turns each words into a flash card <br>
from most frequent to least frequent. <br>
Additionally, after a flash card is completed it will be set to reappear based on a certain frequency. <br>
That frequency is: 1 day, 3 days, 7 days and then 30 days. <br>
For the translations Bab.la is scraped. <br>

## modules and libraries
PyQt - Used to create a GUI for the program. <br>
BeautifulSoup - Used to scrape Bab.la. <br>
SQLite - Used for database functionality. <br>
