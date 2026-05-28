# BIJOU-R — PLAN D'ACTION COMPLET v2
> Réflexion Opus · Mis à jour le 20/05/2026
> Objectif : boutique Shopify bijouterie qui choque, convertit, scale et s'automatise à fond.

---

## ARCHITECTURE GLOBALE

```
                    ┌──────────────────────┐
                    │   SHOPIFY (core)     │
                    │  Bijou-R store + API │
                    └──────────┬───────────┘
                               │ webhooks
                ┌──────────────┴──────────────┐
                ▼                             ▼
        ┌───────────────┐             ┌──────────────────┐
        │  n8n / Make   │             │     Klaviyo      │
        │ (orchestrateur)─────────────►  (email + SMS)   │
        └───┬────┬────┬─┘             └──────────────────┘
            │    │    │
            ▼    ▼    ▼
    ┌───────┐ ┌──────┐ ┌──────────────────┐
    │Firefly│ │Meshy │ │ManyChat / Meta   │
    │  API  │ │  AI  │ │TikTok / Pinterest│
    │(photos│ │(3D)  │ │                  │
    └───────┘ └──────┘ └──────────────────┘
            ▲
            │
    ┌───────┴────────┐
    │ Google Ads /   │
    │ Merchant /     │
    │ Search Console │
    └────────────────┘
```

**Pile technique :**
- **Shopify Advanced** (240 €/mois) — checkout extensions + multi-marché FR/IL
- **n8n** self-hosted (5 €/mois VPS Hetzner) — orchestrateur principal
- **Klaviyo** — email + SMS automation
- **Adobe Firefly Services** — génération photos IA
- **Meshy AI** — génération modèles 3D depuis photos
- **Airtable** — PIM produits (source de vérité)
- **Cloudinary** — pipeline images CDN

---

## PHASE 0 — FONDATIONS (Jour 1-2)

### 1. CRÉATION DES MAILS

| Adresse | Usage |
|---|---|
| `hello@bijou-r.com` | Contact client principal |
| `commandes@bijou-r.com` | Confirmation commandes (Shopify SMTP) |
| `support@bijou-r.com` | SAV / litiges |
| `pro@bijou-r.com` | Collabs influenceurs / B2B |

**Outil :** Google Workspace (~6 $/mois) — domaine custom, crédible.
> Créer les mails APRÈS l'achat du domaine.

---

### 2. ACHAT DU DOMAINE

**Priorité :** `bijou-r.com`
**Vérifier aussi :** `bijour.com` / `bijou-r.fr` / `bijou-r.co`

**Plateformes :**
1. **Namecheap** — ~10 $/an
2. **Shopify Domains** — intégration native, zéro config DNS
3. **OVH** — marché FR/IL

Acheter `.com` (obligatoire) + `.fr` ou `.co.il` (optionnel mais recommandé).

---

## PHASE 1 — SHOPIFY CONFIGURATION (Jour 2-4)

### 3. CONFIGURATION SHOPIFY

**Plan :** Advanced (240 €/mois) — nécessaire pour Shopify Flow + multi-marché.

#### Thème recommandé
**Impulse** (Archetype Themes, 380 $) ou **Prestige** (Maestrooo, 320 $).

Pourquoi pas Dawn gratuit : besoin de :
- Sections lookbook éditorial
- Quick-view + sticky add-to-cart
- Drawer cart avec upsell natif
- Mega-menu visuel
- Image zoom 4K + **lecteur 3D natif** (crucial — cf section 3D)

**Identité visuelle :**
- Palette : noir profond `#0A0A0A`, blanc cassé `#FAF7F2`, or champagne `#C9A961`
- Polices : Cormorant Garamond (titres) + Inter (UI)
- Animation hover : zoom 1.05 sur vignettes produit

#### Structure de navigation

```
Header
├── Bracelets → Tennis (signature) / Chaînes / Joncs / Voir tout
├── Colliers → Pendentifs / Chokers / Sautoirs / Voir tout
├── Bagues → Solitaires / Alliances / Cocktail / Voir tout
├── Boucles d'oreilles
├── Nouveautés
├── Édition limitée  ← bracelet tennis ancre ici
└── Le Journal (blog SEO)

Top-bar : "Livraison offerte dès 150 € — Garantie à vie sur tous nos bijoux"
```

#### Pages à créer

| Page | Contenu clé |
|---|---|
| Home | Hero vidéo bracelet tennis, 3 piliers USP, "Le Signature", témoignages, feed Instagram |
| À propos | Storytelling fondateur, atelier, philosophie |
| Notre atelier | Process fabrication, certifications RJC / Kimberley Process |
| Guide des tailles | Tableau FR/IL/US, méthode mesure poignet |
| Garantie à vie | Couverture détaillée + formulaire activation |
| Livraison & Retours | FR 48h gratuite > 150 €, IL DHL 3-5j, retours 30j |
| FAQ | 20-30 questions (or, entretien, allergies, gravure) — crucial pour AEO |
| Le Journal | Blog SEO (2 articles/semaine) |
| Programme fidélité | Cercle Bijou-R — paliers Or/Platine/Diamant |
| Carte cadeau | 50/100/250/500/1000 € |
| Contact | Formulaire + WhatsApp + horaires |
| Pages légales | CGV, CGU, Mentions, Confidentialité, Cookies, Retours |

