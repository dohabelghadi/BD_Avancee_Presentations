import random
from collections import Counter

class DPoSNode:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake
        self.votes = 0
        self.is_delegate = False

class DelegatedProofOfStake:
    def __init__(self, delegate_count=5):
        self.nodes = []
        self.delegates = []
        self.delegate_count = delegate_count
        self.block_producers = []
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def vote_for_delegates(self):
        """
        Simulation du vote : chaque nœud vote avec son stake
        """
        print("Début des votes...")
        
        # Réinitialiser les votes
        for node in self.nodes:
            node.votes = 0
        
        # Chaque nœud vote (simplifié : vote proportionnel au stake)
        for voter in self.nodes:
            # Distribution aléatoire des votes
            vote_power = voter.stake
            candidates = random.sample(self.nodes, min(3, len(self.nodes)))
            
            for candidate in candidates:
                candidate.votes += vote_power / len(candidates)
        
        # Trier par votes et sélectionner les délégués
        self.nodes.sort(key=lambda x: x.votes, reverse=True)
        self.delegates = self.nodes[:self.delegate_count]
        
        for delegate in self.delegates:
            delegate.is_delegate = True
        
        print(" Délégués élus :")
        for i, delegate in enumerate(self.delegates):
            print(f"  {i+1}. {delegate.name} - Votes: {delegate.votes:.2f} - Stake: {delegate.stake}")
    
    def produce_blocks(self, rounds=3):
        """
        Production de blocs par les délégués
        """
        print("\n  Production de blocs :")
        
        for round_num in range(rounds):
            print(f"\nTour {round_num + 1}:")
            
            # Rotation des producteurs de blocs
            start_index = round_num % len(self.delegates)
            block_producers = []
            
            for i in range(min(3, len(self.delegates))):
                index = (start_index + i) % len(self.delegates)
                producer = self.delegates[index]
                block_producers.append(producer)
                
                # Simuler la création d'un bloc
                block_id = f"Block_{round_num+1}_{i+1}"
                print(f"  {producer.name} produit {block_id}")
                
                # Récompense
                reward = producer.stake * 0.005
                print(f"     Récompense: {reward:.2f}")
            
            self.block_producers.append({
                "round": round_num + 1,
                "producers": [p.name for p in block_producers]
            })

# Exemple d'utilisation
if __name__ == "__main__":
    dpos_system = DelegatedProofOfStake(delegate_count=5)
    
    # Créer des nœuds
    nodes_data = [
        ("Alice", 1000),
        ("Bob", 800),
        ("Charlie", 600),
        ("Diana", 400),
        ("Eve", 300),
        ("Frank", 200),
        ("Grace", 150),
        ("Henry", 100)
    ]
    
    for name, stake in nodes_data:
        dpos_system.add_node(DPoSNode(name, stake))
    
    # Élection des délégués
    dpos_system.vote_for_delegates()
    
    # Production de blocs
    dpos_system.produce_blocks(rounds=3)
