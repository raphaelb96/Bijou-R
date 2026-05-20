# BIJOU-R — PLAN STRATÉGIQUE COMPLET
### Version 3 · Réflexion Opus · 20 mai 2026
> Ce document est la source de vérité de tout le projet Bijou-R.
> Ne rien mettre en œuvre sans avoir lu ce document en entier.

---

## NOTE IMPORTANTE
Le site de référence mentionné n'a pas été reçu dans la conversation — à renvoyer dès que possible.
En attendant, les références utilisées sont : **Messika.com** (luxe FR), **Mejuri.com** (émotion), **James Allen** (configurateur diamants), **Brilliant Earth** (tunnel fiançailles), **Vrai.com** (DTC lab diamonds).

---

# ARCHITECTURE GLOBALE DU PROJET

```
                    ┌──────────────────────────┐
                    │      SHOPIFY ADVANCED     │
                    │  bijou-r.com  (core)      │
                    │  ┌─────────┬──────────┐   │
                    │  │CATALOGUE│CONFIGURTR│   │
                    │  │ normal  │  bague   │   │
                    │  └─────────┴──────────┘   │
                    └──────────┬───────────────┘
                               │ webhooks
              ┌────────────────┴────────────────┐
              ▼                                 ▼
      ┌───────────────┐                 ┌──────────────────┐
      │  n8n (VPS)    │                 │     Klaviyo      │
      │ Orchestrateur ├─────────────────► 18 flows email   │
      └─┬──┬──┬──┬───┘                 └──────────────────┘
        │  │  │  │
        ▼  ▼  ▼  ▼
   ┌──────┐ ┌──────┐ ┌───────┐ ┌──────────────┐
   │Firely│ │Meshy │ │Claude │ │ ManyChat     │
   │ API  │ │AI 3D │ │  API  │ │ IG + TikTok  │
   │(photo│ │(GLB) │ │(blog  │ │              │
   │ IA)  │ │      │ │ auto) │ │              │
   └──────┘ └──────┘ └───────┘ └──────────────┘
        ▲
        │
   ┌────┴────────────┐
   │ Google Ads      │
   │ Meta Ads        │
   │ TikTok Ads      │
   │ Triple Whale    │
   └─────────────────┘
```

**Pile technique complète :**

| Outil | Rôle | Prix/mois |
|---|---|---|
| Shopify Advanced | Core boutique + checkout + multi-marché | 240 € |
| n8n (VPS Hetzner) | Orchestrateur automations | 10 € |
| Klaviyo | Email + SMS (18 flows) | 0-45 € |
| Adobe Firefly API | Génération photos produit IA | 250 € |
| Meshy AI Pro | Génération modèles 3D (.glb) | 25 € |
| Claude API | Rédaction articles blog auto | Variable |
| Gorgias | Helpdesk SAV centralisé | 60 € |
| Triple Whale | Analytics unifié (ROAS réel) | 130 € |
| Airtable | PIM produits + calendrier éditorial | 25 € |
| Cloudinary | CDN images + transformations | 50 € |
| ManyChat | Bots IG + TikTok | 15 € |
| Metricool | Scheduling réseaux sociaux | 30 € |
| Loox | Avis photos UGC | 10 € |

---

# PARTIE 1 — FONDATIONS

## ÉTAPE 1 — DOMAINE ET EMAILS

### Domaine
- **Priorité absolue :** acheter `bijou-r.com` avant tout le reste
- Plateformes : Namecheap (~10 $/an) ou directement via Shopify Domains
- Acheter aussi `.fr` et `.co.il` si le budget le permet (redirection vers .com)
- Connecter dans Shopify : Paramètres → Domaines → Connecter un domaine existant

### Emails (après achat du domaine)
- Google Workspace (~6 $/mois pour 5 comptes)

| Adresse | Usage |
|---|---|
| `hello@bijou-r.com` | Contact client principal |
| `commandes@bijou-r.com` | SMTP Shopify pour confirmations |
| `support@bijou-r.com` | SAV / Gorgias |
| `pro@bijou-r.com` | Collabs influenceurs / B2B |

---

## ÉTAPE 2 — SHOPIFY CONFIGURATION

### Plan
- **Advanced (240 €/mois)** — obligatoire pour : Shopify Flow + multi-marché FR/IL natif + checkout extensions

### Thème
- **Impulse** (Archetype Themes, 380 $) ou **Prestige** (Maestrooo, 320 $)
- Pas Dawn (gratuit) : il manque les sections lookbook, le drawer cart upsell, et le support natif 3D bien intégré
- Personnalisations clés à appliquer dès le départ :
  - Police : Cormorant Garamond (titres) + Inter (corps de texte)
  - Palette : noir `#0A0A0A` + blanc cassé `#FAF7F2` + or champagne `#C9A961`
  - Animation hover produit : zoom 1.05x + switch photo studio → photo portée
  - Navigation transparente qui se solidifie au scroll

### Pages à créer

| Page | Contenu essentiel |
|---|---|
| **Home** | Vidéo héro 8s, piliers USP, bracelet tennis ancre, catégories, témoignages, teaser configurateur, capture email |
| **À propos / La Maison** | Storytelling fondateur, atelier, philosophie |
| **Notre Atelier** | Process fabrication, certifications RJC / Kimberley Process |
| **Le Journal** | Blog AEO (cf Partie 4) |
| **Créer ma bague** | Configurateur bague personnalisée (cf Partie 3) |
| **Guide des tailles** | Tableau FR/IL/US + méthode mesure |
| **Garantie à vie** | Couverture, formulaire activation |
| **Livraison & Retours** | FR 48h gratuit >150€, IL DHL 3-5j, retours 30j |
| **FAQ** | 25-30 questions structurées avec schema FAQPage |
| **Programme fidélité** | Cercle Bijou-R — paliers Or/Platine/Diamant |
| **Carte cadeau** | 50/100/250/500/1000 € |
| **Contact** | Formulaire + WhatsApp |
| **Pages légales** | CGV, CGU, Mentions, Confidentialité, Retours |

### Paiements (dans cet ordre)

1. **Shopify Payments** (FR EUR) — Visa/Mastercard/CB
2. **Stripe** (IL ILS) — Shopify Payments non disponible en Israël
3. **PayPal Express** (FR + IL)
4. **Apple Pay + Google Pay** (automatique)
5. **Alma** (paiement 3x/4x — plus français que Klarna) — crucial sur paniers >300 €
6. **Klarna** (paiement 4x — couverture internationale)
7. **Bit / Tranzila** — paiement local israélien (indispensable pour le marché IL)
8. Cryptos via Coinbase Commerce (optionnel, niche luxe)

Configuration **Shopify Markets** : FR (EUR), IL (ILS), EU (EUR), Monde (EUR). Géolocalisation IP + sélecteur manuel de devise en header.

### Metafields produits (namespace `bijour`)

| Champ | Type | Description |
|---|---|---|
| `bijour.materiau` | text | Acier 316L / Plaqué or / Or massif |
| `bijour.carats_or` | number | 14 / 18 / 24 |
| `bijour.pierre_principale` | text | Diamant / Saphir / Rubis |
| `bijour.carat_pierre` | decimal | ex: 2.0 |
| `bijour.purete_diamant` | text | VS1 / VVS / SI1 |
| `bijour.couleur_diamant` | text | D / E / F / G |
| `bijour.certification` | file | PDF certificat GIA/IGI |
| `bijour.poids_grammes` | decimal | ex: 8.5 |
| `bijour.origine` | text | France / Italie |
| `bijour.delai_fabrication` | number | En jours |
| `bijour.modele_3d` | file | URL .glb (auto-rempli par pipeline Meshy) |
| `bijour.story` | multiline | Histoire de la pièce |

### Trust signals (sur toutes les fiches produit)

