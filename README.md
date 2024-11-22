# Gestion de la salle de sport Steel Fist

Ce projet est une application de gestion de données pour une salle de sport, développée avec **SQLModel** pour la gestion des bases de données et **Streamlit** pour l'interface utilisateur. L'application offre différentes fonctionnalités en fonction des rôles des utilisateurs : **admin** ou **utilisateur standard**.

---

## Fonctionnalités

### Pour les Administrateurs :
- **Gestion des Coachs** : Ajouter, modifier et supprimer des coachs.
- **Gestion des Membres** : Ajouter, modifier et supprimer des membres.
- **Gestion des Cours** : Ajouter, modifier et supprimer des cours disponibles dans la salle de sport.

### Pour les Utilisateurs Standards :
- **Inscription aux Cours** : S'inscrire aux cours proposés par la salle de sport.
- **Consultation d'Historique** : Voir l'historique des cours auxquels ils se sont inscrits.

### Authentification :
- Fonctionnalité de **log-in** / **log-out**.
- Gestion des droits d'accès selon le rôle (admin ou utilisateur standard).

---

## Installation

1. **Cloner le dépôt Git**  
   ```bash
   git clone <lien_du_repo>
   cd <nom_du_repo>

2. **Installer les dépendances**
Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée. Ensuite, exécutez :
    ```bash
    pip install -r requirements.txt

3. **Lancer l'application**
Démarrez le serveur Streamlit :
    ```bash
    streamlit run main.py

4. **Configuration de la Base de Données**

L'application utilise SQLModel pour interagir avec la base de données. Voici quelques exemples de requêtes utilisées :

**Rechercher l'ID d'un membre par son nom :**
    
    statement = select(Members.member_id).where(Members.member_name == name)
    name_id = session.exec(statement).first()

**Compter les inscriptions d'un membre :**
    
    statementh = select(func.count(Registrations.registration_id)).where(Registrations.member_id == name_id)

**La structure de la base de données inclut les tables suivantes :**

    
    Members : Liste des membres.
    Accesscards : Liste des accès.
    Coaches : Liste des coachs.
    Courses : Liste des cours.
    Registrations : Suivi des inscriptions aux cours.

## Contributions

Les contributions sont les bienvenues !

Créez une issue pour signaler un bug ou proposer une nouvelle fonctionnalité.
Soumettez une pull request après avoir testé vos modifications.

## Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.
Auteur

Développé par 
@MichAdebayo
Michael Adebayo 
et 
@LudivineRB
Ludivine Raby 🏋️‍♀️.


