from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, numbers
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

wb = Workbook()

# ─── Couleurs ────────────────────────────────────────────────────────────────
OR         = "FFD700"
OR_LIGHT   = "FFF8DC"
NOIR       = "1A1A1A"
GRIS       = "F2F2F2"
GRIS_MED   = "D9D9D9"
BLANC      = "FFFFFF"
VERT       = "2E7D32"
VERT_LIGHT = "E8F5E9"
BLEU       = "1565C0"
BLEU_LIGHT = "E3F2FD"
ROUGE      = "B71C1C"
ROUGE_LIGHT= "FFEBEE"
VIOLET     = "6A1B9A"
VIOLET_LIGHT="F3E5F5"

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def font(bold=False, color=NOIR, size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")

def border_thin():
    s = Side(style="thin", color=GRIS_MED)
    return Border(left=s, right=s, top=s, bottom=s)

def border_medium():
    s = Side(style="medium", color=NOIR)
    return Border(left=s, right=s, top=s, bottom=s)

def center():
    return Alignment(horizontal="center", vertical="center", wrap_text=True)

def left():
    return Alignment(horizontal="left", vertical="center", wrap_text=True)

def apply_header(ws, row, col, value, bg=NOIR, fg=BLANC, size=10, bold=True):
    c = ws.cell(row=row, column=col, value=value)
    c.fill = fill(bg)
    c.font = font(bold=bold, color=fg, size=size)
    c.alignment = center()
    c.border = border_thin()
    return c

def apply_cell(ws, row, col, value=None, bg=BLANC, fg=NOIR, bold=False,
               align="left", border=True, italic=False, size=10, number_format=None):
    c = ws.cell(row=row, column=col, value=value)
    c.fill = fill(bg)
    c.font = font(bold=bold, color=fg, size=size, italic=italic)
    c.alignment = center() if align == "center" else left()
    if border:
        c.border = border_thin()
    if number_format:
        c.number_format = number_format
    return c

# ═══════════════════════════════════════════════════════════════════════════════
# ONGLET 1 — COURS
# ═══════════════════════════════════════════════════════════════════════════════
ws_cours = wb.active
ws_cours.title = "COURS"
ws_cours.sheet_properties.tabColor = OR

ws_cours.column_dimensions["A"].width = 35
ws_cours.column_dimensions["B"].width = 18
ws_cours.column_dimensions["C"].width = 18
ws_cours.column_dimensions["D"].width = 40

# Titre principal
ws_cours.merge_cells("A1:D1")
c = ws_cours["A1"]
c.value = "COURS DU MARCHÉ — BIJOU-R"
c.fill = fill(NOIR)
c.font = font(bold=True, color=OR, size=14)
c.alignment = center()
ws_cours.row_dimensions[1].height = 35

ws_cours.merge_cells("A2:D2")
c = ws_cours["A2"]
c.value = "⚠  Mettez à jour ces cellules jaunes pour recalculer tous les prix du catalogue"
c.fill = fill(OR_LIGHT)
c.font = font(bold=True, color=NOIR, size=10)
c.alignment = center()
ws_cours.row_dimensions[2].height = 22

# ── Section OR ────────────────────────────────────────────────────────────────
ws_cours.merge_cells("A3:D3")
c = ws_cours["A3"]
c.value = "OR"
c.fill = fill(OR)
c.font = font(bold=True, color=NOIR, size=11)
c.alignment = center()
ws_cours.row_dimensions[3].height = 20

headers = ["Paramètre", "Valeur", "Unité", "Note"]
for i, h in enumerate(headers, 1):
    apply_header(ws_cours, 4, i, h, bg=NOIR, fg=OR)
ws_cours.row_dimensions[4].height = 20

rows_or = [
    ("Cours de l'or (à mettre à jour)", 85.00, "€ / gramme", "Prix spot international converti en €/g"),
]
for i, (param, val, unit, note) in enumerate(rows_or, 5):
    apply_cell(ws_cours, i, 1, param, bg=OR_LIGHT, bold=True)
    c = apply_cell(ws_cours, i, 2, val, bg=OR, bold=True, align="center")
    c.number_format = '#,##0.00 "€"'
    apply_cell(ws_cours, i, 3, unit, bg=OR_LIGHT, align="center")
    apply_cell(ws_cours, i, 4, note, bg=OR_LIGHT, italic=True)
    ws_cours.row_dimensions[i].height = 18

# ── Section DIAMANTS NATURELS ─────────────────────────────────────────────────
ws_cours.merge_cells("A7:D7")
c = ws_cours["A7"]
c.value = "DIAMANTS NATURELS"
c.fill = fill(BLEU)
c.font = font(bold=True, color=BLANC, size=11)
c.alignment = center()
ws_cours.row_dimensions[7].height = 20

for i, h in enumerate(headers, 1):
    apply_header(ws_cours, 8, i, h, bg=BLEU, fg=BLANC)

rows_nat = [
    ("Naturel — N1 Essentiel",  1800, "€ / carat", "H-I / SI1-SI2 — entrée de gamme"),
    ("Naturel — N2 Sélection",  3500, "€ / carat", "G-H / VS2 — bon rapport qualité/prix"),
    ("Naturel — N3 Prestige",   6200, "€ / carat", "F-G / VS1 — haute joaillerie"),
    ("Naturel — N4 Excellence", 10500,"€ / carat", "E-F / VVS1-VVS2 — très haute joaillerie"),
    ("Naturel — N5 Exception",  18000,"€ / carat", "D / IF — collector"),
]
for i, (param, val, unit, note) in enumerate(rows_nat, 9):
    apply_cell(ws_cours, i, 1, param, bg=BLEU_LIGHT, bold=True)
    c = apply_cell(ws_cours, i, 2, val, bg=BLEU_LIGHT, bold=True, align="center")
    c.number_format = '#,##0 "€"'
    apply_cell(ws_cours, i, 3, unit, bg=BLEU_LIGHT, align="center")
    apply_cell(ws_cours, i, 4, note, bg=BLEU_LIGHT, italic=True)
    ws_cours.row_dimensions[i].height = 18

# ── Section DIAMANTS LABORATOIRE ──────────────────────────────────────────────
ws_cours.merge_cells("A15:D15")
c = ws_cours["A15"]
c.value = "DIAMANTS DE LABORATOIRE"
c.fill = fill(VIOLET)
c.font = font(bold=True, color=BLANC, size=11)
c.alignment = center()
ws_cours.row_dimensions[15].height = 20

for i, h in enumerate(headers, 1):
    apply_header(ws_cours, 16, i, h, bg=VIOLET, fg=BLANC)

rows_lab = [
    ("Labo — L1 Essentiel",  420,  "€ / carat", "H-I / SI1-SI2 — même qualité visuelle"),
    ("Labo — L2 Sélection",  780,  "€ / carat", "G-H / VS2"),
    ("Labo — L3 Prestige",   1300, "€ / carat", "F-G / VS1"),
    ("Labo — L4 Excellence", 2100, "€ / carat", "E-F / VVS1-VVS2"),
    ("Labo — L5 Exception",  3500, "€ / carat", "D / IF"),
]
for i, (param, val, unit, note) in enumerate(rows_lab, 17):
    apply_cell(ws_cours, i, 1, param, bg=VIOLET_LIGHT, bold=True)
    c = apply_cell(ws_cours, i, 2, val, bg=VIOLET_LIGHT, bold=True, align="center")
    c.number_format = '#,##0 "€"'
    apply_cell(ws_cours, i, 3, unit, bg=VIOLET_LIGHT, align="center")
    apply_cell(ws_cours, i, 4, note, bg=VIOLET_LIGHT, italic=True)
    ws_cours.row_dimensions[i].height = 18

# ═══════════════════════════════════════════════════════════════════════════════
# ONGLET 2 — CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
ws_cfg = wb.create_sheet("CONFIG")
ws_cfg.sheet_properties.tabColor = GRIS_MED

ws_cfg.column_dimensions["A"].width = 35
ws_cfg.column_dimensions["B"].width = 18
ws_cfg.column_dimensions["C"].width = 18
ws_cfg.column_dimensions["D"].width = 40

ws_cfg.merge_cells("A1:D1")
c = ws_cfg["A1"]
c.value = "CONFIGURATION — PARAMÈTRES FIXES"
c.fill = fill(NOIR)
c.font = font(bold=True, color=BLANC, size=14)
c.alignment = center()
ws_cfg.row_dimensions[1].height = 35

sections = [
    ("OR & MÉTAUX", NOIR, BLANC, [
        ("Pureté or 18k", 0.75, "facteur", "75% d'or pur dans l'alliage 18k"),
        ("Supplément or blanc (rhodium)", 0.08, "facteur +%", "Coût du plaquage rhodium"),
        ("Supplément or rose", 0.02, "facteur +%", "Alliage cuivre légèrement plus coûteux"),
    ]),
    ("FABRICATION", VERT, BLANC, [
        ("Main d'œuvre par défaut", 180.00, "€", "Modifiable ligne par ligne dans le catalogue"),
        ("Frais généraux fixes", 25.00, "€", "Emballage, écrin, certificat"),
    ]),
    ("TARIFICATION", ROUGE, BLANC, [
        ("Coefficient de marge", 2.8, "×", "Prix vente HT = prix revient × coefficient"),
        ("TVA", 0.20, "%", "20% — France"),
    ]),
]

row = 2
for section_name, bg, fg, params in sections:
    ws_cfg.merge_cells(f"A{row}:D{row}")
    c = ws_cfg[f"A{row}"]
    c.value = section_name
    c.fill = fill(bg)
    c.font = font(bold=True, color=fg, size=11)
    c.alignment = center()
    ws_cfg.row_dimensions[row].height = 20
    row += 1

    for i, h in enumerate(["Paramètre", "Valeur", "Unité", "Note"], 1):
        apply_header(ws_cfg, row, i, h, bg=bg, fg=fg)
    ws_cfg.row_dimensions[row].height = 18
    row += 1

    for param, val, unit, note in params:
        apply_cell(ws_cfg, row, 1, param, bg=GRIS, bold=True)
        c = apply_cell(ws_cfg, row, 2, val, bg=OR_LIGHT if bg == NOIR else GRIS, bold=True, align="center")
        if unit == "€":
            c.number_format = '#,##0.00 "€"'
        elif unit in ("facteur", "×"):
            c.number_format = "0.00"
        elif unit in ("facteur +%", "%"):
            c.number_format = "0%"
        apply_cell(ws_cfg, row, 3, unit, bg=GRIS, align="center")
        apply_cell(ws_cfg, row, 4, note, bg=GRIS, italic=True)
        ws_cfg.row_dimensions[row].height = 18
        row += 1

# ═══════════════════════════════════════════════════════════════════════════════
# ONGLET 3 — CATALOGUE
# ═══════════════════════════════════════════════════════════════════════════════
ws_cat = wb.create_sheet("CATALOGUE")
ws_cat.sheet_properties.tabColor = OR

# Colonnes
COL = {
    "REF":           1,
    "NOM":           2,
    "COLLECTION":    3,
    "METAL":         4,
    "TYPE_DIAM":     5,
    "NIVEAU_DIAM":   6,
    "POIDS_OR":      7,
    "CARATS":        8,
    "MAIN_OEUVRE":   9,
    "COUT_OR":       10,
    "COUT_DIAM":     11,
    "COUT_REVIENT":  12,
    "PRIX_HT":       13,
    "PRIX_TTC":      14,
}

widths = [14, 28, 18, 14, 16, 20, 13, 10, 14, 14, 14, 14, 14, 14]
for i, w in enumerate(widths, 1):
    ws_cat.column_dimensions[get_column_letter(i)].width = w

# Titre
ws_cat.merge_cells("A1:N1")
c = ws_cat["A1"]
c.value = "CATALOGUE PRODUITS — BIJOU-R"
c.fill = fill(NOIR)
c.font = font(bold=True, color=OR, size=14)
c.alignment = center()
ws_cat.row_dimensions[1].height = 35

# Groupes d'en-têtes (ligne 2 = groupes)
groups = [
    (1, 3, "IDENTITÉ PRODUIT", NOIR, BLANC),
    (4, 6, "MATIÈRES", BLEU, BLANC),
    (7, 9, "POIDS & FABRICATION", VERT, BLANC),
    (10, 11, "COÛTS MATIÈRES", ROUGE, BLANC),
    (12, 14, "PRIX CALCULÉS  ✦  ne pas modifier", OR, NOIR),
]
for start, end, label, bg, fg in groups:
    if start == end:
        ws_cat.cell(row=2, column=start)
    else:
        ws_cat.merge_cells(
            start_row=2, start_column=start, end_row=2, end_column=end
        )
    c = ws_cat.cell(row=2, column=start, value=label)
    c.fill = fill(bg)
    c.font = font(bold=True, color=fg, size=10)
    c.alignment = center()
    c.border = border_thin()
ws_cat.row_dimensions[2].height = 22

# En-têtes colonnes (ligne 3)
headers_cat = [
    ("Référence", NOIR, BLANC),
    ("Nom du modèle", NOIR, BLANC),
    ("Collection", NOIR, BLANC),
    ("Métal", BLEU, BLANC),
    ("Type diamant", BLEU, BLANC),
    ("Niveau diamant", BLEU, BLANC),
    ("Poids or (g)", VERT, BLANC),
    ("Carats", VERT, BLANC),
    ("Main d'œuvre (€)", VERT, BLANC),
    ("Coût or (€)", ROUGE, BLANC),
    ("Coût diamant (€)", ROUGE, BLANC),
    ("Prix de revient (€)", OR, NOIR),
    ("Prix HT (€)", OR, NOIR),
    ("Prix TTC (€)", OR, NOIR),
]
for i, (h, bg, fg) in enumerate(headers_cat, 1):
    apply_header(ws_cat, 3, i, h, bg=bg, fg=fg, size=9)
ws_cat.row_dimensions[3].height = 32
ws_cat.freeze_panes = "A4"

# ── Données exemples ──────────────────────────────────────────────────────────
# Formules de calcul (référencent COURS et CONFIG)
# COUT_OR  = poids_or * cours_or * pureté * coeff_métal
# COUT_DIAM= carats  * cours_diamant_selon_niveau
# REVIENT  = cout_or + cout_diam + main_oeuvre + frais_generaux
# HT       = revient * marge
# TTC      = HT * (1 + TVA)

def coeff_metal_formula(metal_col_letter):
    """Retourne le coefficient métal selon or blanc/rose/jaune."""
    return (
        f'IF({metal_col_letter}{{r}}="Or blanc",'
        f'1+CONFIG!B6,'
        f'IF({metal_col_letter}{{r}}="Or rose",'
        f'1+CONFIG!B7,1))'
    )

def cours_diam_formula(type_col, niv_col):
    """Retourne le cours diamant selon type (Naturel/Labo) et niveau (N1..N5 / L1..L5)."""
    # Naturel : COURS B9..B13, Labo : COURS B17..B21
    nat = (
        f'IF({niv_col}{{r}}="N1 Essentiel",COURS!B9,'
        f'IF({niv_col}{{r}}="N2 Sélection",COURS!B10,'
        f'IF({niv_col}{{r}}="N3 Prestige",COURS!B11,'
        f'IF({niv_col}{{r}}="N4 Excellence",COURS!B12,'
        f'IF({niv_col}{{r}}="N5 Exception",COURS!B13,0)))))'
    )
    lab = (
        f'IF({niv_col}{{r}}="L1 Essentiel",COURS!B17,'
        f'IF({niv_col}{{r}}="L2 Sélection",COURS!B18,'
        f'IF({niv_col}{{r}}="L3 Prestige",COURS!B19,'
        f'IF({niv_col}{{r}}="L4 Excellence",COURS!B20,'
        f'IF({niv_col}{{r}}="L5 Exception",COURS!B21,0)))))'
    )
    return f'IF({type_col}{{r}}="Naturel",{nat},{lab})'

sample_data = [
    # REF,              NOM,                    COLLECTION,  METAL,       TYPE,      NIVEAU
    ("SOL-001-OB-N", "Solitaire Éclat",       "Solitaires","Or blanc",  "Naturel", "N3 Prestige",  3.2, 1.00),
    ("SOL-001-OB-L", "Solitaire Éclat",       "Solitaires","Or blanc",  "Labo",    "L3 Prestige",  3.2, 1.00),
    ("SOL-001-OJ-N", "Solitaire Éclat",       "Solitaires","Or jaune",  "Naturel", "N3 Prestige",  3.2, 1.00),
    ("SOL-001-OR-N", "Solitaire Éclat",       "Solitaires","Or rose",   "Naturel", "N3 Prestige",  3.2, 1.00),
    ("PAV-001-OB-N", "Pavé Lumière",          "Pavé",      "Or blanc",  "Naturel", "N2 Sélection", 4.1, 0.48),
    ("PAV-001-OB-L", "Pavé Lumière",          "Pavé",      "Or blanc",  "Labo",    "L2 Sélection", 4.1, 0.48),
    ("ALI-001-OB-N", "Alliance Éternité",     "Alliances", "Or blanc",  "Naturel", "N1 Essentiel", 2.8, 0.30),
    ("ALI-001-OJ-N", "Alliance Éternité",     "Alliances", "Or jaune",  "Naturel", "N1 Essentiel", 2.8, 0.30),
]

DEFAULT_MO = 180  # valeur par défaut main d'oeuvre

metal_let  = get_column_letter(COL["METAL"])
type_let   = get_column_letter(COL["TYPE_DIAM"])
niv_let    = get_column_letter(COL["NIVEAU_DIAM"])
or_let     = get_column_letter(COL["POIDS_OR"])
car_let    = get_column_letter(COL["CARATS"])
mo_let     = get_column_letter(COL["MAIN_OEUVRE"])
cor_let    = get_column_letter(COL["COUT_OR"])
cdi_let    = get_column_letter(COL["COUT_DIAM"])
rev_let    = get_column_letter(COL["COUT_REVIENT"])
ht_let     = get_column_letter(COL["PRIX_HT"])
ttc_let    = get_column_letter(COL["PRIX_TTC"])

for idx, row_data in enumerate(sample_data, 4):
    ref, nom, coll, metal, typ, niv, poids, carats = row_data
    r = idx

    bg_row = OR_LIGHT if r % 2 == 0 else BLANC

    apply_cell(ws_cat, r, COL["REF"],        ref,    bg=bg_row, bold=True)
    apply_cell(ws_cat, r, COL["NOM"],        nom,    bg=bg_row)
    apply_cell(ws_cat, r, COL["COLLECTION"], coll,   bg=bg_row)

    # Métal — couleur selon type
    metal_bg = {"Or blanc": BLEU_LIGHT, "Or jaune": OR_LIGHT, "Or rose": ROUGE_LIGHT}.get(metal, bg_row)
    apply_cell(ws_cat, r, COL["METAL"], metal, bg=metal_bg, bold=True, align="center")

    # Type diamant
    typ_bg = BLEU_LIGHT if typ == "Naturel" else VIOLET_LIGHT
    apply_cell(ws_cat, r, COL["TYPE_DIAM"], typ, bg=typ_bg, bold=True, align="center")

    apply_cell(ws_cat, r, COL["NIVEAU_DIAM"], niv, bg=bg_row, align="center")

    c = apply_cell(ws_cat, r, COL["POIDS_OR"], poids, bg=bg_row, align="center")
    c.number_format = '0.0 "g"'

    c = apply_cell(ws_cat, r, COL["CARATS"], carats, bg=bg_row, align="center")
    c.number_format = '0.00 "ct"'

    # Main d'oeuvre — valeur par défaut depuis CONFIG (modifiable manuellement)
    c = apply_cell(ws_cat, r, COL["MAIN_OEUVRE"], None, bg=OR_LIGHT, bold=True, align="center")
    c.value = f"=CONFIG!$B$8"
    c.number_format = '#,##0 "€"'

    # Coût or = poids * cours_or * pureté * coeff_métal
    coeff = coeff_metal_formula(metal_let)
    c = apply_cell(ws_cat, r, COL["COUT_OR"], None, bg=ROUGE_LIGHT, align="center")
    c.value = (
        f"=ROUND({or_let}{r}*COURS!$B$5*CONFIG!$B$5*{coeff.format(r=r)},2)"
    )
    c.number_format = '#,##0.00 "€"'

    # Coût diamant = carats * cours selon niveau
    cours_f = cours_diam_formula(type_let, niv_let).format(r=r)
    c = apply_cell(ws_cat, r, COL["COUT_DIAM"], None, bg=ROUGE_LIGHT, align="center")
    c.value = f"=ROUND({car_let}{r}*{cours_f},2)"
    c.number_format = '#,##0.00 "€"'

    # Prix de revient = cout_or + cout_diam + main_oeuvre + frais généraux
    c = apply_cell(ws_cat, r, COL["COUT_REVIENT"], None, bg=OR_LIGHT, bold=True, align="center")
    c.value = f"=ROUND({cor_let}{r}+{cdi_let}{r}+{mo_let}{r}+CONFIG!$B$9,2)"
    c.number_format = '#,##0.00 "€"'

    # Prix HT = revient * marge
    c = apply_cell(ws_cat, r, COL["PRIX_HT"], None, bg=OR_LIGHT, bold=True, align="center")
    c.value = f"=ROUND({rev_let}{r}*CONFIG!$B$11,2)"
    c.number_format = '#,##0.00 "€"'

    # Prix TTC = HT * (1 + TVA)
    c = apply_cell(ws_cat, r, COL["PRIX_TTC"], None, bg=OR, bold=True, align="center")
    c.value = f"=ROUND({ht_let}{r}*(1+CONFIG!$B$12),2)"
    c.number_format = '#,##0.00 "€"'

    ws_cat.row_dimensions[r].height = 20

# Ligne "Ajouter ici" pour guider
next_r = len(sample_data) + 4
ws_cat.merge_cells(f"A{next_r}:N{next_r}")
c = ws_cat[f"A{next_r}"]
c.value = "⟶  Ajouter vos produits à partir de cette ligne en copiant une ligne existante"
c.fill = fill(GRIS)
c.font = font(italic=True, color="888888", size=9)
c.alignment = center()
ws_cat.row_dimensions[next_r].height = 18

# Validations données
dv_metal = DataValidation(
    type="list",
    formula1='"Or blanc,Or jaune,Or rose"',
    showDropDown=False
)
dv_type = DataValidation(
    type="list",
    formula1='"Naturel,Labo"',
    showDropDown=False
)
dv_niv = DataValidation(
    type="list",
    formula1='"N1 Essentiel,N2 Sélection,N3 Prestige,N4 Excellence,N5 Exception,L1 Essentiel,L2 Sélection,L3 Prestige,L4 Excellence,L5 Exception"',
    showDropDown=False
)
ws_cat.add_data_validation(dv_metal)
ws_cat.add_data_validation(dv_type)
ws_cat.add_data_validation(dv_niv)
dv_metal.sqref = f"D4:D500"
dv_type.sqref  = f"E4:E500"
dv_niv.sqref   = f"F4:F500"

# ═══════════════════════════════════════════════════════════════════════════════
# ONGLET 4 — EXPORT SHOPIFY
# ═══════════════════════════════════════════════════════════════════════════════
ws_exp = wb.create_sheet("EXPORT SHOPIFY")
ws_exp.sheet_properties.tabColor = VERT

exp_headers = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Type",
    "Tags", "Published", "Option1 Name", "Option1 Value",
    "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value",
    "Variant SKU", "Variant Price", "Variant Compare At Price",
    "Variant Inventory Qty", "Image Src", "Image Alt Text", "SEO Title", "SEO Description"
]