- Bandeau certifications : RJC, Kimberley Process, Made in France
- Badge "Garantie à vie" visible
- Badge "Paiement 100% sécurisé 3D Secure"
- Bloc "Vu dans" (logos presse — à obtenir)
- SIRET + adresse atelier en footer
- Numéro de téléphone + WhatsApp visibles

---

# PARTIE 2 — OPTIMISATION ÉMOTIONNELLE DU SITE

## LA PHILOSOPHIE : "L'effet vitrine Place Vendôme"

Un client qui entre sur Bijou-R doit ressentir en moins de **3 secondes** :
1. **Légitimité** — "C'est une vraie maison de joaillerie"
2. **Désir** — "Je veux toucher / posséder / offrir"
3. **Appartenance** — "C'est pour des gens comme moi"

**Règle des 3 sorties :** aucun visiteur ne quitte sans **acheter**, **donner son email**, ou **être obsédé** par un produit (retargeting déclenché).

---

## LES 5 DÉCLENCHEURS ÉMOTIONNELS BIJOUTERIE

| Déclencheur | Cible psychologique | Application Bijou-R |
|---|---|---|
| **IDENTITÉ** | "Ce bijou dit qui je suis" | Copy : "La femme Bijou-R ose, brille, transmet" |
| **AMOUR** | Cadeau, alliance, fiançailles | Tunnel "Pour Elle / Pour Lui" + configurateur |
| **STATUT** | Réussite, signe extérieur | Prix ancre 24 990 €, certificats GIA, packaging luxe |
| **SELF-LOVE** | "Je me l'offre" | Copy : "Vous n'avez besoin de personne pour briller" |
| **TRANSMISSION** | Héritage, génération | "Le bijou que votre fille portera dans 30 ans" |

---

## ARCHITECTURE ÉMOTIONNELLE PAGE PAR PAGE

### A. HOMEPAGE — "Le premier coup d'œil"

**Zone visible sans scroll (above the fold) :**

```
[VIDÉO HÉRO — 8 secondes en boucle silencieuse]
Plan 1 : macro d'un diamant qui tourne, lumière qui joue
Plan 2 : main féminine qui ferme un fermoir bracelet tennis
Plan 3 : coupe rapide — le bracelet glisse sur le poignet

Bouton son optionnel [♪] → ASMR : tintement de chaînes

[HEADLINE]
"Le bijou que vous porterez toute votre vie."

[SOUS-HEADLINE]
"Diamants certifiés GIA. Sertissage à la main. Livraison sécurisée en 48h."

[CTA PRINCIPAL]          [CTA SECONDAIRE]
"Je découvre"           "Créer ma bague unique →"
```

**Sections homepage dans l'ordre (stratégique) :**

1. **Bandeau "As Seen In"** — logos Vogue, Elle, Marie Claire (à obtenir, placement RP)
2. **Best-sellers** avec badge "127 personnes regardent" (Fomo app)
3. **Catégories visuelles** — Bracelets / Colliers / Bagues / Boucles (photos macro, pas catalogue)
4. **"Pourquoi Bijou-R"** — 4 piliers (Diamants certifiés / Atelier français / Garantie à vie / Livraison sécurisée)
5. **Section "Le Signature"** — bracelet tennis ancre 24 990 € en hero, seul, majestueux
6. **Teaser configurateur** — "Créez la bague qu'aucune autre femme ne possède →"
7. **Témoignages vidéo** — UGC clientes qui montrent leur bijou
8. **Derniers articles du Journal** (AEO + retour visites)
9. **Capture email** — "Recevez notre guide *Choisir son diamant* + 10% sur votre 1ère commande"

---

### B. PAGE CATÉGORIE — "Le rayon"

- **Bannière héro** avec citation émotionnelle spécifique :
  > *"Un bracelet tennis, c'est l'élégance qui ne demande pas la parole."*
- **Filtres intelligents** : Métal / Carats / Budget / Occasion (Mariage, Anniversaire, Self-gift)
- **Tri par défaut** : "Coup de cœur" (ordre manuel choisi — pas alphabétique)
- **Hover sur produit** : switch vers photo portée + apparition prix
- **Badges dynamiques** : "Plus que 2 en stock" / "Nouveauté" / "Le préféré des clientes" / "Vu 89 fois aujourd'hui"
- **Mini-quiz flottant** : "Pas sûre ? Trouvez VOTRE bijou en 30 secondes →" (capture email + segmente Klaviyo)

---

### C. FICHE PRODUIT — "Le moment du désir"

**Layout desktop :**

```
[GALERIE — 60% gauche]            [INFOS — 40% droite]
  Photo 1 : macro studio           Nom du bijou
  Photo 2 : portée (poignet/cou)   "Sertie à la main à Paris"
  Photo 3 : échelle (avec main)
  Photo 4 : détail sertissage      Prix : 1 290 €
  Photo 5 : packaging écrin        ou 4x 322,50€ sans frais (Alma)
  Vidéo 360° ASMR
  VIEWER 3D NATIF SHOPIFY           Description courte (3 lignes émo.)
  [Bouton AR sur mobile]
                                    Sélecteur taille + guide popup
                                    Sélecteur métal (Or jaune/blanc/rose)
                                    Gravure offerte → champ 15 car.
                                    [Preview gravure sur 3D live]

                                    ┌──────────────────────────┐
                                    │   "Elle est pour moi →"  │
                                    └──────────────────────────┘

                                    "Essayer virtuellement (AR)"

                                    ⏱ Commandez dans 4h 12min
                                    → Livraison garantie mercredi

                                    [Accordéons]
                                    ✓ Caractéristiques techniques
                                    ✓ Certificat GIA (PDF)
                                    ✓ Livraison & retour
                                    ✓ Garantie à vie
```

**Sous le fold :**
- **Histoire du bijou** — 2 paragraphes émotionnels + inspiration
- **Vidéo atelier** 15 secondes : l'artisan qui sertit (sans son)
- **Section unboxing** : 4 photos packaging — boîte cuir, écrin velours, carte manuscrite, chiffon soie
- **Reviews photos** (Loox / Judge.me) — minimum 12 avant ouverture
- **"Souvent acheté avec"** — cross-sell (écrin supplémentaire, entretien)
- **"Vous pourriez aussi aimer"** — modèles similaires
- **FAQ produit** (schema FAQPage — 5-8 questions spécifiques au produit)

---

### D. PANIER — "L'instant fragile"

C'est ici qu'on perd 70% des clients. Tout doit rassurer et accélérer.

- **Panier slide-in** (pas nouvelle page — rester dans le flow)
- **Image macro du bijou** + nom + prix + gravure si choisie
- **Barre de progression** : "Plus que 290 € pour la livraison express offerte 🚚"
- **Garanties répétées** sous le CTA :
  - "Livraison sécurisée FedEx assurée"
  - "Retour gratuit 30 jours"
  - "Garantie à vie"
- **Upsell intelligent** : "Ajoutez l'écrin de voyage (49€) — offert au-delà de 2 000 €"
- **CTA** : "Finaliser mon écrin →" (pas "Payer")
- **Alma/Klarna affiché** : "Payez en 4 fois sans frais"

---

### E. CHECKOUT — "Zéro friction"

- **Shopify Pay / Apple Pay / Google Pay** en haut de page (one-click)
- Email capturé en premier (même si abandon → flow Klaviyo)
- Pas de création de compte obligatoire
- "Vos données sont chiffrées SSL 256-bit" sous chaque étape
- Récap visuel du bijou toujours visible à droite
- Badge "Verified by Stripe" + logos cartes
- Champ "Code promo" discret (pas en évidence — sinon les clients sortent chercher un code)

---

### F. POST-ACHAT — "Le client devient ambassadeur"

