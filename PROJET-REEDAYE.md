# PROJET REEDAYE — Contexte & Mémoire de session

> Fichier de référence centralisé pour le projet de site e-commerce de bijouterie/diamants.
> Quand tu (le user) me dis « réfère-toi à ce fichier » ou « regarde le projet », c'est ici que je viens lire le contexte.

---

## 1. Identité de la marque

| Élément | Valeur |
|---|---|
| **Nom de marque** | **Reedaye** *(orthographe à confirmer définitivement)* |
| **Localisation** | Israël (le user vit et opère depuis Israël) |
| **Identité visuelle** | À définir — pas encore de logo, charte couleur, typo confirmés |

---

## 2. Modèle économique

**Made-to-order / Dropship fabricant** — modèle clé à retenir :

- Le user **ne stocke rien**.
- Le user a un **fabricant en Israël** qui fournit aussi les diamants.
- Workflow d'une commande :
  1. Client commande sur le site Reedaye (diamant + type de bijou)
  2. User transmet la commande complète au fabricant israélien
  3. Fabricant produit la bijouterie sertie + livraison

**Conséquence majeure** : aucun investissement initial en inventaire. C'est un avantage énorme pour démarrer.

---

## 3. Catalogue produits

6 catégories vendues :

1. **Bagues** (joaillerie générale, sans pierre principale)
2. **Diamants** (loose / nus)
3. **Bagues en diamant** (engagement rings — produit phare attendu)
4. **Boucles d'oreilles**
5. **Colliers**
6. **Pendentifs**

**Plan catalogue** :
- Phase 1 : **10 produits** au démarrage (le temps de configurer)
- Phase 2 : **50 produits** une fois le site stabilisé
- Suite : montée en charge progressive

---

## 4. Langues et internationalisation

| Langue | Code | Note |
|---|---|---|
| Français | `fr` | Marché probable principal |
| Anglais | `en` | Marché international |
| **Hébreu** | `he` | **RTL obligatoire** (right-to-left) — choix de thème critique |

**Devises envisagées** : EUR, USD, ILS — devise principale à confirmer.

---

## 5. Décisions tech actées

| Décision | Statut |
|---|---|
| **Plateforme** | **Shopify Basic** (32 €/mois) au démarrage. PAS Shopify Plus. |
| **Pas de stock** | Confirmé (modèle made-to-order) |
| **Pas de custom dev lourd** | Confirmé — on reste sur apps Shopify standard |
| **Configurateur** | Nécessaire pour les bagues en diamant (diamant + setting) |
| **360° viewer** | Souhaité (style Blue Nile mais avec les vidéos du fabricant) |
| **AR try-on** | Phase 2 (Shopify AR natif gratuit possible) |

---

## 6. Budget validé (recalibré et accepté)

**One-shot (démarrage)** :
- Domaine : ~12 €/an
- Thème premium éventuel : ~300 €
- Setup site : fait par Claude gratuitement dans cette branche Git
- **Total estimé : 12-300 €**

**Mensuel récurrent** :
- Shopify Basic : 32 €/mois
- Apps essentielles : 0-50 €/mois (la plupart ont free tiers)
- BNPL : commission par vente, pas d'abonnement
- **Total estimé : 32-80 €/mois**

→ **Confirmé : ce n'est PAS 3-4 K€/mois.** C'était l'estimation pour Shopify Plus + catalogue diamant live à la Blue Nile, ce qui n'est pas nécessaire ici.

---

## 7. Apps Shopify pressenties

À installer au démarrage :

| Fonction | App suggérée | Coût |
|---|---|---|
| Configurateur bague | Customily ou Inkybay | 0-30 €/mois |
| 360° produit | Magic 360 ou Sirv | ~20 €/mois |
| Reviews | Judge.me | Gratuit |
| Email marketing | Klaviyo | Gratuit jusqu'à 250 contacts |
| Live chat | Shopify Inbox | Gratuit |
| Wishlist | Smart Wishlist | Gratuit |
| Page builder éditorial | GemPages ou PageFly | ~30 €/mois (optionnel) |
| BNPL international | Klarna, PayPal Pay Later, Alma | Gratuit à installer |
| Cookie consent (RGPD) | Cookiebot ou Iubenda | Free tier |
| Multi-langue | Shopify Markets + Translate & Adapt | Natif gratuit |

---

## 8. Référence d'inspiration : Blue Nile

**Analyse complète disponible** dans le repo :
- 📄 PDF : `analyse-bluenile/bluenile-analyse-complete.pdf` (23 pages)
- 🐍 Script générateur : `analyse-bluenile/build_report.py`

**Points clés à retenir de l'analyse Blue Nile pour Reedaye** :