ws_exp.column_dimensions["A"].width = 22
ws_exp.column_dimensions["B"].width = 30
ws_exp.column_dimensions["C"].width = 40
for i in range(4, len(exp_headers) + 1):
    ws_exp.column_dimensions[get_column_letter(i)].width = 18

ws_exp.merge_cells(f"A1:{get_column_letter(len(exp_headers))}1")
c = ws_exp["A1"]
c.value = "EXPORT SHOPIFY — Format prêt pour import Matrixify"
c.fill = fill(VERT)
c.font = font(bold=True, color=BLANC, size=13)
c.alignment = center()
ws_exp.row_dimensions[1].height = 30

for i, h in enumerate(exp_headers, 1):
    apply_header(ws_exp, 2, i, h, bg=NOIR, fg=BLANC, size=9)
ws_exp.row_dimensions[2].height = 28
ws_exp.freeze_panes = "A3"

# Instructions
ws_exp.merge_cells(f"A3:{get_column_letter(len(exp_headers))}3")
c = ws_exp["A3"]
c.value = (
    "ℹ  Remplissez cet onglet depuis le CATALOGUE en copiant Référence → Handle, Nom → Title, Prix TTC → Variant Price. "
    "Ajoutez les variantes de taille (une ligne par taille, même Handle). Exportez en .CSV pour Matrixify."
)
c.fill = fill(GRIS)
c.font = font(italic=True, color=NOIR, size=9)
c.alignment = left()
ws_exp.row_dimensions[3].height = 32

# Exemple de ligne export
example_exp = [
    "solitaire-eclat-ob-n", "Solitaire Éclat — Or Blanc — Diamant Naturel",
    "<p>Description SEO à remplir</p>", "Bijou-R", "Bague Solitaire",
    "solitaire, diamant naturel, or blanc, fiançailles", "TRUE",
    "Taille", "52",
    "Métal", "Or blanc",
    "Diamant", "N3 Prestige",
    "SOL-001-OB-N-52", "=CATALOGUE!N4", "", "3",
    "https://url-image.com/bague.jpg", "Solitaire Éclat diamant naturel 1ct or blanc",
    "Bague Solitaire Diamant 1ct Or Blanc — Bijou-R",
    "Découvrez notre solitaire Éclat, diamant naturel 1 carat F/VS1 serti en or blanc 18k."
]
for i, val in enumerate(example_exp, 1):
    c = apply_cell(ws_exp, 4, i, val, bg=GRIS)
    c.font = font(size=8, italic=True, color="555555")
ws_exp.row_dimensions[4].height = 18

# ── Sauvegarde ────────────────────────────────────────────────────────────────
output = "/home/user/Bijou-R/Catalogue_Bijou-R.xlsx"
wb.save(output)
print(f"Fichier créé : {output}")