```
Page de confirmation (pas juste un récap commande) :

"Bravo. Vous venez de choisir un bijou que vous porterez
toute votre vie."

[Vidéo 20 secondes : préparation du colis dans l'atelier,
ruban doré, cire de sceau, carte manuscrite]

CE QUI ARRIVE MAINTENANT :
✓ Aujourd'hui : votre bijou est confié à notre maître-sertisseur
✓ Demain : contrôle qualité + emballage à la main
✓ J+2 : départ FedEx assuré
✓ J+3 : il est entre vos mains

[Tracker visuel animé]

PENDANT L'ATTENTE :
→ Téléchargez le guide d'entretien de votre bijou
→ Rejoignez notre cercle privé Instagram (@bijou.r)
→ Parrainez une amie : 50€ pour elle, 50€ pour vous

[CTA bonus]
"Composez VOTRE prochaine pièce →" (vers configurateur)
```

---

## MICRO-MOMENTS D'ÉMOTION (les détails qui transforment)

| Moment | Implémentation | Impact |
|---|---|---|
| Hover produit | Switch photo studio → portée + zoom 1.05x | +18% temps page |
| Scroll homepage | Parallaxe douce, fade-in textes | Premium feel |
| Son ASMR | Bouton optionnel : tintement chaînes, écrin qui s'ouvre | Mémorable, partageable |
| Ouverture fiche produit | Bijou "apparaît" en 0.4s, fondu depuis fond blanc | Effet vitrine |
| Ajout au panier | Animation : le bijou vole vers l'icône panier | Gamification |
| Viewer 3D | Rotation auto 5s puis attente interaction | Engagement +35% |
| Gravure live | Le texte apparaît sur le bijou 3D en temps réel | Attachement instantané |
| Exit intent | Popup : "Avant de partir... 10% sur votre 1ère commande" | Récupère 8% |
| Email capture | Popup après 30s OU 50% scroll — jamais immédiat | +12% conversions |

---

## FOMO, SCARCITÉ, PREUVE SOCIALE

**À placer stratégiquement :**

- Homepage : "Rejoint par 14 287 femmes qui aiment les vrais bijoux"
- Catégorie : badges live "Vu 23 fois cette heure"
- Fiche produit :
  - "Plus que 3 en stock" (réel — basé sur inventaire Shopify)
  - "5 personnes regardent cette pièce" (Fomo app)
  - "Camille de Lyon a acheté ce bracelet il y a 12 minutes" (notif sociale)
- Panier : "Votre panier est réservé 15 minutes" (timer doux)
- Checkout : "Livraison express disponible pour la Fête des Mères — commandez avant le 22/05"

**Apps recommandées :** Fomo, Loox, Trustoo, Back in Stock

---

## STRATÉGIE DE RÉDUCTIONS (sans dévaluer la marque)

**Règle absolue :** jamais de "-50%" sur la homepage. Une maison de joaillerie ne brade pas.

| Mécanisme | Application | Effet psychologique |
|---|---|---|
| **Welcome offer** | -10% via email 1ère commande | Capture email + entry premium |
| **Gravure offerte** | À partir de 500 € | Valeur ajoutée, pas remise |
| **Écrin de voyage** | Offert au-delà de 2 000 € | Cadeau, pas discount |
| **Livraison express** | Offerte au-delà de 800 € | Service premium |
| **Cercle Bijou-R VIP** | Après 1er achat : -15% à vie + prélancement | Fidélité |
| **Parrainage** | 50 € parrain + 50 € filleul | Bouche-à-oreille |
| **Birthday gift** | -20% le mois d'anniversaire | Émotionnel pur |
| **Diamond Days** (2x/an) | "Nos diamants à tarif atelier — 72h" | Événementiel, justifié |

**À bannir :** Black Friday classique (-30-40%), codes "BIJOU10" affichés partout, popups remise agressifs sur la homepage.

---

## COPY ÉMOTIONNEL — EXEMPLES CONCRETS

**Headlines :**
- "Le bijou n'est pas un accessoire. C'est une mémoire qu'on porte."
- "Elle ne se demande pas si on la remarque. Elle le sait."
- "Pour les femmes qui ne demandent pas la permission de briller."
- "Ce que vous portez, vos petites-filles le porteront aussi."

**CTA émotionnels (jamais "Acheter") :**

| Contexte | CTA |
|---|---|
| Homepage | "Je découvre →" |
| Catégorie | "Voir cette pièce →" |
| Fiche produit | **"Elle est pour moi"** |
| Configurateur | "Je crée ma bague unique →" |
| Newsletter | "Je rejoins le cercle Bijou-R" |
| Panier | "Finaliser mon écrin →" |
| Wishlist | "Garder ce bijou en mémoire" |

**Structure description produit :**

```
[Accroche émotionnelle — 1 ligne]
"Elle se glisse au poignet comme une promesse silencieuse."

[Histoire courte — 3 lignes]
"Inspirée des bracelets portés par Chris Evert en 1987, cette pièce
réunit 4,2 carats de diamants brillants certifiés GIA, sertis
à la main dans notre atelier parisien."

[Caractéristiques techniques — bullets]
✓ Or 18 carats — 18,4g
✓ 47 diamants taille brillant — 4,2 ct total
✓ Couleur F-G / Pureté VS1-VS2
✓ Certificat GIA inclus
✓ Garantie à vie

[Réassurance finale]
"Livrée dans son écrin de cuir, accompagnée du certificat d'authenticité
signé par notre maître-joaillier."
```

---

## EXPÉRIENCE UNBOXING — Vendue AVANT l'achat

**Section dédiée sur chaque fiche produit — carrousel 5 photos :**

```
Photo 1 : Boîte extérieure cuir noir, logo Bijou-R à chaud en doré
Photo 2 : Ouverture de la boîte (point de vue main, effet unboxing)
Photo 3 : Écrin intérieur velours, bijou serti
Photo 4 : Carte manuscrite + certificat sur papier vergé
Photo 5 : Sachet de soie + chiffon d'entretien monogrammé

Caption :
"Chaque bijou Bijou-R arrive comme un événement. Écrin de cuir signé,
certificat sur papier vergé, carte manuscrite. Parce que recevoir
un bijou ne devrait jamais ressembler à recevoir un colis."
```

---

## STRATÉGIE PRIX ANCRE (LE BANGER)

**Catalogue structuré en 5 niveaux :**

| Position | Produit | Prix € | Rôle |
|---|---|---|---|
| **ANCRE** | Bracelet Tennis Signature Or Blanc 18k 2ct | **24 990 €** | Choque. Légitime TOUT. |
| **PREMIUM** | Tennis Or Blanc 18k 1ct | 6 990 € | Aspiration |
| **BESTSELLER** | Tennis Or Jaune 14k | 2 490 € | Sweet spot marge + volume |
| **ENTRÉE** | Tennis Vermeil 0.5ct | 890 € | 1er achat |
| **TRAFIC** | Tennis Argent | 290 € | Volume + cadeau |

**Gamification Alma sur le bestseller :**
> "4 × 622 € sans frais" — psychologiquement, 2 490 € devient digérable.

**Comparatif affiché dans le configurateur :**
> "Pour la même bague chez Tiffany : env. 12 500 €
> Pour la même bague chez Cartier : env. 14 200 €
> Bijou-R, atelier direct : 7 480 €"

---

## PERSONNALISATION = ATTACHEMENT INSTANTANÉ

| Personnalisation | Bijoux | Surcoût | Délai |
|---|---|---|---|
| Gravure intérieure (15 car.) | Bagues, bracelets | Offerte | +3j |
| Gravure extérieure | Médailles | +50 € | +5j |
| Pierre de naissance | Colliers symboliques | Inclus | +2j |
| Initiale pendentif | Colliers | Inclus | +2j |
| Taille sur mesure | Bagues | Inclus | +7j |
| Carte calligraphe | Toute commande >500 € | Offerte | +1j |

**Effet clé :** un bijou gravé ne se retourne pas. Taux de retour divisé par 4.

---

# PARTIE 3 — VIEWER 3D ET GÉNÉRATION AUTOMATIQUE

## VIEWER 3D NATIF SHOPIFY

