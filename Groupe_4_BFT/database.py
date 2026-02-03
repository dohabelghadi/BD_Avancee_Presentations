from pymongo import MongoClient
from datetime import datetime
import random

class DatabaseManager:
    def __init__(self):
        # Connexion à MongoDB sur le PORT 27018
        self.client = MongoClient('mongodb://localhost:27018/', serverSelectionTimeoutMS=5000)
        self.db = self.client['bft_simulation']
        
        # Collections
        self.blocks = self.db.blocks
        self.messages = self.db.messages
        
        print("📦 Base de données initialisée")
    
    def cleanup(self):
        """Nettoie les données précédentes"""
        try:
            self.blocks.delete_many({})
            self.messages.delete_many({})
            print("🗑️  Données nettoyées")
        except Exception as e:
            print(f"⚠️  Erreur nettoyage: {e}")
    
    def save_block(self, block_data):
        """Sauvegarde un bloc"""
        try:
            self.blocks.insert_one(block_data)
            return True
        except Exception as e:
            print(f"❌ Erreur sauvegarde bloc: {e}")
            return False
    
    def save_message(self, message_data):
        """Sauvegarde un message"""
        try:
            self.messages.insert_one(message_data)
            return True
        except Exception as e:
            print(f"❌ Erreur sauvegarde message: {e}")
            return False
    
    def test_connection(self):
        """Teste la connexion à MongoDB"""
        try:
            self.client.server_info()
            print("✅ Connecté à MongoDB (port 27018)")
            return True
        except Exception as e:
            print(f"❌ Erreur connexion MongoDB: {e}")
            print("   Lancez: docker-compose up -d")
            print("   Port utilisé: 27018 (car 27017 est peut-être occupé)")
            return False

# Instance globale
db = DatabaseManager()