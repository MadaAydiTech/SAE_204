# SAE_204_toutes_les_parties (il y'en a 4 différentes toutes sont reliés)

Ce projet regroupe les travaux pratiques et déploiements réalisés dans le cadre de la **SAÉ 2.04** que j'ai effectué en 2026 lors de mon 2ème semestre. Il couvre le développement web couplé à des scripts python, la mise en place d'une infrastructure de Téléphonie sur IP (VoIP), ainsi que le déploiement conteneurisé d'un service de partage de fichiers sécurisé.

---

La SAÉ 2.04 est articulée autour de **4 parties complémentaires** :

### Partie 1 Art Mathématique (Symfony + Python)
Développement d'une application web dynamique permettant de générer et d'afficher des œuvres d'art mathématique à partir de scripts Python exécutés en arrière-plan.
* **Stack technique** : Symfony (PHP), Python, Apache, Linux.
* **Fonctionnalités** :
  * Exécution de scripts Python via le composant `Symfony\Component\Process` (avec les boutons : *courbe de Von Koch*, *nées carrées*, *Morellet*).
  * Traitement dynamique des formulaires HTML (transmission de paramètres comme le hasard ou encore la grille de ma figure).
  * Sécurisation de l'accès au site via authentification HTTP Basic (`.htaccess` / `.htpasswd`).
  * Gestion du rendu dynamique d'images dans les vues Twig.

---
### Partie 2 Script Python & Art Mathématique : François Morellet
Conception d'un script Python autonome s'inspirant d'une œuvre célèbre, puis déformation algorithmique par l'aléatoire et intégration au site web.

* **Stack technique** : Python, Pygame, PIL.
* **Œuvre choisie** : François Morellet — *Répartition aléatoire du rouge au jaune suivant progression* (Figure 61/77, 1970).
* **Démarche & Déformation** :
  * **Analyse de la figure de base** : Implémentation d'une grille avec placement régulier d'une case sur deux (`if colonne % 2 == 0 and ligne % 2 == 0`).
  * **Ajout d'aléatoire & Détournement** : Augmentation du nombre de couleurs (10 couleurs chaudes), variation aléatoire des tailles (`random.randint`), alternance dynamique entre carrés et cercles, puis superposition d'un visuel de clown (`pygame.image.load` et `blit`) au centre du décor.
  * **Évolution libre** : Libération des contraintes de grille pour une répartition 100 % hasardeuse des formes sur les axes $x$ et $y$.
  * **Intégration Symfony Headless** : Utilisation du composant `pygame.Surface` combiné à la variable d'environnement `SDL_VIDEODRIVER="dummy"` pour forcer la génération de l'image en mémoire sur le serveur Debian sans affichage graphique.
---
### Partie 3 Partage de Fichiers & Contrôle d'Accès (Samba & Docker sans samba-tools)
Déploiement d'un service de stockage réseau centralisé (SMB/CIFS) avec gestion fine des droits d'accès utilisateurs et groupes.
* **Stack technique** : Samba, Docker, Docker Compose, Portainer, Linux CIFS.
* **Réalisations** :
  * Migration d'une approche de configuration manuelle vers une solution **entièrement conteneurisée et automatisée** (`docker-compose.yml`).
  * Mise en place d'une matrice de droits stricte : répertoires personnels isolés, répertoires partagés par groupe et zone publique en lecture seule.
  * Résolution de contraintes d'isolation réseau inter-conteneurs et tests de validation croisés via CLI (`smbclient`) et GUI (`cifs`).

---

### Partie 4 Téléphonie sur IP (IPBX Asterisk et utilisation du cloud AWS)
Conception et déploiement de l'infrastructure téléphonique VoIP complète pour un atelier d'artistes.
* **Stack technique** : FreePBX (Asterisk), Protocoles SIP, Softphones (microSIP).
* **Architecture & Règles métier** :
  * **Plan de numérotation** : quatres extensions SIP pour les artistes + numéros SDA directs pour accès immédiat.
  * **Serveur Vocal Interactif (SVI / IVR)** : Routage des appels entrants via menu à touches depuis le numéro principal (`0466666666`).
  * **Conditions Temporelles (Time Conditions)** : Gestion des plages horaires (08h-18h, 7j/7), des nuits et de la fermeture annuelle (juillet-août) avec diffusion d'annonces vocales adaptées.
  * **Messagerie vocale** : Redirection automatique des appels vers la boîte vocale en cas d'absence du destinataire.
---