**Shopify supporte le 3D nativement** via `model-viewer` (Google). Il suffit d'uploader un `.glb` ou `.gltf` dans les médias produit.

**Ce que le client voit :**
- Rotation 360° libre (doigt sur mobile, souris sur desktop)
- Pinch to zoom
- Éclairage HDR automatique (reflets or et brillance pierres)
- **Bouton "Voir en AR"** sur iOS (AR Quick Look) et Android (Scene Viewer)
- Pour les bagues : voir la bague en réalité augmentée sur sa main réelle

**Aucune app supplémentaire nécessaire** pour le rendu de base. Zakeke à ajouter si gravure live en 3D voulue.

---

## MESHY AI — PIPELINE AUTOMATIQUE PHOTO → 3D

**Meshy.ai** génère des modèles 3D `.glb` depuis des photos produit. Mode `surface_mode: "hard"` + PBR = reflets métalliques et brillance pierres bien rendus.

**API Meshy :**

```
POST https://api.meshy.ai/v2/image-to-3d
Headers: Authorization: Bearer {MESHY_API_KEY}
Body: {
  "image_url": "https://...(photo produit)",
  "enable_pbr": true,
  "surface_mode": "hard",
  "topology": "quad",
  "target_polycount": 30000
}
→ Retourne task_id

GET https://api.meshy.ai/v2/image-to-3d/{task_id}
→ Poll jusqu'à "succeeded" → model_urls.glb
```

**Prix :** ~20 $/mois Pro (~1 crédit par modèle).

---

## ADOBE FIREFLY API — PIPELINE PHOTOS AUTOMATIQUES

**Endpoints principaux :**

| Endpoint | Usage |
|---|---|
| `POST /v3/images/generate` | Visuel lifestyle depuis prompt texte |
| `POST /v3/images/fill` | Mettre un fond luxe sur photo bijou |
| `POST /v3/images/expand` | Packshot carré → bannière / story |
| `POST /v3/images/generate-object-composite` | **Placer le bijou dans un décor IA** |

**Auth :** OAuth Server-to-Server via Adobe Developer Console.

---

## PIPELINE AUTOMATION COMPLET (n8n)

```
Shopify webhook : products/create
        │
        ├──────────────────────────┐
        ▼                          ▼
[PHOTOS — Firefly]        [MODÈLE 3D — Meshy]
        │                          │
Adobe IMS → access_token  Meshy API image-to-3d
        │                          │
Upload photo → /storage   Poll toutes les 10s
        │                          │
generate-object-composite Download .glb
(×4 variantes)                     │
        │                 Shopify : upload media
Download × 4              MODEL_3D type
        │
Cloudinary CDN
        │
Upload → Shopify images
        │
        └──────────── Slack : "Approuver ?" ──────────────┐
                                                           │
                                              [Bouton OUI] → push
                                              [Bouton NON] → discard
```

**Durée totale :** 5-15 minutes par produit, 100% automatique.

**Prompts Firefly :**

```
Bracelet tennis :
"Sparkling diamond tennis bracelet on polished black marble,
dramatic studio lighting, deep shadows, luxury jewelry editorial,
Vogue style, 8k hyperrealistic"

Bague solitaire :
"Elegant diamond solitaire ring on female hand, natural sunlight,
minimalist white background, Hasselblad H6D, 100mm macro,
f/2.8 bokeh, premium jewelry photography"
```

---

# PARTIE 4 — CONFIGURATEUR BAGUE PERSONNALISÉE

## VISION

Le configurateur est la **machine à conversion premium** de Bijou-R. Ticket moyen : 4 500-15 000 €.

URL dédiée : `bijou-r.com/creer-ma-bague`

Ce n'est pas juste un outil — c'est une expérience. Le client crée quelque chose d'unique et s'y attache avant même de l'avoir acheté.

---

## PAGE D'ENTRÉE DU TUNNEL

```
[Vidéo fullscreen : main qui dessine une bague à l'encre,
fade vers une bague réelle qui apparaît]

"Créez la bague qu'aucune autre femme ne possède."
"En 8 étapes. En 5 minutes. Pour la vie."

[CTA principal]
"Commencer ma création →"

[CTA secondaire]
"Voir les bagues déjà créées" (galerie inspiration)

[Trust badges]
✓ Diamants certifiés GIA & IGI
✓ Atelier français — sertissage main
✓ Livraison sécurisée 21 jours
✓ Garantie à vie + assurance perte
✓ Visioconférence avec un expert gratuite
```

---

## LES 8 ÉTAPES DU TUNNEL

### ÉTAPE 1 — L'occasion (segmentation émotionnelle)

```
"Cette bague, c'est pour quelle occasion ?"

[6 cartes visuelles cliquables]
💍 Demande en mariage
💎 Alliance de mariage
🎁 Cadeau pour elle
💖 Cadeau pour moi (self-love)
🎉 Célébrer un événement
✨ Just because
```

*Note : cette étape segmente le tunnel — "Demande en mariage" → on insiste sur l'émotion, écrin spécial, service vidéaste.*

---

### ÉTAPE 2 — Style de monture

```
[Grille 6 styles avec viewer 3D miniature qui tourne]
• Solitaire classique
• Solitaire avec pavé
• Trilogie
• Halo
• Toi & Moi
• Vintage / Art Déco

[Prix indicatif à droite, mis à jour en temps réel]
"À partir de 2 400 €"
```

---

### ÉTAPE 3 — Métal

```
[4 options en macro]
• Or jaune 18 carats (+0€)
• Or rose 18 carats (+0€)
• Or blanc 18 carats (+0€)
• Platine 950 (+800€)

[Pour chaque, texte émotionnel]
"Or rose — Chaleureux, contemporain, parfait pour les peaux claires"
"Platine 950 — Le métal noble, le plus résistant, choisi par
les grandes maisons de joaillerie (+800€)"

[Viewer 3D live : la monture choisie s'affiche dans le métal choisi]
```

---

### ÉTAPE 4 — Forme du diamant

```
[Grille 8 formes avec rendu 3D]
• Rond (Brillant) — le plus brillant
• Princesse — carré moderne
• Coussin — vintage romantique
• Ovale — allonge le doigt
• Émeraude — élégance Art Déco
• Poire — signature personnelle
• Marquise — drame & singularité
• Cœur — audace pure
```

---

### ÉTAPE 5 — Origine du diamant (CHOIX CLÉ)

```
[Deux cartes côte à côte]

🌍 DIAMANT NATUREL              💎 DIAMANT DE LABORATOIRE
Formé il y a 3 milliards         Créé dans nos labs partenaires
d'années                         français
Rareté absolue                   Chimiquement identique
Investissement & transmission    40-60% moins cher
Certificat GIA                   Certificat IGI
À partir de 4 800 €/carat        À partir de 1 900 €/carat

[Lien] "Comprendre la différence →" (modal éducatif)
```

---

### ÉTAPE 6 — Caractéristiques 4C

**6A — Carats :**
```
[Slider visuel 0.3ct → 5ct — la bague grossit visuellement]
[Prix mis à jour en live à chaque mouvement du slider]
[Tip] "1 carat = taille moyenne, choix le plus populaire"
```

**6B — Couleur :**
```
[Slider D → K avec dégradé visuel]
[Reco IA] "Pour 1 carat, F-G est imperceptible à l'œil, économise 1 200€"
```

**6C — Pureté :**
```
[Slider FL → SI2]
[Reco IA] "VS1-VS2 : aucune inclusion visible à l'œil nu"
```

**6D — Catalogue diamants réels :**
```
[MODE 1] "Je veux choisir le diamant exact"
→ Catalogue de diamants EN STOCK avec :
  - Vidéo 360° HD du diamant réel
  - Photos plan rapproché
  - Certificat GIA/IGI PDF téléchargeable
  - Prix exact
  (Style James Allen)

[MODE 2] "Je laisse Bijou-R choisir"
→ "Nos gemmologues sélectionnent le diamant avec le meilleur
   rapport qualité/lumière du stock selon vos critères."
```

