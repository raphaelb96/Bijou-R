# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projet

Boutique e-commerce spécialisée en bijoux haute joaillerie (bagues diamant : solitaires, pavé, rivière), avec présence multicanal forte (Instagram, TikTok, Facebook, Pinterest, Google).

---

## Stack technique

### E-commerce
- **Shopify** — plateforme principale
- Thèmes bijouterie recommandés : Dawn, Prestige, Gem
- Apps Shopify à configurer : Google & YouTube, Klaviyo, Triple Whale

### Visuels IA
- **Kling AI** — vidéos produit 360°, animations bague sur main
- **Midjourney** — photos de mise en scène luxe
- **Adobe Firefly** — retouche et backgrounds

### Marketing & SEO
- **Shopify Magic** — descriptions produit SEO
- **Klaviyo** — emails automatiques post-achat, relances panier
- **Surfer SEO** — optimisation pages produit
- **AdCreative.ai** — visuels publicitaires

### Analytics
- **Triple Whale** — stats Shopify + réseaux sociaux centralisés

### CRM (phase 2)
- **HubSpot**

---

## Canaux de vente
- Google Shopping
- Instagram Shopping
- TikTok Shop
- Pinterest Product Pins
- Etsy (synchronisé via Shopify)

---

## Fichiers produit

Les modèles 3D sont au format `.csg` (CounterSketch / OpenNURBS) — non convertibles sans Rhino. Photos produit disponibles (fond blanc, rendu studio).

---

## Stratégie de contenu SEO / AEO

**Objectif dual** : référencement Google + présence dans les réponses IA (ChatGPT, Claude, Perplexity).

### Circuit de publication
1. Rédiger l'article (Claude)
2. Publier sur le blog Shopify
3. Republier sur Medium + LinkedIn
4. Transformer en épingle Pinterest
5. Créer une vidéo courte TikTok/Instagram basée sur l'article

### Sujets d'articles prioritaires
- "Comment choisir sa bague de fiançailles"
- "Diamant naturel vs diamant synthétique"
- "Les 4C du diamant expliqués simplement"
- "Comment connaître sa taille de bague"
- "Entretenir sa bague en or blanc"

---

## Prompts Kling AI validés

### Rotation 360° bague seule
```
Luxury diamond ring slow 360 degree rotation on perfectly white background, ring stays completely upright and vertical, rotating on its own vertical axis, never tilting or leaning, camera placed directly in front at eye level, straight-on frontal view throughout entire rotation, white gold band with perfectly symmetrical channel-set round diamonds running along both sides of the shank, matching diamond rivers on each side of the band mirroring each other perfectly, large round brilliant cut center diamond held by six prongs, ultra realistic diamond reflections, professional jewelry photography, studio lighting, seamless loop
```

### Bague sur main femme
```
Photorealistic luxury jewelry commercial, beautiful woman's manicured hand with nude nails picking up a diamond ring from an open black velvet jewelry box, soft natural light, skin texture ultra detailed, slow motion, cinematic depth of field, shot on Canon EOS R5, 8K
```

### Écrin luxe
```
Luxury diamond ring inside an open black velvet jewelry box, dramatic side lighting with golden reflections, dark elegant background, slow cinematic zoom, smoke effect, 4K jewelry commercial
```

---

## Import catalogue produit (grand volume)

### Principe
Ne pas saisir manuellement. Tout passe par un fichier CSV / Google Sheets importé en masse sur Shopify.
Structure : **une ligne = un produit** (titre, description, prix, SKU, URLs images, variantes tailles, collections, tags).

### Outils
- **Matrixify** (~$20/mois) — importateur Shopify avancé, indispensable pour grands catalogues. Gère les mises à jour, images, métadonnées. L'importateur natif Shopify est trop limité.
- **Claude** — génération de descriptions SEO en lot (50+ produits à la fois depuis un tableau de specs).
- Images : héberger sur Google Drive public ou Dropbox → référencer par URL dans le CSV → Matrixify les aspire automatiquement.

### Workflow
1. Structurer le catalogue en Google Sheets (1-2 jours selon volume)
2. Générer les descriptions en lot avec Claude (quelques heures)
3. Héberger les images et récupérer leurs URLs publiques
4. Importer via Matrixify (quelques heures)

### Point de départ à clarifier
La stratégie dépend du format actuel du catalogue :
- Tableur Excel/Google Sheets existant → partir directement de là
- Fiches PDF ou catalogue papier → extraction manuelle ou OCR d'abord
- Références issues des fichiers `.csg` seulement → reconstruire les fiches depuis les références

---

## Prochaines étapes

- [ ] Ouvrir compte Shopify (14 jours gratuit)
- [ ] Générer vidéos 360° sur Kling AI avec les prompts ci-dessus
- [ ] Rédiger 3 premiers articles SEO
- [ ] Configurer Klaviyo pour emails automatiques
- [ ] Connecter Instagram + TikTok + Pinterest à Shopify
- [ ] Configurer Google Shopping
