# CLAUDE.md — Bijou-R

## ⚡ INSTRUCTION CRITIQUE — À EXÉCUTER EN PREMIER

**Au démarrage de CHAQUE session, avant toute réponse :**

1. Lire `/home/user/Bijou-R/PLAN_COMPLET_BIJOUR.md` (plan stratégique complet)
2. Lire `/home/user/Bijou-R/GUIDE_EXECUTION_PAS_A_PAS.txt` (guide d'exécution bloc par bloc)

Ne pas répondre sans avoir lu ces deux fichiers. Ils contiennent TOUT le contexte du projet.

---

## Le projet

**Bijou-R** — boutique e-commerce de bijoux haute joaillerie.
- Produits : bracelets tennis, colliers, bagues, boucles d'oreilles
- Marchés : France + Israël (€ + ₪)
- Canal principal : TikTok organique + Instagram Reels
- Plateforme : Shopify Basic (39 €/mois)

---

## Phase en cours

**Phase 1 — Site + Optimisation + Automations**

Phase 2 (Marketing TikTok/Instagram/pubs) = **VERROUILLÉE**. Ne pas démarrer tant que Phase 1 n'est pas terminée.

---

## Stack technique

| Couche | Outil | Coût |
|---|---|---|
| E-commerce | Shopify Basic | 39 €/mois |
| Domaine | Cloudflare Registrar | ~10 €/an |
| Email pro | Google Workspace Starter | 6 €/mois |
| Email marketing | Klaviyo (free <250 contacts) | 0 € |
| Automations | n8n self-hosted (Hetzner CX11 VPS) | 3,50 €/mois |
| 3D produit | Meshy AI Pro + Shopify model-viewer | 20 $/mois |
| Photos IA | Adobe Firefly (CC inclus) + Stability AI API | ~0,01 €/image auto |
| Social DM | ManyChat (free) | 0 € |
| Marque FR | INPI classes 14 + 35 | 270 € one-shot |

**Budget Phase 1 ≈ 78 €/mois**

---

## Fichiers du repo

| Fichier | Rôle |
|---|---|
| `PLAN_COMPLET_BIJOUR.md` | Source de vérité stratégique — lire EN PREMIER |
| `GUIDE_EXECUTION_PAS_A_PAS.txt` | Source de vérité opérationnelle — lire EN DEUXIÈME |
| `Catalogue_Bijou-R.xlsx` | Calculateur de prix (5 onglets : TABLE_POIDS / COURS / CONFIG / CATALOGUE / EXPORT SHOPIFY) |
| `catalogue_bijoux.py` | Script Python qui régénère le `.xlsx` (`python3 catalogue_bijoux.py`) |
| `analyse-bluenile/` | Analyse Blue Nile (référence UX/visuelle) |

---

## Règles de travail

- Branche de travail : **`Dev`** (jamais directement sur `main`)
- Les merges `Dev` → `main` sont déclenchés par le user uniquement
- Mettre à jour `PLAN_COMPLET_BIJOUR.md` et `GUIDE_EXECUTION_PAS_A_PAS.txt` quand le plan évolue — ne pas créer de nouveaux fichiers .md
- Ne JAMAIS inventer des actions non demandées (ne pas passer en Phase 2 sans instruction explicite)

---

## Contexte produits (résumé rapide)

10 SKUs au lancement :
1. Bracelet Tennis Signature Or Blanc 18k 3ct — **24 990 €** (ancre prix psychologique)
2. Bracelet Tennis Or Blanc 18k 1ct — 6 990 €
3. Bracelet Tennis Or Jaune 14k 1ct — **2 490 €** (hero product)
4. Bracelet Tennis Vermeil 0,5ct — 890 €
5. Bracelet Tennis Argent 925 1ct — 290 €
6. Collier Riviera 9 Diamants Or Blanc — 1 890 €
7. Collier Pendentif Diamant Solitaire — 590 €
8. Bague Solitaire Diamant Or Blanc — 1 490 €
9. Boucles d'Oreilles Créoles Or 18k — 449 €
10. Set Cadeau Collier + Boucles — 790 €