---

### ÉTAPE 7 — Détails finaux

```
[Sélecteur taille] + lien "Comment connaître ma taille ?"
[Baguier gratuit] → commande un baguier papier envoyé à domicile

[Gravure intérieure — offerte]
Champ 15 caractères + preview en temps réel sur le 3D
"Une date, des initiales, un secret..."

[Options]
• Pierres latérales / pavé sur l'anneau (+X€)
• Écrin spécial "Demande en mariage" (+89€)
• 🎬 Service "Vidéaste pour la demande" (+1 200€)
  ← DIFFÉRENCIANT ABSOLU — aucun concurrent ne le propose
```

---

### ÉTAPE 8 — Récap & Achat

```
[À gauche : Viewer 3D fullscreen — rotation auto + AR]

[À droite : Récap]
"VOTRE BAGUE UNIQUE AU MONDE"

✓ Solitaire halo — Or rose 18ct
✓ Diamant naturel ovale 1.2ct — F/VS1 — GIA n°2186524835
✓ Pavé latéral 0.18ct
✓ Taille 53 — Gravure "S & D — 14.06.26"
✓ Écrin demande en mariage

[Prix total]  7 480 €
              ou 4× 1 870€ sans frais (Alma)

[Comparatif affiché]
"Tiffany : env. 12 500€ | Cartier : env. 14 200€"

[3 CTAs]
🟡 "Je commande ma bague →"
🔵 "Parler à un expert (visio gratuite)"
⚪ "Sauvegarder ma création"

[Réassurances finales]
✓ Livraison sécurisée 21j FedEx assuré
✓ Garantie à vie — SAV à vie
✓ Assurance perte/vol 1ère année offerte
✓ Modification possible dans les 48h
✓ Retour 30j — remboursement intégral
```

---

## UX ÉMOTIONNEL DU CONFIGURATEUR

| Principe | Application |
|---|---|
| **Progress bar émotionnelle** | "Vous êtes à 60% de votre création unique" + barre dorée |
| **Jamais de page-load** | Transitions fluides 300-500ms entre étapes |
| **Viewer 3D toujours visible** | La bague évolue à chaque choix |
| **Prix dynamique** | Affiché en haut, anime à chaque clic |
| **Encouragements** | "Magnifique choix" / "Cette monture est notre best-seller" |
| **Sauvegarde auto** | Email envoyé avec lien de reprise (Klaviyo) |
| **Aide contextuelle** | Bouton "?" sur chaque champ + chat Gorgias |

---

## GAMIFICATION DU PRIX

```
Étape 2 — monture solitaire         "À partir de 2 400 €"
Étape 3 — platine                   "2 400 € → 3 200 € ✨"
Étape 5 — diamant naturel           "3 200 € → +pierre"
Étape 6 — 1.2ct F/VS1               "Diamant : +5 760 €"
                                     ━━━━━━━━━━━━━━━━━━━
                                     TOTAL : 7 480 €

Sous le total :
"Pour la même bague chez Tiffany : env. 12 500 €"
"Chez Cartier : env. 14 200 €"
```

---

## IMPLÉMENTATION TECHNIQUE

### Option A — Apps Shopify (rapide, budget limité)
- **Zakeke 3D Customizer** (~$59-499/mois)
- Limite : peu flexible pour le tunnel émotionnel précis voulu

### Option B — Custom Liquid + Vue.js + Three.js ← RECOMMANDÉ
- Page custom `/pages/creer-ma-bague`
- Front : **Three.js** ou **Babylon.js** pour le viewer 3D
- Tunnel : **Vue.js** ou **Alpine.js** dans le Liquid
- Stock diamants : Airtable + n8n (sync temps réel)
- Création produit final : Shopify Admin API crée un produit "custom" éphémère à la volée

### Option C — Shopify Hydrogen (headless, React) ← Phase 2
- Liberté totale UX, animations premium
- Coût dev : 30-60k€ initial
- À envisager à 100k€ de CA mensuel

---

## STOCK DE DIAMANTS (Style James Allen)

**Sources fournisseurs :**
- **RapNet** (réseau mondial diamantaires, API disponible)
- **IDEX** (alternative)
- **VDB** (Virtual Diamond Boutique)
- Pour les lab-grown : **WD Lab Grown**, **Diamond Foundry**

**Champs de la base diamants (Airtable) :**

| Champ | Source |
|---|---|
| N° certificat GIA/IGI | Fournisseur |
| Forme / Carats / Couleur / Pureté | Certificat |
| Taille (cut) / Polissage / Symétrie | Certificat |
| Prix HT fournisseur | Fournisseur |
| Prix vente Bijou-R | Calcul auto (markup ×2.5-3) |
| URL vidéo 360° du diamant | Fournisseur |
| URL PDF certificat | Fournisseur |
| Disponible en stock | Boolean |

---

## REDIRECTIONS VERS LE CONFIGURATEUR

1. **Fiche produit bague** — bloc en bas :
   > "Vous voulez quelque chose d'UNIQUE ? Créez VOTRE bague →"

2. **Catégorie Bagues** — bannière :
   > "Aucune bague ne vous correspond ? Composez la vôtre →"

3. **Menu principal** — item dédié "Créer ma bague" en gras/doré

4. **Popup contextuel** — si >2 min sur catégorie bagues sans clic :
   > "Envie d'une bague qui n'existe nulle part ailleurs ?"

5. **Homepage** — section dédiée avec la vidéo d'intro du configurateur

---

# PARTIE 5 — APPLICATIONS SHOPIFY

| App | Usage | Prix/mois |
|---|---|---|
| **Klaviyo** | Email + SMS automation | 0-45 € |
| **Loox** | Avis avec photos UGC | ~10 € |
| **Judge.me** | Avis + étoiles schema | Gratuit |
| **Fomo** | Notifications sociales live | ~20 € |
| **Searchanise** | Search avancée + filtres metafields | ~19 € |
| **Tidio** | Chat live + bot | Gratuit |
| **Hextom Shipping Bar** | Barre livraison offerte | Gratuit |
| **Back in Stock** | Alerte réassort | ~20 € |
| **Shopify Flow** | Automations natives | Gratuit (Advanced) |
| **Gorgias** | SAV centralisé | ~60 € |
| **ReConvert** | Upsell post-achat | ~5 € |
| **Zakeke** | Viewer 3D + gravure live | ~50 € |
| **Vitals** | SEO + popups + social proof | ~30 € |
| **Bundler** | Sets + bundles | Gratuit |
| **Stocky** | Gestion stock + prévisions | ~79 € |
| **Triple Whale** | Dashboard analytics unifié | ~130 € |
| **Metricool** | Scheduling réseaux sociaux | ~30 € |
| **Rewind** | Backup Shopify quotidien | ~9 € |
| **Intelligems** | A/B testing prix et contenu | ~99 € |
| **Rebuy** | Recommandations IA cross-sell | ~99 € |
| **Langify** | Traduction FR/HE/EN | ~20 € |

---

# PARTIE 6 — AUTOMATIONS COMPLÈTES

## KLAVIYO — 18 FLOWS

