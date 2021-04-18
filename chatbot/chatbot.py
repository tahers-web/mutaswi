from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('BankBot')
training_data_quesans = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans
trainer = ListTrainer(chatbot.storage)
trainer.train(training_data) 

trainer = ChatterBotCorpusTrainer(chatbot.storage)
trainer.train("chatterbot.corpus.english")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")