#### Paiements

1. **Shopify Payments** (FR EUR) — Visa/Mastercard/CB
2. **Stripe** (IL ILS) — Shopify Payments non dispo en Israël
3. **PayPal Express** (FR + IL)
4. **Apple Pay + Google Pay** (auto avec Shopify Payments/Stripe)
5. **Alma / Klarna** — paiement 3x/4x (Alma plus français) — crucial > 300 €
6. **Bit / Tranzila** — paiement local israélien très utilisé
7. **Cryptos** via Coinbase Commerce (optionnel)

Configuration **multi-devise** via Shopify Markets : FR (EUR), IL (ILS), EU (EUR).

#### Trust signals

- Bandeau certifications : RJC, Kimberley Process, Made in France
- Badge "Garantie à vie" sur toutes les fiches produit
- Badge "Paiement 100 % sécurisé — 3D Secure"
- Bloc "Vu dans" (logos presse)
- Avis Loox/Judge.me avec photos clients
- Numéro téléphone + WhatsApp visible
- SIRET + adresse atelier en footer

---

## PHASE 2 — VIEWER 3D & 360° (LE DIFFÉRENCIATEUR MAJEUR)

### 4. VISIONNEUSE 3D INTERACTIVE SUR SHOPIFY

> Objectif : le client touche son téléphone et tourne le bijou dans tous les sens comme un objet 3D réel. Sur mobile, il peut même pointer vers sa main et voir la bague en AR.

#### Comment ça marche nativement sur Shopify

**Shopify supporte les modèles 3D nativement** via le composant `model-viewer` (Google). Il suffit d'uploader un fichier `.glb` ou `.gltf` dans les médias produit — Shopify affiche automatiquement :
- Rotation 360° libre (doigt sur mobile, souris sur desktop)
- Zoom pinch
- Éclairage HDR automatique
- **Mode AR sur iPhone (iOS AR Quick Look)** — le client pointe sa caméra et voit la bague sur sa main
- **Mode AR sur Android (Scene Viewer)** — idem
- Aucune app Shopify nécessaire pour le rendu de base

#### Générer les modèles 3D avec Meshy AI

**Meshy.ai** est l'outil qu'il te faut. Il génère des modèles 3D `.glb` depuis des photos produits avec une qualité excellente sur les bijoux (métal, pierres).

**Deux modes :**
1. **Image to 3D** — tu envoies une photo du bijou → Meshy génère le modèle 3D (idéal pour tes photos existantes)
2. **Text to 3D** — tu décris le bijou → Meshy génère (pour les produits sans photo encore)

**Qualité de sortie :** PBR (Physically Based Rendering) — les reflets or et l'éclat des pierres sont bien rendus.

**Prix Meshy AI :** ~20 $/mois plan Pro (150 crédits/mois, ~1 crédit par modèle).

**Meshy AI a une API.** Endpoints principaux :

```
POST https://api.meshy.ai/v2/image-to-3d
Headers: Authorization: Bearer {MESHY_API_KEY}
Body: {
  "image_url": "https://...(photo produit)",
  "enable_pbr": true,
  "surface_mode": "hard",   // bijoux = surface dure
  "topology": "quad",
  "target_polycount": 30000
}
→ Retourne un task_id

GET https://api.meshy.ai/v2/image-to-3d/{task_id}
→ Poll jusqu'à "succeeded", récupère model_urls.glb
```

#### Pipeline automation complet : Photo produit → 3D → Shopify

```
Shopify webhook (products/create)
        │
        ▼
n8n : produit a un tag "needs-3d" ?
        │
        ▼
HTTP : GET image principale du produit
        │
        ▼
HTTP POST → Meshy API /v2/image-to-3d
  { image_url, enable_pbr: true, surface_mode: "hard" }
        │
        ▼
Wait + Poll toutes les 10s → GET /v2/image-to-3d/{task_id}
  jusqu'à status = "succeeded"
        │
        ▼
Download .glb depuis model_urls.glb
        │
        ▼
Shopify Admin API : POST /products/{id}/media.json
  { "media": { "original_source": "<glb_url>",
               "media_type": "MODEL_3D",
               "alt": "Vue 3D - {product_title}" } }
        │
        ▼
Retirer le tag "needs-3d", ajouter "3d-done"
        │
        ▼
Slack : "Modèle 3D généré pour {product_title} — approuver ?"
```

Durée totale : 5-15 minutes par produit, 100 % automatique.

#### Apps Shopify pour enrichir l'expérience 3D (optionnel)

| App | Usage | Prix |
|---|---|---|
| **Zakeke 3D Viewer** | Viewer 3D + personnalisation gravure live + AR | ~50 $/mois |
| **CGTrader AR** | Viewer AR plus avancé | ~30 $/mois |
| **Magic 360** | 360° spin (photos, pas vrai 3D) | ~20 $/mois |