| # | Flow | Déclencheur | Étapes | Objectif |
|---|---|---|---|---|
| 1 | **Welcome Series** | Subscribe form | E1 immédiat (BIENVENUE10) → J+1 storytelling → J+3 le Signature → J+5 avis → J+8 urgence | Convertir subs |
| 2 | **Browse Abandonment** | Viewed Product 3× | E1 +4h → E2 +24h garantie | Récup intent |
| 3 | **Cart Abandonment** | Checkout started | E1 +1h → E2 +24h social proof → SMS +48h → E3 +72h -10% | Récup panier |
| 4 | **Checkout Abandonné** | Checkout démarré | E1 +30min → E2 +20h → E3 +44h | Hot leads |
| 5 | **Post-Purchase** | Order placed | E1 immédiat → E2 +2j guide entretien → E3 +5j suivi | NPS + upsell |
| 6 | **Order Shipped** | Fulfillment created | SMS + email tracking | Service |
| 7 | **Delivery** | Order delivered | E1 +1j (comment porter) → E2 +7j (avis Loox) → E3 +14j (cross-sell) | Reviews + LTV |
| 8 | **Win-Back 60j** | 60j sans achat | E1 nouveautés → E2 +5j -15% → E3 +10j last chance | Réactivation |
| 9 | **Win-Back 180j** | 180j sans achat | E1 mood → E2 +7j -20% + free ship | Churn |
| 10 | **Anniversaire achat** | 1 an après 1er achat | "Membre depuis 1 an" + exclusivité | Loyalty |
| 11 | **Birthday** | Date anniversaire | -15% le jour J | Émotionnel |
| 12 | **VIP Upgrade** | LTV > 1000 € | "Bienvenue au Cercle Diamant" + perks | Premium |
| 13 | **Back in Stock** | Réassort produit | Email + SMS immédiat | Récup demande |
| 14 | **Price Drop** | Produit wishliste baisse | Email | Récup wishlist |
| 15 | **Cross-sell** | J+30/J+90 post-achat | Pièces complémentaires | Repeat rate |
| 16 | **List Hygiene** | 120j sans engagement | E1 "On vous manque" → si no open : suppression | Délivrabilité |
| 17 | **Review Request** | Livraison +10j | Loox + incentive 5€ | UGC |
| 18 | **Configurateur Abandonné** | Étape 3+ sans finaliser | E1 "Votre bague vous attend" + lien reprise → E2 +48h expert | Récup configurateur |

---

## SHOPIFY FLOW (Natif — Gratuit sur Advanced)

- Tag "VIP" quand customer LTV > 1 000 €
- Tag "needs-ai-shot" → déclenche pipeline Firefly
- Tag "needs-3d" → déclenche pipeline Meshy AI
- Notification Slack sur order > 500 €
- Auto-hide product quand inventory = 0
- Fraud risk > medium → hold fulfillment
- Auto-cancel commande non payée > 24h
- Tag "repeat" sur 2e achat
- Auto gift-wrap si SKU `GIFT-BOX`

---

## MANYCHAT — FLOWS INSTAGRAM & TIKTOK

- **Keyword "PRIX"** → DM auto avec lien produit + code -10%
- **Commentaire "info"** sous post → DM auto fiche produit
- **DM welcome** pour nouveau follower → carrousel collection
- **Lead magnet** : "Envoie GUIDE → reçois le guide bracelet tennis" → capture email → push Klaviyo
- **Retargeting DM** : sync Klaviyo pour relancer en DM Insta les abandons panier
- **TikTok flow** : équivalent via ManyChat TikTok (bêta)

---

## N8N — AUTOMATIONS TECHNIQUES

| Automation | Stack | Fréquence |
|---|---|---|
| Nouveau produit → 4 photos IA | webhook → n8n → Firefly → Slack → Shopify | event |
| Nouveau produit → modèle 3D | webhook → n8n → Meshy → Shopify media | event |
| Articles blog auto (Claude API) | Cron lun/jeu 9h → Claude → validation → Shopify Blog API | 2×/semaine |
| Reporting CA quotidien | Triple Whale API → n8n → Slack → Notion | daily 8h |
| Audit fiches produit faibles | GA4 + Shopify → Claude analyse → Slack reco | daily 7h |
| Social media publish | Airtable → Metricool API | selon calendrier |
| Stock < seuil → alerte | Stocky → Slack | hourly |
| Backup Shopify | Rewind | daily |

---

# PARTIE 7 — BLOG AEO / LE JOURNAL

## ARCHITECTURE DU JOURNAL

**URL :** `bijou-r.com/journal` (pas "blog" — "Journal" est plus premium)

```
/journal/
├── /guides-achat/        → BOFU — intention d'achat forte
├── /art-de-porter/       → MOFU — style et inspiration
├── /comprendre/          → TOFU — éducation diamant, métaux
├── /atelier/             → Brand — coulisses, artisans
├── /histoires/           → Émotionnel — vraies histoires clientes
└── /entretien/           → Post-achat — SEO long terme
```

---

## CALENDRIER ÉDITORIAL 12 MOIS

| Mois | Thématique | Articles phares |
|---|---|---|
| Janvier | Self-love, résolutions | "Le bijou qui marque vos victoires" / "Pierre de naissance : grenat" |
| Février | Saint-Valentin, fiançailles | "Cadeau Saint-Valentin 200-2000€" / "Demander en mariage en 2026" |
| Mars | Printemps, grand-mères | "Le bijou transmis : pourquoi ça change tout" |
| Avril | Mariages, communions | "Bijoux de mariée : alliance, parure, traditions" |
| Mai | Fête des Mères | "Top cadeaux Fête des Mères selon le budget" |
| Juin | Fiançailles été | "Bague de fiançailles : guide complet 2026" |
| Juillet | Vacances, bijoux d'été | "Bijoux résistants à l'eau de mer" |
| Août | Rentrée, bracelet tennis | "Le bracelet tennis : pourquoi tout le monde en veut" |
| Septembre | Roch Hachana, Yom Kippour | "Bijoux pour les fêtes juives : la tradition" ← marché IL |
| Octobre | TOFU éducation | Articles 4C diamant, guide couleur, guide pureté |
| Novembre | Anti-Black Friday | "Pourquoi nous ne ferons jamais de Black Friday" |
| Décembre | Noël, Hanoukka | "Cadeaux Hanoukka 2026" / "Bijoux de Noël" |

**Rythme :** 2 articles/semaine = 104 articles/an.

---

## STRUCTURE D'UN ARTICLE OPTIMISÉ AEO

```markdown
# [H1 = exactement la query cible]
Ex: "Diamant naturel ou de laboratoire : que choisir en 2026 ?"

---
## Réponse rapide (TL;DR — 4 lignes max)
[Bloc encadré]
"Le diamant de laboratoire est 40-60% moins cher que le naturel,
chimiquement identique, et plus responsable. Le diamant naturel
garde une valeur de revente supérieure et une rareté incomparable.
Pour un bijou de tous les jours : lab. Pour une transmission : naturel."

---
## Sommaire (cliquable)
1. Les différences fondamentales
2. Tableau comparatif
3. Lequel choisir selon votre situation
4. FAQ

## [H2 — sous-question 1]
Réponse complète en 3-5 lignes.

## Tableau comparatif (essentiel pour AEO)
| Critère | Diamant naturel | Diamant lab |
|---|---|---|
| Prix | ... | ... |

## FAQ (avec schema JSON-LD FAQPage)
Q1 : "Quel est le budget moyen pour une bague de fiançailles en 2026 ?"
R1 : ...

## Conclusion + CTA produit
[Lien interne vers produit + configurateur]
```

**Éléments AEO obligatoires sur chaque article :**
- ✅ Schema FAQPage (JSON-LD)
- ✅ Schema Article + Author + Organization
- ✅ TL;DR en haut (4 lignes max — cité directement par les IA)
- ✅ Au moins 1 tableau comparatif
- ✅ Données chiffrées sourcées (GIA, IGI, De Beers)
- ✅ 3-5 liens internes par article
- ✅ 1500-2500 mots
- ✅ Mis à jour (date visible)

---

## AUTOMATISATION PUBLICATION ARTICLES (Claude API + n8n)

