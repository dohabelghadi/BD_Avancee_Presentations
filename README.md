# 🚀 CFT Algorithms: Paxos & Raft

Implémentation des algorithmes de consensus **Raft** et **Paxos** en Python avec persistance MongoDB.

## 📚 À Propos

Ce projet démontre le fonctionnement de deux algorithmes de consensus distribués tolérants aux pannes (Crash Fault Tolerant):

- **Raft**: Algorithme de consensus avec élection de leader et réplication de log
- **Paxos**: Algorithme de consensus classique (Basic Paxos)

## 🏗️ Architecture

- **3 nœuds** pour chaque algorithme
- **MongoDB** pour la persistance de l'état
- **Flask** pour l'API REST
- **Requests** pour la communication inter-nœuds

## 📦 Installation

### Prérequis

- Python 3.8+
- Docker & Docker Compose
- Git

### Étapes
```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/CFT-Paxos-Raft.git
cd CFT-Paxos-Raft

# 2. Créer l'environnement virtuel
python -m venv .venv

# 3. Activer l'environnement
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Linux/Mac:
source .venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Démarrer MongoDB
cd docker
docker-compose up -d
cd ..
```

## 🚀 Utilisation

### Démarrer Raft

Ouvrez 3 terminaux et exécutez:
```bash
# Terminal 1
python raft/raft_server.py 1

# Terminal 2
python raft/raft_server.py 2

# Terminal 3
python raft/raft_server.py 3
```

### Démarrer Paxos
```bash
# Terminal 1
python paxos/paxos_server.py 1

# Terminal 2
python paxos/paxos_server.py 2

# Terminal 3
python paxos/paxos_server.py 3
```

### Tests Manuels
```bash
python tests/manual_test.py
```

## 📊 API Endpoints

### Raft

- `GET /status` - État du nœud
- `GET /health` - Health check
- `POST /client_request` - Soumettre une commande
- `POST /request_vote` - RPC RequestVote (interne)
- `POST /append_entries` - RPC AppendEntries (interne)

### Paxos

- `GET /status` - État du nœud
- `GET /health` - Health check
- `POST /propose` - Proposer une valeur
- `POST /prepare` - Phase 1a Prepare (interne)
- `POST /accept` - Phase 2a Accept (interne)
- `POST /learn` - Learner (interne)

## 🧪 Tests

### Test Manuel
```bash
python tests/manual_test.py
```

### Tests Automatiques (TODO)
```bash
pytest tests/test_raft.py -v
pytest tests/test_paxos.py -v
```

## 📖 Comment Ça Marche?

### Raft

1. **Élection de Leader**: Les nœuds démarrent en tant que followers. Si un timeout se produit, une élection commence
2. **Réplication de Log**: Le leader reçoit les commandes clients et les réplique sur tous les followers
3. **Commit**: Une fois qu'une majorité a répliqué, l'entrée est committée

### Paxos

1. **Phase 1 (Prepare)**: Le proposeur demande la permission aux accepteurs
2. **Phase 2 (Accept)**: Le proposeur demande l'acceptation d'une valeur
3. **Learn**: Une fois acceptée par la majorité, la valeur est apprise par tous

## 🔧 Configuration

Les ports par défaut:

- **Raft**: 5001, 5002, 5003
- **Paxos**: 6001, 6002, 6003
- **MongoDB**: 27017, 27018, 27019

Modifiez dans `*_server.py` si nécessaire.

## 🐛 Dépannage

### MongoDB ne démarre pas
```bash
cd docker
docker-compose down
docker-compose up -d
```

### Port déjà utilisé

Modifiez les ports dans les fichiers `*_server.py` ou arrêtez le processus existant.

### Modules non trouvés
```bash
pip install -r requirements.txt
```

## 📝 Licence

MIT

## 👥 Auteur

Yasmine FaTih - [GitHub](https://github.com/yasminefatih)

## 🙏 Remerciements

- Diego Ongaro pour Raft
- Leslie Lamport pour Paxos
```

---

## ✅ VÉRIFICATION FINALE

Voici tous les fichiers que vous devez avoir:
```
CFT-Paxos-Raft/
├── .gitignore ✅
├── README.md ✅
├── requirements.txt ✅
│
├── docker/
│   └── docker-compose.yml ✅
│
├── raft/
│   ├── __init__.py ✅
│   ├── raft_node.py ✅
│   └── raft_server.py ✅
│
├── paxos/
│   ├── __init__.py ✅
│   ├── paxos_node.py ✅
│   └── paxos_server.py ✅
│
├── tests/
│   ├── __init__.py ✅
│   └── manual_test.py ✅
│
└── utils/
    └── __init__.py ✅