> Recommandation : commencer avec le viewer natif Shopify (gratuit), passer à Zakeke si tu veux ajouter la **gravure personnalisée en live** (le client voit son prénom gravé en temps réel en 3D).

#### Résultat final sur le site

Sur la fiche produit de la bague :
- Photo 1 : packshot fond blanc
- Photo 2 : portée lifestyle
- Photo 3 : détail macro
- **Photo 4 : icône 3D → viewer interactif** (tourne avec le doigt)
- **Bouton "Voir en AR"** sur iOS/Android → réalité augmentée

C'est un différenciateur énorme dans la bijouterie en ligne. Quasiment aucune marque accessible le fait aussi bien.

---

## PHASE 3 — PRODUITS (Jour 3-7)

### 5. CATALOGUE PRODUITS

#### Stratégie 3 niveaux — psychologie du prix ancre

| Niveau | Produit | Prix (€) | Rôle |
|---|---|---|---|
| **ANCRE HAUTE** | Bracelet Tennis Signature Or Blanc 18k 2ct | **24 990 €** | Choque, légitime tout |
| **PREMIUM** | Tennis Or Blanc 18k 1ct | 6 990 € | Aspiration |
| **BESTSELLER** | Tennis Or Jaune 14k | 2 490 € | Sweet spot marge |
| **ENTRÉE** | Tennis Vermeil 0.5ct | 890 € | 1er achat |
| **TRAFIC** | Tennis Argent | 290 € | Volume |

L'ancre à 24 990 € ne vend pas beaucoup — mais elle fait paraître le 2 490 € comme une **affaire**. C'est la mécanique du banger.