```
[Cron : lundi 9h + jeudi 9h]
        ↓
[Airtable] Lire la prochaine ligne "Status: À produire"
        ↓
[Claude API - claude-opus-4]
Prompt: "Tu es rédacteur SEO/AEO pour Bijou-R.
Rédige un article de 1800-2200 mots sur [SUJET].
TL;DR 4 lignes. 3 H2 min. 1 tableau comparatif.
FAQ 5 questions (JSON-LD). 3 liens internes vers [PRODUITS].
Livrable : JSON avec title, meta_description, tldr, body_html,
faq_schema, tags."
        ↓
[Firefly API] Générer image cover (style macro luxe)
        ↓
[Quality check n8n] : longueur OK ? mots-clés présents ?
        ↓
[Slack] "Article prêt à valider" + [Bouton VALIDER] [MODIFIER]
        ↓
[Si VALIDER] Shopify Blog API → POST article
        ↓
[Klaviyo] Notifier segment "Abonnés Journal"
        ↓
[Airtable] Update status "Publié" + URL
```

---

## INTERLINKING STRATÉGIQUE

**Règles :**
1. Chaque article → 3 fiches produits minimum
2. Chaque fiche produit → 1-2 articles dans "À lire aussi"
3. Pages pillar : `bijou-r.com/journal/guides-achat/bague-fiancailles-guide-complet` linke 15 articles satellites

**Exemple cluster "Bague de fiançailles" :**
```
PILLAR : /journal/guides-achat/bague-fiancailles-guide-complet
    ↓
    - /journal/comprendre/4c-diamant
    - /journal/comprendre/diamant-naturel-vs-lab
    - /journal/guides-achat/budget-bague-3000-5000
    - /journal/atelier/sertissage-bague
    - /products/bague-solitaire-...
    - /pages/creer-ma-bague
```

---

# PARTIE 8 — SEO GOOGLE

## STRUCTURE URL ET META

- URLs : `bijou-r.com/bracelets/tennis-signature-or-blanc` (FR), `/he/...` (IL)
- Titles : `{Nom} — {Métal} {Carats} | Bijou-R` (60 chars max)
- Metas : `{Nom} en {métal}. Fabriqué en France, garantie à vie. Livraison offerte dès 150€.` (155 chars)

## SCHEMA MARKUP PRODUIT

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Bracelet Tennis Signature Or Blanc 18 Carats",
  "image": ["url1.jpg", "url2.jpg"],
  "description": "...",
  "sku": "BR-TENNIS-OB-18",
  "brand": {"@type": "Brand", "name": "Bijou-R"},
  "material": "Or blanc 18 carats",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "24990.00",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "127"
  }
}
```

## GOOGLE MERCHANT CENTER

- Feed via app "Google & YouTube" Shopify (gratuit)
- Custom labels : bestseller, haute marge, saison
- Activer listings gratuits + Shopping ads

---

# PARTIE 9 — GOOGLE ADS

## STRUCTURE CAMPAGNES

```
Compte Google Ads Bijou-R
│
├── Brand Search "Bijou-R"              5€/j — défense marque
├── Performance Max — Catalogue         50-150€/j — principal
│   ├── Asset Group "Bracelets Tennis"
│   ├── Asset Group "Colliers"
│   ├── Asset Group "Bagues"
│   └── Asset Group "Le Signature"
├── Standard Shopping — Bestsellers     15-30€/j — contrôle CPC
├── Search — Generic high-intent        20-40€/j
│   ├── "bracelet tennis"
│   ├── "collier diamant femme"
│   └── "bague solitaire"
├── Remarketing Display                 15€/j
└── YouTube Awareness (mois 3+)
```

## BUDGETS

| Mois | Budget total | ROAS objectif |
|---|---|---|
| M1 | 2 500 € | 2.5+ |
| M2 | 4 000 € | 3.5+ |
| M3 | 6 000-8 000 € | 4+ |
| M6 | 12 000-20 000 € | 5+ |

**Règle scaling :** ROAS > 3 sur 7j → +20% budget tous les 3 jours.

---

# PARTIE 10 — META ADS

## STRUCTURE CAMPAGNES

```
TOFU — Awareness (vidéo engagement)
    Intérêts : Cartier, Messika, Tiffany, Van Cleef, Vogue Paris

MOFU — Considération (View Content / ATC)
    LAL 1% buyers + retargeting vidéo viewers 75%

BOFU — Conversion (Advantage+ Shopping = cheval de bataille)
    ASC main + retargeting ATC 30j + email list Klaviyo sync

DPA — Catalogue dynamique (retargeting + cross-sell)
```

## CRÉATIFS QUI CONVERTISSENT

Formats priorité :
1. **Reels UGC** 9:16 — 15-30s — hook 2 premières secondes
2. **Carousel** — "5 raisons" / "Avant-Après"
3. **Photo statique** — fond noir épuré avec prix visible
4. **Vidéo unboxing** premium
5. **Vidéo atelier** behind-the-scenes

Angles gagnants :
- "Pourquoi ce bracelet coûte 2490€ (et pourquoi ça vaut le coup)"
- "Garantie à vie : ce qu'aucune autre marque ne fait"
- "Diamants certifiés GIA — voici notre certificat"
- "Made in France — visite de notre atelier"
- **L'Ancre à 24 990€** — crée le buzz, nourrit l'algo, pas pour convertir directement

## BUDGETS META

| Phase | FR/jour | IL/jour | Total/mois |
|---|---|---|---|
| M1 Test | 100 € | 50 € | ~4 500 € |
| M2 Optim | 200 € | 100 € | ~9 000 € |
| M3 Scale | 400 € | 150 € | ~16 500 € |
| M6 | 1 000 € | 300 € | ~39 000 € |

---

# PARTIE 11 — RÉSEAUX SOCIAUX

## INSTAGRAM

**Handle :** `@bijou.r` ou `@bijour_officiel`

**Bio :**
```
✦ Bijoux qui durent
💎 Or 18k & Diamants certifiés GIA
🏛 Fabriqués en France · Garantie à vie
📦 Livraison express 🔗 [lien boutique]
```

**Contenu :**
| Format | Fréquence | Contenu |
|---|---|---|
| Reels | 4-5/semaine | Produit en mouvement, ASMR, unboxing, **démo viewer 3D** |
| Carrousel | 2-3/semaine | "Comment porter X", "Guide tailles", "Avant/Après" |
| Stories | Quotidien | Coulisses, sondages, nouveautés, urgence stock |
| Live | 1/mois | Présentation collection, Q&A |

---

## TIKTOK

**Handle :** `@bijour_` ou `@bijourofficial`
Activer **TikTok Shop** si disponible.

**Formats gagnants :**
| Type | Hook | Durée |
|---|---|---|
| Prix choc | "Ce bracelet coûte 24 990€..." | 15-30s |
| ASMR bijoux | Son du bijou, brillance | 15s |
| **Démo 3D viewer** | "Vous pouvez tourner le bijou avec votre doigt" | 20s |
| Unboxing | Ouvrir le colis Bijou-R | 30-45s |

---

## FACEBOOK

**Statut : Secondaire.** Créer mais ne pas poster activement.
Utilité unique : **Meta Ads** + catalogue produits synchronisé.

---

# PARTIE 12 — L'AGILEUR

**Ce qu'il faut avoir prêt avant son retour :**

- [ ] 5-10 pièces sélectionnées pour tournage
- [ ] Brief créatif écrit (ci-dessous)
- [ ] Props : marbre blanc, velours noir, lumière dorée, boîtes kraft premium
- [ ] Accès éditeur Instagram + TikTok
- [ ] Liste de 20 hooks vidéo testés
- [ ] Story de démo du viewer 3D à filmer

**Brief créatif :**
```
MARQUE : Bijou-R
TON : Confident, désirable, accessible mais premium
NE PAS DIRE : "pas cher" / "discount" / "promo"
DIRE : "prix direct" / "sans intermédiaire" / "qualité joaillier"
ANGLES : Prix ancre / Choc visuel / Émotionnel / Démo 3D viewer wow
CTA : "Lien en bio" / "Code [NOM] -10%"
```

---

# PARTIE 13 — AEO (RÉFÉRENCEMENT IA)

## POURQUOI C'EST CRITIQUE EN 2026

40% des recherches passent par des moteurs IA (ChatGPT Search, Perplexity, Google AI Overviews, Claude, Gemini). Une recherche "où acheter un bracelet tennis en France" donne 3-5 marques citées. **Être cité = exister. Hors citation = invisible.**

## FICHIER llms.txt (à créer à la racine)

```
# Bijou-R
> Maison de joaillerie française, bijoux en or 18 carats,
  garantie à vie, fabrication France. Livraison FR/IL.

