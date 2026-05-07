# model.py

import torch
import torch.nn as nn
from mesa import Agent, Model
from mesa.time import RandomActivation
import random
import pandas as pd
import datetime as dt
import uuid
import openpyxl
import json
from pracbot import bag_of_words, tokenize  # Ensure you have these imports from your project

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()  # Define ReLU activation here

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)  # Use self.relu
        out = self.l2(out)
        out = self.relu(out)  # Use self.relu
        out = self.l3(out)

        return out

class UserAgent(Agent):
    def __init__(self, unique_id, model, chatbot):
        super().__init__(unique_id, model)
        self.chatbot = chatbot
        self.input_key = f"user_input_{unique_id}"  # Unique key for each agent

    def step(self):
        # User agent interacts with the chatbot
        user_input = input()
        self.chatbot.process_user_input(user_input)


class ChatBotModel(Model):
    def __init__(self, num_agents, chatbot):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.chatbot = chatbot

        # Create user agents
        for i in range(self.num_agents):
            agent = UserAgent(i, self, chatbot)
            self.schedule.add(agent)

    def step(self):
        # Step through user agents
        self.schedule.step()