Autres techniques de pricing :
- Prix finissant en 0 pour le luxe (2490 pas 2489) — psychologie inverse du discount
- Jamais de soldes sur la collection signature (préserve l'aura)
- Paiement 4× Alma affiché en gros : "4 × 622 €" rend 2490 € digérable
- Carte cadeau 500 € offerte dès 5000 € (incite à monter en gamme)

#### 10 produits de lancement minimum

1. Bracelet Tennis Signature (ANCRE — 24 990 €)
2. Bracelet Tennis Or Blanc 18k (6 990 €)
3. Bracelet Tennis Or Jaune 14k (2 490 €)
4. Bracelet Chaîne dorée (299 €)
5. Collier Riviera Diamants (1 890 €)
6. Collier Pendentif (299 €)
7. Bague Solitaire (1 490 €)
8. Boucles Créoles Or (449 €)
9. Set Cadeau Collier + Boucles (590 €)
10. Jonc or (390 €)

#### Fiche produit — structure complète

```
[H1] Bracelet Tennis Signature — Or Blanc 18 Carats | Bijou-R

[Bloc résumé AEO]
• Or blanc 18 carats
• 2 carats de diamants VS1 couleur G
• Certificat GIA inclus
• Garantie à vie
• Livraison France 48h offerte

[Description éditoriale 300-500 mots]
[Spécifications techniques en tableau — métafields]
[Sélecteur taille + couleur métal]
[CTA : Ajouter au panier + Paiement 4× Alma affiché]
[Viewer 3D / 360°]
[Bundle : "Complétez le look"]
[FAQ produit spécifique — 5-10 questions — schema FAQPage]
[Avis clients Loox avec photos]
[Garantie + Livraison + Retours en icônes]
```

#### Metafields à créer (namespace `bijour`)

- `bijour.materiau` — Acier 316L / Plaqué or 18k / Or massif 18k
- `bijour.carats_or` — 14/18/24
- `bijour.pierre_principale` — Diamant / Saphir / Rubis
- `bijour.carat_pierre` — ex: 2.0
- `bijour.purete_diamant` — VS1, VVS, SI1
- `bijour.couleur_diamant` — D, E, F, G
- `bijour.certification` — PDF certificat GIA/IGI
- `bijour.poids_grammes` — ex: 8.5
- `bijour.origine` — France / Italie
- `bijour.delai_fabrication` — en jours
- `bijour.video_360` — file vidéo spin
- `bijour.story` — histoire de la pièce
- `bijour.modele_3d` — GLB file URL (auto-rempli par pipeline Meshy)

---

## PHASE 4 — GÉNÉRATION PHOTOS AI (Jour 5-10)

### 6. ADOBE FIREFLY API — Photos automatiques

#### Ce qui existe

Adobe **Firefly Services** (API accessible via Adobe Developer Console).

| Endpoint | Usage Bijou-R |
|---|---|
| `POST /v3/images/generate` | Créer un visuel lifestyle depuis prompt texte |
| `POST /v3/images/generate-async` | Batch catalogue |
| `POST /v3/images/fill` | Mettre un fond luxe sur une photo de bijou |
| `POST /v3/images/expand` | Étendre un packshot en bannière/story |
| `POST /v3/images/generate-object-composite` | **Placer le bijou dans un décor IA** — la killer feature |
| `POST /v2/storage/image` | Upload photo source |

**Auth :** OAuth Server-to-Server (Client Credentials) via Adobe Developer Console.
**Prix :** facturé en generative credits (~0,20 € par image). Plan Firefly Services à partir de ~250 $/mois.

#### Pipeline automation : Nouveau produit → 4 photos + 1 modèle 3D

```
Shopify webhook (products/create)
        │
        ├──────────────────────────────────────────┐
        ▼                                          ▼
[BRANCH A : PHOTOS FIREFLY]              [BRANCH B : MODÈLE 3D MESHY]
        │                                          │
Adobe IMS → get access_token            Meshy API → image-to-3d
        │                                          │
Upload photo brute → /v2/storage/image  Poll jusqu'à "succeeded"
        │                                          │
generate-object-composite ×4 variantes  Download .glb
(fond marbre, fond velours noir,                   │
lumière dorée, fond minimaliste)        Upload Shopify media (MODEL_3D)
        │                                          │
Download images → Cloudinary CDN        Tag "3d-done"
        │
Upload vers Shopify product images
        │
Slack : "Approuver les 4 visuels ?"
        │
[Bouton Approuver] → push Shopify
```

#### Prompts Firefly par catégorie

**Bracelet tennis :**
```
"Sparkling diamond tennis bracelet on polished black marble,
dramatic studio lighting, deep shadows, luxury jewelry editorial,
Vogue style, 8k hyperrealistic, --ar 1:1"
```

**Bague solitaire :**
```
"Elegant diamond solitaire ring on female hand, natural sunlight,
minimalist white background, Hasselblad medium format,
100mm macro, f/2.8 bokeh, premium jewelry photography"
```

**Format par image :**
- Photo 1 : fond blanc pur (catalogue)
- Photo 2 : fond velours noir (luxe)
- Photo 3 : lifestyle portée (ambiance)
- Photo 4 : macro détail (brillance pierre)
- Photo 5 : générée expand → 9:16 story Instagram

---

## PHASE 5 — APPLICATIONS SHOPIFY

### 7. APPS PAR PRIORITÉ

#### Essentielles au lancement

| App | Usage | Prix |
|---|---|---|
| **Klaviyo** | Email + SMS automation | Gratuit < 250 contacts |
| **Loox** | Avis avec photos UGC | ~10 $/mois |
| **Judge.me** | Avis + étoiles schema | Gratuit plan base |
| **Searchanise** | Search avancée + filtres metafields | ~19 $/mois |
| **Tidio** | Chat live + bot SAV | Gratuit plan base |
| **Hextom Shipping Bar** | Barre livraison offerte | Gratuit |
| **Back in Stock** | Alerte réassort | ~20 $/mois |
| **Shopify Flow** | Automations natives | Gratuit (Advanced) |

#### Croissance (mois 2+)

| App | Usage | Prix |
|---|---|---|
| **Gorgias** | SAV centralisé email + IG + TikTok | ~60 $/mois |
| **ReConvert** | Upsell post-achat | ~5 $/mois |
| **Zakeke** | Viewer 3D + gravure live | ~50 $/mois |
| **Appstle Subscriptions** | "Bijou du mois" abonnement | ~10 $/mois |
| **Langify** | Traductions FR/HE/EN | ~20 $/mois |
| **Stocky** | Gestion stock + prévisions | ~79 $/mois |
| **Triple Whale** | Dashboard analytics unifié | ~130 $/mois |
| **Bundler** | Sets + bundles | Gratuit |
| **Vitals** | SEO + popups + social proof | ~30 $/mois |

---

## PHASE 6 — AUTOMATIONS COMPLÈTES

### 8. KLAVIYO — 18 FLOWS DÉTAILLÉS

| # | Flow | Déclencheur | Étapes | Objectif |
|---|---|---|---|---|
| 1 | **Welcome Series** | Subscribe form | E1 immédiat (code BIENVENUE10) → J+1 storytelling → J+3 le Signature → J+5 avis clients → J+8 urgence code expire | Convertir nouveaux subs |
| 2 | **Browse Abandonment** | Viewed Product 3× sans add to cart | E1 +4h → E2 +24h garantie | Récup intent |
| 3 | **Cart Abandonment** | Checkout started | E1 +1h → E2 +24h social proof → SMS +48h → E3 +72h -10 % code unique | Récup panier |
| 4 | **Checkout Abandoned** | Checkout démarré sans achat | E1 +30min → E2 +20h → E3 +44h | Hot leads |
| 5 | **Post-Purchase** | Order placed | E1 +0 (merci + storytelling) → E2 +2j guide entretien → E3 +5j suivi colis | NPS + upsell |
| 6 | **Order Shipped** | Fulfillment created | SMS + email tracking | Service |
| 7 | **Delivery Confirmation** | Order delivered | E1 +1j (comment porter) → E2 +7j (demande avis Loox) → E3 +14j (cross-sell) | Reviews + LTV |
| 8 | **Win-Back 60j** | Pas d'achat 60j | E1 nouveautés → E2 +5j -15 % → E3 +10j last chance | Réactivation |
| 9 | **Win-Back 180j** | Pas d'achat 180j | E1 mood collection → E2 +7j -20 % + free ship | Réveil churn |
| 10 | **Anniversaire achat** | 1 an après 1er achat | Email "membre depuis 1 an" + exclusivité | Loyalty |
| 11 | **Birthday** | Date anniversaire client | -15 % le jour J | Personnalisation |
| 12 | **VIP Tier Upgrade** | LTV > 1000 € | "Bienvenue au Cercle Diamant" + perks | Premium loyalty |
| 13 | **Back in Stock** | Souscription → réassort | Email + SMS immédiat | Récup demande |
| 14 | **Price Drop** | Produit wishliste → baisse prix | Email | Récup wishlist |
| 15 | **Replenishment** | Cross-sell J+30/J+90 | Suggestions pièces complémentaires | Repeat rate |
| 16 | **List Hygiene** | No engagement 120j | E1 "On vous manque" → si no open : suppression | Délivrabilité |
| 17 | **Review Request** | Livraison +10j | Loox intégré + incentive 5 € | UGC |
| 18 | **Wishlist Reminder** | Item wishlist > 7j | "Toujours en stock" | Conversion |

**Segmentation Klaviyo :**
- Engaged (90j open/click)
- VIP (LTV > 1000 €)
- IL audience (location)
- High intent (> 3 sessions, viewed Tennis)
- Loyal (>= 2 orders)

### 9. SHOPIFY FLOW (natif, gratuit)

- Tag "VIP" quand customer total > 1000 €
- Tag "needs-ai-shot" → déclenche pipeline Firefly
- Tag "needs-3d" → déclenche pipeline Meshy AI
- Notification Slack sur order > 500 €
- Auto-hide product quand inventory = 0
- Fraud risk > medium → hold fulfillment + email
- Auto-cancel commande non payée > 24h
- Tag "repeat" sur 2e achat
- Auto gift-wrap si SKU `GIFT-BOX` dans commande

### 10. SOCIAL MEDIA AUTOMATION

- **Metricool** ou **Later** (15-50 $/mois) — scheduling IG/TikTok/Pinterest/Facebook
- n8n : Airtable calendrier éditorial → si statut "à publier" → push API Metricool
- **Pinterest** : auto-pin chaque nouveau produit via flux RSS Shopify → Tailwind
- TikTok : programmation via TikTok Business Suite natif

### 11. MANYCHAT — Flows Instagram & TikTok

- **Story reply keyword** "PRIX" → DM auto avec lien produit + code -10 %
- **Comment to DM** : "info" sous post tennis → DM auto fiche produit
- **DM welcome** : nouveau follower → carrousel collection
- **Lead magnet** : "Envoie GUIDE pour recevoir notre guide bracelet tennis" → capture email → push Klaviyo
- **TikTok flow** : équivalent via ManyChat TikTok (bêta)

### 12. SAV AUTOMATISÉ

- **Gorgias** helpdesk (60 $/mois) — IA répond à 80 % des questions FAQ
- Tags auto : livraison / taille / retour / garantie
- Macros pré-écrites pour les 30 cas les plus fréquents
- Routing : tickets IL → agent hébreu, tickets FR → agent FR
- WhatsApp Business intégré
- SLA : 4h en heures ouvrées

### 13. REPORTING AUTOMATIQUE

- **Triple Whale** ou **Polar Analytics** (130 $/mois) — dashboard unifié
- Rapport quotidien 8h : CA, AOV, ROAS Meta/Google, taux conversion, stock
- Rapport hebdo auto-généré dans Notion (n8n + Notion API)
- Google Looker Studio + BigQuery (export Shopify quotidien) pour dashboards custom

### 14. TABLEAU RÉCAP AUTOMATIONS

| Automation | Stack | Fréquence |
|---|---|---|
| Nouveau produit → 4 photos IA | Shopify webhook → n8n → Firefly → Slack → Shopify | event |
| Nouveau produit → modèle 3D | Shopify webhook → n8n → Meshy API → Shopify media | event |
| Welcome + nurturing | Klaviyo | event |
| Abandon panier | Klaviyo + ManyChat | event |
| Post-purchase | Klaviyo + Gorgias | event |
| Stock < seuil | Stocky + Slack | hourly |
| Social media publish | Metricool + Airtable | daily |
| Reporting CA | Triple Whale + n8n → Notion | daily |
| Bilan hebdo | Looker Studio email | weekly |
| Backup Shopify | Rewind | daily |

---

## PHASE 7 — SEO GOOGLE

### 15. STRUCTURE SEO

**URLs :**
- `bijou-r.com/bracelets/tennis-signature-or-blanc` (FR)
- `bijou-r.com/he/...` (IL)

**Titles produit :** `{Nom} — {Métal} {Carats} | Bijou-R` (60 chars max)
**Meta description :** `{Nom} en {métal} avec {pierre}. Fabriqué en France, garantie à vie. Livraison offerte dès 150 €.` (155 chars max)

### 16. BLOG — 3 PILIERS SEO

**Pilier 1 : Guides d'achat (BOFU)**
- Comment choisir un bracelet tennis
- Or 14 vs 18 carats : lequel choisir
- Diamant naturel vs lab-grown
- Combien coûte un vrai bracelet tennis
- Solitaire : guide complet des 4C

**Pilier 2 : Entretien & lifestyle (MOFU)**
- Nettoyer son or 18 carats à la maison
- Comment éviter les allergies aux bijoux
- Porter son bracelet tennis 24/7 : oui ou non

**Pilier 3 : Inspiration & culture (TOFU)**
- Histoire du bracelet tennis (Chris Evert)
- Tendances bijoux 2026
- Comment empiler ses bracelets
- Bijoux dans la culture juive (pour SEO IL)

Rythme : 2 articles/semaine, 1500-2500 mots, avec FAQ schema.

### 17. GOOGLE MERCHANT CENTER

- Feed produits via app **Google & YouTube** Shopify (natif gratuit)
- Champs requis : GTIN, MPN, brand=Bijou-R, condition=new, image min 1500×1500
- Custom labels : bestseller, marge haute, saison
- Activer listings gratuits + Shopping ads

### 18. SCHEMA MARKUP PRODUIT (JSON-LD)

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Bracelet Tennis Signature Or Blanc 18 Carats",
  "image": ["https://cdn.bijou-r.com/1.jpg", "..."],
  "description": "...",
  "sku": "BR-TENNIS-OB-18",
  "brand": { "@type": "Brand", "name": "Bijou-R" },
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

Ajouter aussi : `BreadcrumbList`, `Organization`, `FAQPage`, `Article`, `WebSite` avec `SearchAction`.

---

## PHASE 8 — GOOGLE ADS

### 19. STRUCTURE CAMPAGNES

```
Compte Google Ads Bijou-R
│
├── Brand Search "Bijou-R"              (5 €/j — défense marque)
├── Performance Max — Catalogue         (50-150 €/j — principal)
│   ├── Asset Group "Bracelets"
│   ├── Asset Group "Colliers"
│   ├── Asset Group "Bagues"
│   └── Asset Group "Le Signature"
├── Standard Shopping — Bestsellers     (15-30 €/j — contrôle CPC)
├── Search — Generic high-intent        (20-40 €/j)
│   ├── "bracelet tennis"
│   ├── "collier diamant"
│   ├── "bague solitaire"
│   └── "bijoux femme luxe"
├── Remarketing Display                 (15 €/j)
└── YouTube Awareness (mois 3+)
```

### 20. BUDGETS & KPIs

| Mois | Budget/mois | Objectif ROAS |
|---|---|---|
| M1 | 2 500 € | 2.5+ |
| M2 | 4 000 € | 3.5+ |
| M3 | 6 000-8 000 € | 4+ |
| M6 | 12 000-20 000 € | 5+ |

**KPIs :**
- ROAS objectif : 3.5 minimum, 5+ Search brand
- CPA cible : < 40 % AOV
- Taux conversion site : 1.8-2.5 %
- Search Impression Share brand : > 90 %

---

## PHASE 9 — META ADS

### 21. STRUCTURE CAMPAGNES

```
Business Manager Bijou-R
│
├── TOFU — Awareness (Engagement vidéo / ThruPlay)
│   ├── Intérêts joaillerie (Cartier, Messika, Van Cleef)
│   └── LAL 1-3 % vidéo viewers
│
├── MOFU — Considération (View Content / Add to Cart)
│   ├── LAL 1 % buyers
│   └── Retargeting vidéo viewers 75 %
│
├── BOFU — Conversion (Advantage+ Shopping = principal)
│   ├── ASC main campaign
│   ├── Retargeting ATC 30j
│   └── Email list Klaviyo sync
│
└── DPA — Catalogue dynamique
    ├── Retargeting full catalog
    └── Cross-sell post-purchase
```

### 22. CRÉATIFS QUI CONVERTISSENT

Formats priorité :
1. **Reels UGC** 9:16, 15-30s, hook 2 premières secondes
2. **Carousel** storytelling "5 raisons" / "4 styles"
3. **Photo statique** épurée fond noir avec prix visible
4. **Vidéo unboxing** premium
5. **Vidéo atelier** behind-the-scenes

Angles gagnants bijouterie :
- "Pourquoi ce bracelet coûte 2490 € (et pourquoi ça vaut le coup)"
- "Garantie à vie : ce qu'aucune autre marque ne fait"
- "Diamants certifiés GIA — voici notre certificat"
- "Made in France — visite de notre atelier"
- L'Ancre à 24 990 € (crée le buzz, nourrit l'algo — pas pour convertir)

