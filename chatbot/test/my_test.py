import sys

from tensorflow.python.keras.saving.save import load_model
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/') 

from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess

a = load_model('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/models/ner/ner_model.h5')