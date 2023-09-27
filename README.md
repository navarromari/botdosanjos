# Augusto dos Anjos Twitter Bot
[@botdosanjos](https://twitter.com/botdosanjos) is a poetry Twitter bot that posts poem excerpts from the Brazilian poet and professor Augusto dos Anjos. Using Google Sheets, Twitter API, and Cloud Schedule, the bot will read the excerpts from an Excel file and tweet them three times a day, at 12:00, 18:00, and 00:00 (Brasília Time (GMT-3)).  

When a tweet is posted, the excerpt is duplicated at the last row of the file, which creates a loop, so the bot never goes inactive.

The author's complete work and source of the tweets are available at https://www.literaturabrasileira.ufsc.br/documentos/?action=download&id=130252

ANJOS, Augusto dos. Obra completa. Alexei Bueno (Org.). Rio de Janeiro: Nova Aguilar, 1995, 883 p.

![image](https://github.com/navarromari/botdosanjos/assets/95860545/899d52e9-aa25-48c2-8690-93d099af1307)