### 23. BUDGETS META

| Phase | Budget/jour FR | Budget/jour IL | Total/mois |
|---|---|---|---|
| M1 Test | 100 € | 50 € | ~4 500 € |
| M2 Optim | 200 € | 100 € | ~9 000 € |
| M3 Scale | 400 € | 150 € | ~16 500 € |
| M6 | 1000 € | 300 € | ~39 000 € |

**Règle de scaling :** ROAS > 3 sur 7 jours → +20 % budget tous les 3 jours. ROAS < 1.5 → kill.

---

## PHASE 10 — RÉSEAUX SOCIAUX

### 24. INSTAGRAM

**Handle :** `@bijou.r` ou `@bijour_officiel`
**Type :** Compte Business (pas Créateur)

**Bio :**
```
✦ Bijoux qui durent
💎 Or 18k & Diamants certifiés GIA
🏛 Fabriqués en France · Garantie à vie
📦 Livraison express 🔗 [lien boutique]
```

**Stratégie contenu :**
| Format | Fréquence | Contenu |
|---|---|---|
| Reels | 4-5/semaine | Produit en mouvement, ASMR, unboxing, 3D viewer demo |
| Carrousel | 2-3/semaine | "Comment porter X", "Guide tailles", "Avant/Après" |
| Stories | Quotidien | Coulisses, sondages, nouveautés, urgence stock |
| Live | 1/mois | Présentation collection, Q&A |

