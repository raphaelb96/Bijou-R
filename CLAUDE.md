# CLAUDE.md

Fichier d'orientation pour Claude Code sur le projet **Bijou-R**.

---

## Comment reprendre une session

Quand l'utilisateur démarre une nouvelle conversation, il suffit de lire :

1. **`PLAN_COMPLET_BIJOUR.md`** → plan stratégique final (vision, branding, produits, automations, budget)
2. **`GUIDE_EXECUTION_PAS_A_PAS.txt`** → guide d'exécution opérationnel (19 blocs, du Bloc 0 au Bloc 18)

Ces deux fichiers contiennent tout le contexte actuel.

---

## Le projet en une phrase

E-commerce de bijoux haute joaillerie (bracelets tennis, colliers, bagues, boucles d'oreilles) ciblant France + Israël, vendu via Shopify, avec stratégie d'acquisition organique TikTok/Instagram et automations no-code (n8n self-hosted).

---

## Phase actuelle

**Phase 1 — Site + Optimisation + Automations** (en cours)

La Phase 2 (Marketing : TikTok organique, Instagram, premières pubs) est **verrouillée** tant que la Phase 1 n'est pas finie.

---

## Stack technique (résumé)

| Couche | Outil | Coût |
|---|---|---|
| E-commerce | Shopify Basic | 39 €/mois |
| Domaine | Cloudflare Registrar | ~10 €/an |
| Email pro | Google Workspace Starter | 6 €/mois |
| Email marketing | Klaviyo (free <250 contacts) | 0 € |
| Automations | n8n self-hosted (Hetzner CX11) | 3,50 €/mois |
| 3D produit | Meshy AI Pro + Shopify model-viewer natif | 20 $/mois |
| Photos IA | Adobe Firefly (inclus CC) + Stability AI API | 0 € + ~0,01 €/image |
| Social DM | ManyChat (free) | 0 € |
| Marque (FR) | INPI classes 14 + 35 | 270 € one-shot |

Budget Phase 1 ≈ **78 €/mois récurrent**.

---

## Fichiers de référence dans le repo

| Fichier | Rôle |
|---|---|
| `PLAN_COMPLET_BIJOUR.md` | Source de vérité stratégique |
| `GUIDE_EXECUTION_PAS_A_PAS.txt` | Source de vérité opérationnelle |
| `Catalogue_Bijou-R.xlsx` | Calculateur de prix avec onglets TABLE_POIDS / COURS / CONFIG / CATALOGUE / EXPORT SHOPIFY |
| `catalogue_bijoux.py` | Script Python qui régénère le `.xlsx` (lance `python3 catalogue_bijoux.py`) |
| `analyse-bluenile/` | PDF + script d'analyse Blue Nile (référence d'inspiration UX/visuelle) |

---

## Règles de travail

- Travailler sur la branche `Dev` (pas directement sur `main`)
- Le user déclenche lui-même les merges vers `main`
- Quand un plan évolue, mettre à jour **PLAN_COMPLET_BIJOUR.md** et **GUIDE_EXECUTION_PAS_A_PAS.txt** plutôt que créer un nouveau fichier
- Ne pas créer de nouveaux fichiers .md sans nécessité (éviter la prolifération)