- Blue Nile **n'est PAS sur Shopify** (plateforme propriétaire R2Net). On ne cherche pas à les cloner techniquement, juste à reproduire **l'expérience visuelle et le parcours utilisateur**.
- Les **photos « bague sur main »** chez Blue Nile sont des **renders 3D / CGI** (pas IA, pas vraies photos). À reproduire : demander au fabricant des renders 3D ou les produire à part.
- Les **photos diamants 360°** chez Blue Nile = scans réels via Segoma (machine propriétaire). Pour Reedaye, on utilisera les vidéos fournies par le fabricant + un viewer Magic360/Sirv.
- Le **Build Your Own Ring** en 3 étapes (diamant → setting → preview) est le différenciateur historique de Blue Nile. À reproduire absolument côté Reedaye.
- Blue Nile mise sur les **showrooms physiques** + **virtual showroom visio**. Reedaye peut imiter le virtual showroom via Calendly + Google Meet/Zoom au démarrage.
- **Éducation/contenu** : Blue Nile a un education center massif (4C, certifications GCAL/GemEx, ring guides). C'est un levier SEO majeur à reproduire en FR/EN/HE.
- **Trust signals** : reviews, garanties (lifetime warranty), retour 30 jours, assurance livraison, certifications GIA/IGI.

---

## 9. Spécificités liées à l'origine Israël

À prendre en compte dans le site et la logistique :

- **Diamants exportés > 1 ct** → documents **Kimberley Process** requis (à charge fabricant).
- **TVA Israël = 0 %** pour export, mais client final paie TVA + douane dans son pays.
- **« Made in Israel »** : à assumer comme argument marketing (artisanat israélien, savoir-faire Tel Aviv/Ramat Gan). À noter : peut générer des frictions sur certains marchés liés au BDS — à anticiper dans le branding.
- **Expédition internationale** : DHL ou FedEx depuis Israël, assuré et tracké. Délai habituel : 5-10 jours ouvrés.
- **Hébreu RTL** : choix du thème Shopify doit impérativement supporter RTL nativement (la majorité des thèmes modernes le font).
- **Conformité RGPD** (pour marché européen) : cookies, droit à l'oubli, hébergement données — à configurer dès le départ.

---

## 10. Points en suspens / à confirmer

À répondre par le user avant de pouvoir construire :

- [ ] **Orthographe exacte du nom de marque** : Reedaye ? Redaye ? Réédaye ? Autre ?
- [ ] **Devise par défaut** affichée : EUR, USD ou ILS ?
- [ ] **Marché cible principal** : France, US, Israël, autre ?
- [ ] **Logo / identité visuelle** : existante ou à créer ?
- [ ] **Photos produit** : déjà dispo ou à produire ?
- [ ] **Statut juridique** : auto-entrepreneur israélien, société, autre ?
- [ ] **Compte Shopify** : déjà créé ou pas encore ?
- [ ] **Domaine** : acheté ou pas ?
- [ ] **Fournisseur de paiement Israël** : Stripe, Tranzila, PayPlus, autre ? (Stripe pas dispo en Israël, à étudier)

---

## 11. Historique de la conversation (résumé chronologique)

1. **Demande initiale** : analyse complète de bluenile.com pour aider le user à décider Shopify vs autre.
2. **PDF d'analyse Blue Nile** généré (23 pages) — `analyse-bluenile/bluenile-analyse-complete.pdf`.
3. **Question Shopify vs autre** : verdict → Shopify suffit largement pour Reedaye.
4. **Recalibrage budget** : passage de 3-4 K€/mois (Shopify Plus erroné) à 32-80 €/mois (Shopify Basic, le vrai bon plan).
5. **Précision modèle** : positionnement diamant configurable + made-to-order via fabricant Israël.
6. **Demande de construction du site** : mise en pause par le user (« ne lance rien »).
7. **Création de ce fichier de contexte** (présent fichier) pour mémoire de session.

---

## 12. Prochaines étapes possibles (quand le user dira go)

Au feu vert, voici ce qui sera fait dans la branche Git :

1. Sélection et configuration d'un thème Shopify trilingue avec RTL hébreu
2. Construction des 6 pages catégories
3. Template fiche produit avec configurateur diamant + setting
4. Page « À propos » / « Made in Israel »
5. Pages éducatives (4C, guide bague de fiançailles, certifications)
6. Page politique livraison internationale / retour / garantie
7. Configuration Shopify Markets pour multi-langue + multi-devise
8. Liste précise des apps à installer avec ordre de priorité
9. Guide d'import des 10 premiers produits
10. Brief pour le fabricant (photos et vidéos requises par SKU)

---

*Dernière mise à jour : mai 2026 — session initiale Bijou-R / Reedaye.*
*Pour mettre à jour ce fichier : édite-le directement ou demande-moi de le mettre à jour.*