### 25. TIKTOK

**Handle :** `@bijour_` ou `@bijourofficial`
**Activer TikTok Shop** si disponible dans ta région.

**Formats gagnants :**
| Type | Hook | Durée |
|---|---|---|
| Prix choc | "Ce bracelet coûte 24 990 €..." | 15-30s |
| ASMR bijoux | Son du bijou, brillance | 15s |
| 3D viewer demo | "Vous pouvez tourner le bijou avec votre doigt" | 20s |
| Unboxing | Ouvrir le colis Bijou-R | 30-45s |
| "POV tu veux te faire un cadeau" | Transition bijou porté | 15s |

**Hashtags :** `#bijouxfemme #bracelet #tennisnecklace #jewelrytiktok #goldjewelry #unboxing`

### 26. FACEBOOK

**Statut : Secondaire — créer mais pas activer.**

Pourquoi le créer quand même :
- Nécessaire pour Meta Ads (pub Facebook + Instagram depuis le même compte)
- Catalogue produit Facebook = base pour Dynamic Ads
- Clients 30+ en Israël achètent encore via Facebook

Setup minimum :
- [ ] Page Facebook reliée au compte Instagram
- [ ] Meta Business Manager configuré
- [ ] Meta Pixel installé sur Shopify
- [ ] Catalogue produit synchronisé (via Shopify Feed)

