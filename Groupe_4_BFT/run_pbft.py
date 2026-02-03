
import random
from datetime import datetime
from pymongo import MongoClient

# Connexion MongoDB
client = MongoClient('mongodb://localhost:27018/', serverSelectionTimeoutMS=5000)
db = client['bft_simulation']
blocks = db.blocks
messages = db.messages

print("="*50)
print("  pbft_simulation")
print("="*50)

# Configuration
n = 4
f = 1
view = 0
sequence = 1

print(f"• {n} nœuds (1 byzantin)")
print(f"• Besoin: {2*f} PREPARE et {2*f+1} COMMIT")
print("-"*50)

# Nettoyer
blocks.delete_many({})
messages.delete_many({})

# PHASE 1: PRE-PREPARE
print("\n📤 PHASE 1: PRE-PREPARE")
primary_id = view % n
print(f"Primaires: Nœud {primary_id}")

# Transactions
tx1 = {'type': 'TRANSFER', 'from': 'Alice', 'to': 'Bob', 'amount': 100}
tx2 = {'type': 'STAKE', 'from': 'Charlie', 'to': 'Validator', 'amount': 500}
tx3 = {'type': 'VOTE', 'from': 'David', 'to': 'Proposal', 'amount': 1}
transactions = [tx1, tx2, tx3]

print(f"Transactions: 3 créées")

# Bloc
block = {
    'algorithm': 'pbft',
    'height': sequence,
    'proposer': f"node_{primary_id}",
    'transactions': transactions,
    'timestamp': datetime.now(),
    'committed': False
}
blocks.insert_one(block)

# PHASE 2: PREPARE
print("\n📝 PHASE 2: PREPARE")
prepare_count = 0

for node_id in range(n):
    if node_id == primary_id:
        continue
    
    if node_id == 0:  # byzantin
        if random.random() < 0.4:
            print(f"Nœud {node_id} (byzantin): ❌")
        else:
            print(f"Nœud {node_id} (byzantin): ✅")
            prepare_count += 1
    else:
        print(f"Nœud {node_id}: ✅")
        prepare_count += 1

print(f"PREPARE: {prepare_count}/{2*f}")

if prepare_count >= 2 * f:
    print("✅ Phase 2 réussie")
    
    # PHASE 3: COMMIT
    print("\n💾 PHASE 3: COMMIT")
    commit_count = 0
    
    for node_id in range(n):
        if node_id == 0:  # byzantin
            if random.random() < 0.3:
                print(f"Nœud {node_id} (byzantin): ❌")
            else:
                print(f"Nœud {node_id} (byzantin): ✅")
                commit_count += 1
        else:
            print(f"Nœud {node_id}: ✅")
            commit_count += 1
    
    print(f"COMMIT: {commit_count}/{2*f+1}")
    
    if commit_count >= 2 * f + 1:
        print("\n🎉 CONSENSUS ATTEINT!")
        blocks.update_one({'height': sequence}, {'$set': {'committed': True}})
        print("Bloc #1 COMMITÉ")
    else:
        print("\n❌ Échec COMMIT")
else:
    print("\n❌ Échec PREPARE")
print("\n" + "="*50)