import json
import random
import torch
from models.model import NeuralNet
from utils.nltk_utils import bag_of_words, tokenize
from config import settings

BOT_NAME = settings.bot_name

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open(settings.intents_file, "r") as json_data:
    intents = json.load(json_data)

data = torch.load(settings.model_trained_file)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return f"{BOT_NAME}: " + random.choice(intent["responses"])

    return "No entiendo tu consulta..."
