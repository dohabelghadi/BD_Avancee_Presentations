#!/usr/bin/env python3
"""
Vérifie les données dans MongoDB
Une seule commande: python check_data.py
"""

from database import db

print("="*70)
print("🔍 VÉRIFICATEUR DE DONNÉES BFT")
print("="*70)

try:
    # Test connexion
    db.client.server_info()
    print("✅ Connecté à MongoDB sur le port 27018")
except Exception as e:
    print(f"❌ MongoDB non connecté: {e}")
    print("   Lancez: docker-compose up -d")
    print("   Port utilisé: 27018")
    exit()

print("\n📊 STATISTIQUES GÉNÉRALES:")
print("-"*40)

# Compter toutes les données
total_blocks = db.blocks.count_documents({})
total_messages = db.messages.count_documents({})

print(f"Blocs totaux: {total_blocks}")
print(f"Messages totaux: {total_messages}")

# Par algorithme
print("\n📈 PAR ALGORITHME:")
print("-"*40)

for algo in ['pbft', 'tendermint']:
    print(f"\n{algo.upper()}:")
    print("  " + "-"*30)
    
    # Blocs
    blocks = db.blocks.count_documents({'algorithm': algo})
    committed = db.blocks.count_documents({'algorithm': algo, 'committed': True})
    print(f"  Blocs: {blocks} ({committed} commités)")
    
    if blocks > 0 and committed > 0:
        rate = (committed / blocks) * 100
        print(f"  Taux succès: {rate:.1f}%")
    
    # Messages
    messages = db.messages.count_documents({'algorithm': algo})
    print(f"  Messages: {messages}")
    
    # Détail des types de messages
    from pymongo import MongoClient
    temp_client = MongoClient('mongodb://localhost:27018/')
    temp_db = temp_client['bft_simulation']
    
    pipeline = [
        {'$match': {'algorithm': algo}},
        {'$group': {'_id': '$type', 'count': {'$sum': 1}}}
    ]
    
    msg_types = list(temp_db.messages.aggregate(pipeline))
    for msg in msg_types:
        print(f"    {msg['_id']}: {msg['count']}")
    
    # Afficher le dernier bloc
    last_block = temp_db.blocks.find_one(
        {'algorithm': algo},
        sort=[('timestamp', -1)]
    )
    
    if last_block:
        print(f"\n  📦 DERNIER BLOC #{last_block.get('height', 'N/A')}:")
        print(f"    Statut: {'✅ COMMITÉ' if last_block.get('committed') else '❌ EN ATTENTE'}")
        
        if 'transactions' in last_block and last_block['transactions']:
            print(f"    Transactions: {len(last_block['transactions'])}")
            for i, tx in enumerate(last_block['transactions'][:2]):  # Affiche 2 max
                if isinstance(tx, dict):
                    print(f"      {i+1}. {tx.get('type', 'TX')}: {tx.get('from', '?')} → {tx.get('to', '?')}")

print("\n" + "="*70)
print("✅ VÉRIFICATION TERMINÉE")
print("="*70)