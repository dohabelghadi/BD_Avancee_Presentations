import hashlib
import time

class ProofOfWork:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty  # Nombre de zéros requis au début du hash
    
    def mine(self, block_data, previous_hash):
        """
        Simule le minage d'un bloc
        """
        nonce = 0
        start_time = time.time()
        
        while True:
            # Créer la chaîne à hasher
            data_string = f"{block_data}{previous_hash}{nonce}"
            
            # Calculer le hash
            hash_result = hashlib.sha256(data_string.encode()).hexdigest()
            
            # Vérifier si le hash commence par le nombre requis de zéros
            if hash_result[:self.difficulty] == "0" * self.difficulty:
                end_time = time.time()
                mining_time = end_time - start_time
                return {
                    "nonce": nonce,
                    "hash": hash_result,
                    "time": mining_time
                }
            
            nonce += 1
    
    def verify(self, block_data, previous_hash, nonce):
        """
        Vérifie la validité d'un bloc miné
        """
        data_string = f"{block_data}{previous_hash}{nonce}"
        hash_result = hashlib.sha256(data_string.encode()).hexdigest()
        
        return hash_result[:self.difficulty] == "0" * self.difficulty

# Exemple d'utilisation
if __name__ == "__main__":
    pow_system = ProofOfWork(difficulty=4)
    
    # Simuler le minage
    print(" Minage PoW en cours...")
    result = pow_system.mine("Transaction Data", "abc123")
    print(f"Bloc miné !")
    print(f"Nonce trouvé: {result['nonce']}")
    print(f"Hash: {result['hash']}")
    print(f"Temps de minage: {result['time']:.2f} secondes")
    
    # Vérification
    is_valid = pow_system.verify("Transaction Data", "abc123", result['nonce'])
    print(f"Vérification: {'Valide' if is_valid else ' Invalide'}")
