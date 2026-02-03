import random
import hashlib
import time

class Validator:
    def __init__(self, address, stake):
        self.address = address
        self.stake = stake  # Montant détenu
        self.age = 0  # Âge des coins (pour certains PoS)

class ProofOfStake:
    def __init__(self):
        self.validators = []
        self.total_stake = 0
    
    def add_validator(self, validator):
        self.validators.append(validator)
        self.total_stake += validator.stake
    
    def select_validator(self):
        """
        Sélectionne un validateur proportionnellement à son stake
        """
        if not self.validators:
            return None
        
        # Méthode 1: Aléatoire pondéré par le stake
        selection_point = random.uniform(0, self.total_stake)
        current_sum = 0
        
        for validator in self.validators:
            current_sum += validator.stake
            if current_sum >= selection_point:
                return validator
        
        return self.validators[-1]
    
    def create_block(self, validator, transactions):
        """
        Crée un bloc avec le validateur sélectionné
        """
        timestamp = time.time()
        block_data = {
            "validator": validator.address,
            "stake": validator.stake,
            "transactions": transactions,
            "timestamp": timestamp,
            "previous_hash": self.get_last_hash()
        }
        
        # Simuler la création du bloc
        block_hash = hashlib.sha256(str(block_data).encode()).hexdigest()
        
        # Récompense (simplifiée)
        reward = validator.stake * 0.01  # Récompense proportionnelle au stake
        
        return {
            "block": block_data,
            "hash": block_hash,
            "reward": reward
        }

# Exemple d'utilisation
if __name__ == "__main__":
    pos_system = ProofOfStake()
    
    # Ajouter des validateurs
    validators = [
        Validator("Alice", 1000),
        Validator("Bob", 500),
        Validator("Charlie", 300),
        Validator("Diana", 200)
    ]
    
    for v in validators:
        pos_system.add_validator(v)
    
    print(" Sélection PoS en cours...")
    for i in range(5):
        selected = pos_system.select_validator()
        print(f"Tour {i+1}: {selected.address} sélectionné (stake: {selected.stake})")
        
        # Créer un bloc
        block = pos_system.create_block(selected, ["tx1", "tx2", "tx3"])
        print(f"   Bloc créé, récompense: {block['reward']:.2f}")
