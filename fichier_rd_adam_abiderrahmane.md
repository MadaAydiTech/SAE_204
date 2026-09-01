# SAÉ2.04-3 — Infrastructure AD avec Samba
**Adam ABIDERRAHMANE**
## Description et objectif :
L'objectif est de mettre en place une infrastructure de partage de fichiers
Samba respectant le cahier des charges suivant :

| Groupe  | Utilisateur | Répertoire |
|---------|-------------|------------------------|
| cmoi    | moi         | amoi                   |
| ctoi    | toi         | atoi                   |
| cnous   | nous        | anous                  |

**Droits :**
- `cmoi` : lecture sur `amoi`, `atoi`, `anous` — écriture sur `amoi`
- `ctoi` : lecture sur `atoi`, `anous` — écriture sur `atoi`
- `cnous` : lecture et écriture sur `anous`
- `public` : lecture/écriture pour tous
- `amoi-atoi` : `cmoi` lecture/écriture, `ctoi` lecture seule
- `amoi-anous` : `cmoi` lecture/écriture, `cnous` lecture seule

## Contenu du dépôt

- `Dockerfile` : construit une image basée sur `dperson/samba` avec les
  répertoires de partage déjà créés.
- `docker-compose.yml` : orchestre la construction de l'image et le
  démarrage du conteneur avec tous les utilisateurs et partages configurés
  automatiquement (basé sur l'exemple officiel du github de dperson :
  https://github.com/dperson/samba).
- `fichier_rd_adam_abiderrahmane.md` : détail de toutes les commandes testées question par
  question, avec leurs résultats et des commentaires explicatifs.

### Prérequis

- Docker installé et fonctionnel

## Procédure pour reproduire automatiquement les partages
### Étapes

1. **Construire l'image et démarrer le conteneur en une seule commande :**

   ```bash
   docker compose up -d
   ```

   Cette commande :
   - construit l'image Docker à partir du `Dockerfile` (image basée sur
     `dperson/samba` avec les répertoires de partage pré-créés) ;
   - démarre le conteneur `samba-q14` avec tous les utilisateurs (`moi`,
     `toi`, `nous`) et tous les partages (`public`, `amoi`, `atoi`, `anous`,
     `amoi-atoi`, `amoi-anous`) déjà configurés, sans aucune autre action
     manuelle.

2. **Vérifier que le conteneur tourne :**

   ```bash
   docker ps | grep samba-q14
   ```

3. **Tester l'accès aux partages :**

   ```bash
   # Trouver l'IP du conteneur (si le réseau n'est pas en mode host)
   docker inspect samba-q14 | grep IPAddress

   # Se connecter à un partage (mot de passe : Moi12345 pour "moi")
   smbclient //<IP_du_conteneur>/public -U moi
   smbclient //<IP_du_conteneur>/amoi -U moi
   smbclient //<IP_du_conteneur>/atoi -U toi
   smbclient //<IP_du_conteneur>/anous -U nous
   ```

   Identifiants de test :
   | Utilisateur | Mot de passe |
   |-------------|---------------|
   | moi         | Moi12345      |
   | toi         | Toi12345      |
   | nous        | Nous1234      |

4. **Arrêter et supprimer le conteneur (si besoin) :**

   ```bash
   docker compose down
   ```

### Sans Docker Compose (commande unique)

Il est également possible de tout reproduire avec l'image `dperson/samba`
directement, sans Dockerfile ni Compose, via une unique commande
`docker run` (voir Partie III, Question 13, détaillée dans
`fichier_rd_adam_abiderrahmane.md`) :

```bash
docker run -it -d --name samba-manuel --net=host --privileged \
  -v /partage:/partage \
  dperson/samba -p \
  -S -n -w "WORKGROUP" \
  -u "moi;Moi12345" \
  -u "toi;Toi12345" \
  -u "nous;Nous1234" \
  -s "public;/partage/public;yes;no;yes" \
  -s "amoi;/partage/amoi;no;no;no;moi" \
  -s "atoi;/partage/atoi;no;no;no;toi" \
  -s "anous;/partage/anous;no;no;no;nous" \
  -s "amoi-atoi;/partage/amoi-atoi;no;no;no;moi" \
  -s "amoi-anous;/partage/amoi-anous;no;no;no;moi"
```

## Résumé de la démarche 
Ce travail illustre une progression d'automatisation :

1. **Configuration manuelle** (Partie 1, conteneur Ubuntu) — édition
   directe de `/etc/samba/smb.conf`, création manuelle des groupes,
   utilisateurs et droits Linux.
2. **Image pré-configurée avec scripts** (Partie 3, Q12 — image
   `ahmetozer/samba`) — utilisation de scripts dédiés (`shareadd`,
   `sharelist`, `shareshow`, `sharedel`, `reload-samba`) pour gérer les
   partages sans éditer le fichier de configuration à la main.
3. **Configuration en une commande** (Partie 3, Q13 — image
   `dperson/samba`) — toute la configuration (utilisateurs + partages)
   est passée en paramètres d'une seule commande `docker run`.
4. **Infrastructure** (Partie 4, Q14 — Dockerfile + Compose) —
   la configuration est versionnée dans des fichiers texte reproductibles
   à l'identique sur n'importe quelle machine avec une seule commande
   `docker compose up -d`.