---

## PHASE 11 — L'AGILEUR (Préparer avant son retour)

### 27. CE QU'IL FAUT AVOIR PRÊT

- [ ] 5-10 pièces sélectionnées pour tournage
- [ ] Brief créatif écrit (ton, hooks, ce qu'il faut dire / ne pas dire)
- [ ] Props : marbre blanc, velours noir, lumière dorée, boîtes kraft premium, fleurs séchées
- [ ] Accès éditeur Instagram + TikTok
- [ ] Liste de 20 hooks vidéo testés
- [ ] Story UGC démo viewer 3D (le client tourne le bijou)

**Brief créatif type :**
```
MARQUE : Bijou-R
TON : Confident, désirable, accessible mais premium
NE PAS DIRE : "pas cher" / "discount" / "promo"
DIRE : "prix direct" / "sans intermédiaire" / "qualité joaillier"
ANGLES : Prix ancre / Choc visuel / Émotionnel (cadeau, amour propre) / 3D viewer wow
CTA : "Lien en bio" / "Voir la collection" / "Code [NOM] -10%"
```

### 28. MICRO-INFLUENCEURS (en parallèle)

- Cible : 5K-50K abonnés niche mode/bijoux/lifestyle
- Offre : gifting (produit gratuit contre post) ou % commission (10-15 %)
- Outils : **Collabstr** ou **Modash** pour trouver les profils FR + IL
- KPIs : EMV (Earned Media Value), reach, saves, trafic UTM

---

## PHASE 12 — AEO (ANSWER ENGINE OPTIMIZATION)

### 29. RÉFÉRENCEMENT IA — Pourquoi c'est critique en 2026

40 % des recherches passent par des moteurs IA (ChatGPT Search, Perplexity, Google AI Overviews, Claude, Gemini). Une recherche "où acheter un bracelet tennis en France" ne donne plus 10 liens bleus : l'IA répond avec 3-5 marques citées. **Être cité = exister. Hors citation = invisible.**

### 30. OPTIMISATION FICHES PRODUIT POUR LES LLMs

Les IA privilégient les contenus :
- Factuels + structurés (listes, tableaux, FAQ)
- Auto-suffisants (chaque page répond à une question complète)
- Sourcés (certificats GIA, normes RJC)
- Datés ("mis à jour mai 2026")
- Riches en entités (or 18 carats, diamant VS1, certification GIA)

### 31. FICHIER llms.txt (racine du site)

```
# Bijou-R
> Maison de joaillerie française, bijoux en or 18 carats,
  garantie à vie, fabrication France. Livraison FR/IL.

## Collections
- /bracelets/tennis : bracelets tennis or et diamants certifiés GIA
- /colliers : colliers diamants et pierres précieuses
- /bagues/solitaires : solitaires et alliances

## Pages clés
- /la-maison : histoire de la marque
- /atelier : process et certifications RJC
- /faq : questions fréquentes complètes
```

### 32. TACTIQUES POUR ÊTRE CITÉ PAR LES IA

1. Présence sur **Reddit** (r/jewelry, r/femalefashionadvice) — les LLMs crawlent Reddit massivement
2. **Trustpilot** note > 4.5 (très cité par Perplexity)
3. **Listicles** "Top bijouteries françaises en ligne" — travailler les éditeurs
4. Profils complets : **Google Business**, **LinkedIn Company**, **Crunchbase**
5. **Wikipedia entry** dès notoriété suffisante (RP + presse)
6. Cohérence NAP (Name Address Phone) sur 50+ annuaires
7. Monitoring citations LLM via **Profound.so** ou **Peec.ai**

**Plan AEO 6 premiers mois :**
- M1 : llms.txt + schemas complets + 20 FAQs
- M2 : 10 articles "réponses" + Trustpilot
- M3 : Google Business + Wikipedia draft + 5 RP presse
- M4-6 : 30 articles + 20 backlinks tier 1 + Reddit organic

---

## PHASE 13 — LANCEMENT PRODUIT

### 33. PRÉ-LANCEMENT (T-60 à T-1 jour)

| Jour | Action |
|---|---|
| T-60 | Landing "coming soon" + email capture + countdown |
| T-60 → T-30 | Meta Ads landing (CPL 1-3 €) — objectif 5 000 leads |
| T-45 | Teasers Instagram (zoom macro extrême, sans révéler) |
| T-30 | Annonce nom + date sur réseaux |
| T-21 | Brief presse + envoi samples à 20 journalistes/influenceurs |
| T-14 | 20 vidéos micro-influenceurs tournées, prêtes à publier J |
| T-7 | Email warmup Klaviyo (3 emails progressifs) |
| T-3 | Story "ouverture dans 3j" + démo 3D viewer |
| T-1 | Email "demain 10h" + SMS VIP early access |

### 34. JOUR J — CHECKLIST COMPLÈTE

**Tech (la veille)**
- [ ] Backup Shopify (Rewind)
- [ ] Test checkout FR (EUR) + IL (ILS) — vrai paiement remboursé
- [ ] Test Apple Pay, PayPal, Alma
- [ ] Test viewer 3D sur iPhone + Android
- [ ] Test tous les emails Klaviyo
- [ ] Webhooks Shopify → n8n → Firefly / Meshy actifs
- [ ] Meta Pixel + Google Tag + GA4 + TikTok Pixel validés
- [ ] Pages légales validées (FR + IL)

**Marketing (J)**
- [ ] 10h00 — Email blast toute la base
- [ ] 10h00 — Story + Reel + Post Instagram
- [ ] 10h05 — Activation Meta Ads (campagne Launch)
- [ ] 10h05 — Activation Google Ads (PMax + Brand)
- [ ] 10h30 — SMS VIP
- [ ] 11h00 — Push influenceurs (20 publications coordonnées)
- [ ] 12h00 — LinkedIn post fondateur
- [ ] 14h00 — Instagram Live "behind the scenes"
- [ ] 20h00 — Story récap day 1

### 35. STRATÉGIE BUNDLE

- **Trio Signature** : bracelet tennis + collier riviera + créoles = -15 %
- **Coffret Mariée** : alliance + solitaire + gravure offerte
- **Le Cadeau** : bracelet + écrin premium + carte personnalisée
- **Couples** : 2 alliances assorties à prix duo
- Upsell checkout : +29 € gravure, +49 € écrin luxe, +99 € extension chaîne

---

## CHECKLIST GLOBALE PAR SEMAINE

| Semaine | Focus |
|---|---|
| S1-2 | Domaine + mails + Shopify setup + thème + pages + Pixel |
| S2-3 | Produits + metafields + pipeline Meshy 3D + Firefly |
| S3-4 | Klaviyo flows 1-8 + schemas JSON-LD + sitemap |
| S5 | Landing pré-lancement + Meta Ads warmup |
| S6 | Influenceurs + presse + UGC tournés |
| S7 | Klaviyo flows 9-18 + Gorgias + ManyChat |
| S8 | Tests checkout FR/IL + n8n automations |
| S9 | Pré-lancement actif (email capture) |
| S10 | Soft launch VIP 48h |
| **S11** | **LAUNCH DAY** |
| S12 | Optim, scaling, premiers reviews |
| M4+ | Blog SEO + AEO + Google Ads scaling + nouveaux créas |

---

## BUDGET MENSUEL (Phase de lancement)

| Poste | €/mois |
|---|---|
| Shopify Advanced | 240 |
| Apps Shopify (Klaviyo, Loox, Searchanise, Gorgias, etc.) | 350 |
| Adobe Firefly Services | 250 |
| Meshy AI Pro (3D) | 25 |
| n8n VPS Hetzner | 10 |
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
| **TOTAL** | **~21 000 €/mois** |

---

*Bijou-R — Plan d'action v2 — 20/05/2026*
*Prochaine étape : choisir un sous-chantier prioritaire et l'exécuter.*