## Collections
- /bracelets/tennis : bracelets tennis or et diamants certifiés GIA
- /colliers : colliers diamants et pierres précieuses
- /bagues/solitaires : solitaires et alliances
- /pages/creer-ma-bague : configurateur bague personnalisée

## Pages clés
- /la-maison : histoire de la marque
- /atelier : certifications RJC et process
- /journal/faq : questions fréquentes complètes
```

## TACTIQUES

1. Présence sur **Reddit** (r/jewelry, r/femalefashionadvice) — crawlé massivement par les LLMs
2. **Trustpilot** note >4.5 (très cité par Perplexity)
3. **Listicles** "Top bijouteries françaises" — travailler les éditeurs
4. Profils complets : Google Business, LinkedIn Company, Crunchbase
5. **Wikipedia** dès notoriété suffisante
6. Cohérence NAP sur 50+ annuaires
7. Monitoring citations LLM via **Profound.so** ou **Peec.ai**

**Plan 6 mois :**
- M1 : llms.txt + schemas complets + 20 FAQs
- M2 : 10 articles "réponses" + Trustpilot
- M3 : Google Business + Wikipedia draft + 5 RP presse
- M4-6 : 30 articles + 20 backlinks tier 1 + Reddit organic

---

# PARTIE 14 — GUIDA (ASSISTANT IA INTERNE)

## VISION

Guida est l'associée numérique de Bijou-R. Elle analyse les données Shopify en continu, détecte les problèmes et opportunités, suggère des actions, et exécute certaines tâches automatiquement.

**Ce que Guida surveille :**

| KPI | Seuil alerte | Action |
|---|---|---|
| Conversion global | <2% sur 7j | Audit funnel + recommandations Claude |
| AOV | -10% vs mois précédent | Check upsells |
| Bounce rate homepage | >65% | Audit héro + copy |
| ROAS pubs | <2 | Alerte + nouveaux créatifs Firefly |
| Articles publiés | <2/semaine | Trigger rédaction Claude auto |
| Stock diamants | <3 unités | Réappro alert |
| Taux retour | >5% | Audit produits |

## CHATBOT GUIDA CÔTÉ CLIENT

**Personnalité (system prompt) :**
```
Tu es Guida, conseillère en joaillerie chez Bijou-R.
Tu es chaleureuse, élégante, jamais commerciale.
Tu connais la joaillerie comme une amie d'enfance qui a grandi
dans un atelier parisien.
Tu tutoies si le client tutoie. Tu poses 1 question à la fois.
Tu n'inventes JAMAIS un produit inexistant.
Tu rediriges vers un humain si la commande dépasse 5 000€.
```

**Stack :** ManyChat (front) + Claude API (intelligence) + Shopify API (catalogue)

---

# PARTIE 15 — LANCEMENT PRODUIT

## PRÉ-LANCEMENT (T-60 à T-1 jour)

| Jour | Action |
|---|---|
| T-60 | Landing "coming soon" + email capture + countdown |
| T-60 → T-30 | Meta Ads landing (CPL 1-3€) — objectif 5 000 leads |
| T-45 | Teasers IG (zoom macro extrême sans révéler le produit) |
| T-30 | Annonce nom + date |
| T-21 | Brief presse + samples à 20 journalistes/influenceurs |
| T-14 | 20 vidéos micro-influenceurs prêtes à publier |
| T-7 | 3 emails warmup Klaviyo |
| T-3 | Story "ouverture dans 3j" + démo 3D viewer |
| T-1 | Email "demain 10h" + SMS VIP |

## JOUR J — CHECKLIST COMPLÈTE

**Tech (la veille soir) :**
- [ ] Backup Shopify (Rewind)
- [ ] Test checkout FR (EUR) + IL (ILS) — vrai paiement remboursé
- [ ] Test viewer 3D sur iPhone + Android
- [ ] Test Apple Pay, Alma, Klarna
- [ ] Webhooks n8n actifs et testés
- [ ] Meta Pixel + GA4 + TikTok Pixel validés (Tag Assistant)
- [ ] Pages légales validées (avocat FR + IL)
- [ ] Gorgias prêt + macros pré-écrites

**Marketing (Jour J) :**
- [ ] 10h00 — Email blast toute la base
- [ ] 10h00 — Story + Reel + Post Instagram
- [ ] 10h05 — Activation Meta Ads
- [ ] 10h05 — Activation Google Ads
- [ ] 10h30 — SMS VIP
- [ ] 11h00 — Push 20 influenceurs coordonnés
- [ ] 12h00 — LinkedIn post fondateur
- [ ] 14h00 — Instagram Live behind-the-scenes
- [ ] 20h00 — Story récap day 1

---

# BUDGET MENSUEL (Phase de lancement)

| Poste | €/mois |
|---|---|
| Shopify Advanced | 240 |
| Apps (Klaviyo, Loox, Gorgias, Vitals, etc.) | 500 |
| Adobe Firefly Services | 250 |
| Meshy AI Pro (3D) | 25 |
| n8n VPS Hetzner | 10 |
| Claude API (articles auto) | Variable (~50-150) |
| Airtable Team | 25 |
| Cloudinary | 50 |
| Triple Whale | 130 |
| Metricool | 30 |
| Stocky | 79 |
| Retouche photo manuelle (complément) | 800 |
| Meta Ads | 9 000 |
| Google Ads | 4 000 |
| TikTok Ads | 1 500 |
| Influenceurs / UGC | 3 000 |
| RP presse | 1 500 |
| **TOTAL** | **~21 000-22 000 €/mois** |

---

# SITES DE RÉFÉRENCE

| Site | Ce qu'on reprend |
|---|---|
| **Messika.com** | Élégance visuelle, typographie, storytelling designer, vidéo parallaxe |
| **Mejuri.com** | Chaleur émotionnelle, copy self-love, UGC massif, quiz d'entrée, mobile-first |
| **James Allen** | Configurateur diamants, vidéo 360° du diamant réel, filtres 4C, PDF certificat |
| **Brilliant Earth** | Traçabilité, histoires clients, étapes configurateur claires |
| **Vrai.com** | Transparence prix, DTC assumé, esthétique épurée |
| **Bijou-R unique** | **AR sur main réelle + marché IL natif + service vidéaste demande en mariage + automation IA totale** |

---

# ROADMAP 90 JOURS

| Semaine | Focus |
|---|---|
| S1-2 | Domaine + mails + Shopify setup + thème + pages + Pixel |
| S2-3 | Produits + metafields + fiches émotionnelles + pipeline Firefly + Meshy |
| S3-4 | Klaviyo 18 flows + schemas JSON-LD + sitemap GSC |
| S5 | Landing pré-lancement + Meta Ads warmup |
| S6 | Influenceurs + presse + UGC tournés avec l'agileur |
| S7 | ManyChat + Gorgias + n8n blog auto |
| S8 | Prototype configurateur étapes 1-4 + Three.js viewer |
| S9 | Pré-lancement actif (email capture objectif 5k leads) |
| S10 | Soft launch VIP 48h |
| **S11** | **LAUNCH DAY** |
| S12 | Optim, scaling, premiers reviews |
| M4+ | Configurateur full + blog AEO + Google Ads scale |

---

*Bijou-R — Plan Stratégique Complet v3 — 20/05/2026*
*Réflexion Opus — Ne rien mettre en oeuvre sans avoir lu en entier.*
