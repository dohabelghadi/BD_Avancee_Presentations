#!/usr/bin/env python3
import random
from datetime import datetime
from pymongo import MongoClient

# Connexion MongoDB
client = MongoClient('mongodb://localhost:27018/', serverSelectionTimeoutMS=5000)
db = client['bft_simulation']
blocks = db.blocks
messages = db.messages

print("="*50)
print("  TENDERMINT - ROUNDS")
print("="*50)

# Configuration
n = 4
height = 1
round_num = 0
required = (2 * n) // 3 + 1

print(f"• {n} nœuds (1 byzantin)")
print(f"• Besoin: {required}/{n} votes (2/3+)")
print("-"*50)

# Nettoyer
blocks.delete_many({'algorithm': 'tendermint'})
messages.delete_many({'algorithm': 'tendermint'})

# PHASE 1: PROPOSE
print("\n📤 PHASE 1: PROPOSE")
proposer_id = (height + round_num) % n
print(f"Proposer: Nœud {proposer_id}")

# Transactions
tx1 = {'type': 'TRANSFER', 'from': 'Wallet_A', 'to': 'Wallet_X', 'amount': 100}
tx2 = {'type': 'DELEGATE', 'from': 'Wallet_B', 'to': 'Validator', 'amount': 200}
transactions = [tx1, tx2]

print(f"Transactions: 2 créées")

# Bloc
block = {
    'algorithm': 'tendermint',
    'height': height,
    'round': round_num,
    'proposer': f"node_{proposer_id}",
    'transactions': transactions,
    'timestamp': datetime.now(),
    'committed': False
}
blocks.insert_one(block)

# PHASE 2: PREVOTE
print("\n🗳️  PHASE 2: PREVOTE")
prevotes_yes = 0

for node_id in range(n):
    if node_id == 0:  # byzantin
        if random.random() > 0.6:
            print(f"Nœud {node_id} (byzantin): ❌")
        else:
            print(f"Nœud {node_id} (byzantin): ✅")
            prevotes_yes += 1
    else:
        print(f"Nœud {node_id}: ✅")
        prevotes_yes += 1

print(f"PREVOTE: {prevotes_yes}/{required}")

if prevotes_yes >= required:
    print("✅ Phase 2 réussie")
    
    # PHASE 3: PRECOMMIT
    print("\n💾 PHASE 3: PRECOMMIT")
    precommits_yes = 0
    
    for node_id in range(n):
        if node_id == 0:  # byzantin
            if random.random() > 0.4:
                print(f"Nœud {node_id} (byzantin): ✅")
                precommits_yes += 1
            else:
                print(f"Nœud {node_id} (byzantin): ❌")
        else:
            print(f"Nœud {node_id}: ✅")
            precommits_yes += 1
    
    print(f"PRECOMMIT: {precommits_yes}/{required}")
    
    if precommits_yes >= required:
        print("\n🎉 CONSENSUS ATTEINT!")
        blocks.update_one({'height': height}, {'$set': {'committed': True}})
        print("Bloc #1 FINALISÉ")
    else:
        print("\n❌ Échec PRECOMMIT")
else:
    print("\n❌ Échec PREVOTE")
print("\n" + "="*50)

