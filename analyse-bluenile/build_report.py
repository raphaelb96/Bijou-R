#!/usr/bin/env python3
"""
Analyse complète de bluenile.com - Génération PDF
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Image, ListFlowable, ListItem, Flowable
)
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics import renderPDF

OUT = "/home/user/Bijou-R/analyse-bluenile/bluenile-analyse-complete.pdf"

# Palette inspirée Blue Nile
BN_BLUE       = colors.HexColor("#0E3A66")
BN_BLUE_DARK  = colors.HexColor("#08243F")
BN_BLUE_LIGHT = colors.HexColor("#E6EEF6")
BN_GOLD       = colors.HexColor("#C9A24B")
BN_GREY       = colors.HexColor("#4A4A4A")
BN_LIGHT      = colors.HexColor("#F6F6F6")
BN_WHITE      = colors.white

styles = getSampleStyleSheet()

# ----- Styles personnalisés -----
H_COVER = ParagraphStyle("HCover", parent=styles["Title"], fontName="Helvetica-Bold",
                         fontSize=34, leading=40, textColor=BN_BLUE_DARK, alignment=TA_LEFT,
                         spaceAfter=6)
H_COVER_SUB = ParagraphStyle("HCoverSub", parent=styles["Normal"], fontName="Helvetica",
                             fontSize=14, leading=18, textColor=BN_GREY, alignment=TA_LEFT,
                             spaceAfter=2)
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                    fontSize=22, leading=26, textColor=BN_BLUE_DARK, spaceBefore=8, spaceAfter=10)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                    fontSize=15, leading=19, textColor=BN_BLUE, spaceBefore=12, spaceAfter=6)
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontName="Helvetica-Bold",
                    fontSize=12, leading=16, textColor=BN_BLUE, spaceBefore=8, spaceAfter=4)
BODY = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica",
                      fontSize=10, leading=14, textColor=colors.black, alignment=TA_LEFT,
                      spaceAfter=4)
BODY_J = ParagraphStyle("BodyJ", parent=BODY, alignment=TA_JUSTIFY)
SMALL = ParagraphStyle("Small", parent=BODY, fontSize=8, leading=11, textColor=BN_GREY)
QUOTE = ParagraphStyle("Quote", parent=BODY, fontName="Helvetica-Oblique",
                       leftIndent=14, rightIndent=14, textColor=BN_BLUE_DARK,
                       borderColor=BN_GOLD, borderPadding=8, borderWidth=0,
                       backColor=BN_BLUE_LIGHT, spaceBefore=4, spaceAfter=8)
TAG = ParagraphStyle("Tag", parent=BODY, fontSize=9, leading=11, textColor=BN_WHITE,
                     backColor=BN_BLUE, alignment=TA_CENTER)

# ----- Helpers -----
def P(txt, style=BODY):
    return Paragraph(txt, style)

def bullets(items, style=BODY):
    flow = [Paragraph(f"• {it}", style) for it in items]
    return flow

def kv_table(rows, col_widths=(5.5*cm, 11.5*cm)):
    data = [[P(f"<b>{k}</b>"), P(v)] for k, v in rows]
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), BN_BLUE_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
    ]))
    return t

def section_card(title, body_paragraphs):
    inner = [P(f"<b>{title}</b>", H3)] + body_paragraphs
    t = Table([[inner]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BN_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, BN_BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t

# ===== Schéma : maquette homepage =====
class HomepageMockup(Flowable):
    def __init__(self, width=17*cm, height=20*cm):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height

        # Cadre extérieur
        c.setStrokeColor(BN_BLUE)
        c.setLineWidth(0.8)
        c.rect(0, 0, w, h)

        # Top utility bar
        c.setFillColor(BN_BLUE_DARK)
        c.rect(0, h-0.6*cm, w, 0.6*cm, fill=1, stroke=0)
        c.setFillColor(BN_WHITE)
        c.setFont("Helvetica", 6)
        c.drawString(0.3*cm, h-0.4*cm, "Free Shipping  |  30-Day Returns  |  Virtual Showroom  |  Sign In  |  Cart")

        # Logo bar
        c.setFillColor(BN_WHITE)
        c.rect(0, h-1.8*cm, w, 1.2*cm, fill=1, stroke=0)
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.5*cm, h-1.35*cm, "Blue Nile")
        # Search bar
        c.setStrokeColor(colors.grey)
        c.setFillColor(colors.white)
        c.roundRect(w/2-3*cm, h-1.55*cm, 6*cm, 0.7*cm, 3, fill=1, stroke=1)
        c.setFillColor(BN_GREY)
        c.setFont("Helvetica-Oblique", 7)
        c.drawString(w/2-2.8*cm, h-1.3*cm, "Search diamonds, rings, jewelry…")

        # Main nav
        c.setFillColor(BN_BLUE_LIGHT)
        c.rect(0, h-2.4*cm, w, 0.6*cm, fill=1, stroke=0)
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 7)
        nav = ["ENGAGEMENT", "WEDDING", "DIAMONDS", "JEWELRY", "GIFTS", "EDUCATION", "SHOWROOMS"]
        x = 0.4*cm
        for n in nav:
            c.drawString(x, h-2.2*cm, n)
            x += (w-1*cm)/len(nav)

        # Hero
        c.setFillColor(BN_BLUE_LIGHT)
        c.rect(0, h-9*cm, w, 6.4*cm, fill=1, stroke=0)
        c.setStrokeColor(BN_GOLD)
        c.setLineWidth(0.4)
        # diamant illustratif
        c.line(w*0.75-1*cm, h-5.8*cm, w*0.75+1*cm, h-5.8*cm)
        c.line(w*0.75-1*cm, h-5.8*cm, w*0.75, h-7.8*cm)
        c.line(w*0.75+1*cm, h-5.8*cm, w*0.75, h-7.8*cm)
        c.line(w*0.75-1*cm, h-5.8*cm, w*0.75-0.5*cm, h-5.2*cm)
        c.line(w*0.75+1*cm, h-5.8*cm, w*0.75+0.5*cm, h-5.2*cm)
        c.line(w*0.75-0.5*cm, h-5.2*cm, w*0.75+0.5*cm, h-5.2*cm)
        c.line(w*0.75-0.5*cm, h-5.2*cm, w*0.75, h-7.8*cm)
        c.line(w*0.75+0.5*cm, h-5.2*cm, w*0.75, h-7.8*cm)

        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.7*cm, h-4*cm, "Up to 50% Off — Anniversary Sale")
        c.setFont("Helvetica", 8)
        c.drawString(0.7*cm, h-4.7*cm, "Discover curated engagement rings,")
        c.drawString(0.7*cm, h-5.1*cm, "designer settings & natural diamonds.")
        c.setFillColor(BN_BLUE)
        c.rect(0.7*cm, h-6*cm, 2.5*cm, 0.6*cm, fill=1, stroke=0)
        c.setFillColor(BN_WHITE)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(1.4*cm, h-5.8*cm, "SHOP NOW")

        # Category tiles
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.5*cm, h-9.7*cm, "Shop By Category")
        tiles = ["Engagement", "Wedding", "Diamonds", "Necklaces", "Earrings", "Bracelets"]
        tile_w = (w - 0.7*cm) / 6 - 0.1*cm
        for i, t in enumerate(tiles):
            x = 0.35*cm + i*(tile_w + 0.1*cm)
            c.setFillColor(BN_LIGHT)
            c.setStrokeColor(BN_BLUE)
            c.rect(x, h-12.5*cm, tile_w, 2.4*cm, fill=1, stroke=1)
            c.setFillColor(BN_BLUE_DARK)
            c.setFont("Helvetica", 6.5)
            c.drawCentredString(x+tile_w/2, h-12.2*cm, t)

        # Build Your Own / Creative Studio block
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.5*cm, h-13.1*cm, "Design It — Build Your Own Ring  |  Creative Studio  |  Diamond Search")
        c.setFillColor(BN_GOLD)
        c.rect(0.5*cm, h-15.3*cm, w-1*cm, 1.7*cm, fill=0, stroke=1)
        c.setFillColor(BN_BLUE)
        c.setFont("Helvetica", 7)
        c.drawString(0.8*cm, h-14.2*cm, "STEP 1  Diamond")
        c.drawString(0.8*cm + (w-2*cm)/3, h-14.2*cm, "STEP 2  Setting")
        c.drawString(0.8*cm + 2*(w-2*cm)/3, h-14.2*cm, "STEP 3  Complete")
        c.setFillColor(BN_BLUE_LIGHT)
        c.rect(0.8*cm, h-15*cm, 5*cm, 0.5*cm, fill=1, stroke=0)

        # Editorial / Studio collection
        c.setFillColor(BN_LIGHT)
        c.rect(0.5*cm, h-19*cm, w-1*cm, 3.5*cm, fill=1, stroke=0)
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.8*cm, h-16.1*cm, "Blue Nile Studio · Astor · Designer Collections")
        c.setFont("Helvetica", 7)
        c.setFillColor(BN_GREY)
        c.drawString(0.8*cm, h-16.7*cm, "Editorial lifestyle photography + 360° HD product views — curated 'elevated' positioning")

        # Footer mock
        c.setFillColor(BN_BLUE_DARK)
        c.rect(0, 0, w, 1*cm, fill=1, stroke=0)
        c.setFillColor(BN_WHITE)
        c.setFont("Helvetica", 5.5)
        c.drawString(0.3*cm, 0.6*cm, "Education  |  About  |  Press  |  Showrooms  |  Help  |  Returns  |  Track Order  |  Insurance")
        c.drawString(0.3*cm, 0.2*cm, "Email signup  |  Trustpilot reviews  |  Affirm | Klarna | PayPal | Zip | SplitIt  |  Cloudflare CDN")

# ===== Schéma : flow Build-Your-Own-Ring =====
class BYOFlow(Flowable):
    def __init__(self, width=17*cm, height=4*cm):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        steps = [
            ("1  Diamond", "Filtres : shape, carat,\ncut, color, clarity, price\n+ 360° HD viewer"),
            ("2  Setting", "Settings : solitaire, halo,\npavé, three-stone, vintage\nMétaux : platine, or…"),
            ("3  Preview", "Visualisation 3D + render\nbague sur main + prix total\ndynamique"),
            ("4  Complete", "Checkout : CC, Affirm,\nKlarna, PayPal, Zip,\nwire (1.5% off)"),
        ]
        step_w = self.width / 4 - 0.3*cm
        for i, (title, body) in enumerate(steps):
            x = i * (step_w + 0.3*cm)
            c.setFillColor(BN_BLUE)
            c.roundRect(x, 0, step_w, self.height, 6, fill=1, stroke=0)
            c.setFillColor(BN_GOLD)
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x + 0.3*cm, self.height - 0.6*cm, title)
            c.setFillColor(BN_WHITE)
            c.setFont("Helvetica", 7)
            tx = c.beginText(x + 0.3*cm, self.height - 1.2*cm)
            for line in body.split("\n"):
                tx.textLine(line)
            c.drawText(tx)
            if i < 3:
                c.setFillColor(BN_GOLD)
                c.setFont("Helvetica-Bold", 14)
                c.drawCentredString(x + step_w + 0.15*cm, self.height/2 - 0.2*cm, "›")

# ===== Schéma : architecture tech =====
class TechStackDiagram(Flowable):
    def __init__(self, width=17*cm, height=11*cm):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        layers = [
            ("FRONTEND", ["Custom JS framework", "Handlebars (templating)", "D3.js (data viz)",
                          "Segoma 360° HD viewer", "Responsive HTML5/CSS3"]),
            ("APPLICATION", ["R2Net proprietary platform", "Custom diamond search engine",
                             "Build Your Own Ring engine", "Creative Studio (2025)"]),
            ("DATA & MEDIA", ["Amazon S3 (assets/media)", "Diamond inventory feed (R2Net)",
                              "Segoma video CDN", "Brio Animation Studio"]),
            ("EDGE / INFRA", ["Cloudflare CDN + WAF", "DNSSEC", "Cloud-Native migration in progress (Signet)"]),
            ("MARKETING & CRM", ["Emarsys (email, SAP)", "Google Ads + Shopping (PLA)",
                                 "Meta Ads (FB/IG)", "Trustpilot (reviews)"]),
            ("CUSTOMER SERVICE", ["Freshworks Freshdesk (helpdesk)", "Freshchat (live chat)",
                                  "Virtual showroom video calls", "ID.me / UNiDAYS verification"]),
            ("PAIEMENT & ERP", ["Visa/MC/Amex", "PayPal + Pay Later", "Affirm  |  Klarna  |  Zip  |  SplitIt",
                                "Blue Nile Card", "SAP MRO (back-office)"]),
        ]
        y = h
        layer_h = (h - 0.2*cm) / len(layers)
        palette = [BN_BLUE, BN_BLUE_DARK, BN_GOLD, colors.HexColor("#2E5A87"),
                   BN_BLUE, BN_BLUE_DARK, BN_GOLD]
        for i, (title, items) in enumerate(layers):
            y -= layer_h
            c.setFillColor(palette[i])
            c.roundRect(0, y, 4.5*cm, layer_h - 0.1*cm, 4, fill=1, stroke=0)
            c.setFillColor(BN_WHITE)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(0.3*cm, y + layer_h - 0.7*cm, title)
            c.setFont("Helvetica", 7)
            c.drawString(0.3*cm, y + 0.3*cm, "Couche " + str(i+1))

            # boxes for items
            n = len(items)
            box_w = (w - 4.8*cm) / n - 0.15*cm
            for j, it in enumerate(items):
                bx = 4.7*cm + j*(box_w + 0.15*cm)
                c.setFillColor(BN_LIGHT)
                c.setStrokeColor(palette[i])
                c.roundRect(bx, y + 0.1*cm, box_w, layer_h - 0.3*cm, 3, fill=1, stroke=1)
                c.setFillColor(BN_BLUE_DARK)
                c.setFont("Helvetica", 6.8)
                # wrap text manually
                words = it.split(" ")
                line, lines = "", []
                for word in words:
                    if c.stringWidth(line + " " + word, "Helvetica", 6.8) < box_w - 0.2*cm:
                        line = (line + " " + word).strip()
                    else:
                        lines.append(line)
                        line = word
                lines.append(line)
                ty = y + layer_h - 0.5*cm
                for ln in lines:
                    c.drawString(bx + 0.1*cm, ty, ln)
                    ty -= 0.3*cm

# ===== Schéma : 360 diamond viewer =====
class DiamondViewer(Flowable):
    def __init__(self, width=17*cm, height=7*cm):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(BN_LIGHT)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        # 8 frames diamant - rotation
        c.setFillColor(BN_BLUE_DARK)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.3*cm, h - 0.5*cm, "Segoma 360° HD viewer · 40× magnification · ~300 000 diamants natifs")
        frame_w = (w - 0.6*cm) / 8 - 0.1*cm
        for i in range(8):
            x = 0.3*cm + i*(frame_w + 0.1*cm)
            c.setFillColor(BN_WHITE)
            c.setStrokeColor(BN_BLUE)
            c.rect(x, 1*cm, frame_w, h - 2.2*cm, fill=1, stroke=1)
            # mini diamant
            cx = x + frame_w/2
            cy = 1*cm + (h - 2.2*cm)/2
            angle = i * (360/8)
            import math
            rad = math.radians(angle)
            c.setStrokeColor(BN_GOLD)
            c.setLineWidth(0.5)
            r = (h - 2.2*cm) * 0.3
            # diamond shape rotated
            pts = [(0, r), (r*0.7, r*0.3), (r*0.5, -r*0.2), (0, -r),
                   (-r*0.5, -r*0.2), (-r*0.7, r*0.3)]
            rpts = [(cx + p[0]*math.cos(rad) - p[1]*math.sin(rad),
                     cy + p[0]*math.sin(rad) + p[1]*math.cos(rad)) for p in pts]
            p = c.beginPath()
            p.moveTo(*rpts[0])
            for pt in rpts[1:]:
                p.lineTo(*pt)
            p.close()
            c.drawPath(p, stroke=1, fill=0)
            c.setFillColor(BN_GREY)
            c.setFont("Helvetica", 5.5)
            c.drawCentredString(cx, 1.2*cm, f"frame {i+1}")

        # Caption
        c.setFillColor(BN_BLUE)
        c.setFont("Helvetica-Oblique", 7.5)
        c.drawString(0.3*cm, 0.3*cm,
                     "200 frames analysées par diamant · vidéo MP4/HTML5 · scrub manuel + autoplay · zoom 40× (40× SuperZoom sur James Allen)")

# ===== Composition du document =====
def build():
    doc = SimpleDocTemplate(OUT, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=1.6*cm, bottomMargin=1.6*cm,
                            title="Analyse complète Blue Nile",
                            author="Bijou-R Analysis")

    story = []

    # ===== COVER =====
    story.append(Spacer(1, 1.5*cm))
    story.append(P("ANALYSE 360°", ParagraphStyle(
        "preTitle", parent=BODY, fontSize=11, textColor=BN_GOLD,
        fontName="Helvetica-Bold")))
    story.append(P("Blue&nbsp;Nile.com", H_COVER))
    story.append(P("Décryptage complet d'un leader du e-commerce diamantaire", H_COVER_SUB))
    story.append(Spacer(1, 0.4*cm))

    cover_table = Table([
        ["Périmètre", "Site, apps, marketing, technologies, photographie, ads"],
        ["Date d'analyse", "Mai 2026"],
        ["Société analysée", "Blue Nile (filiale Signet Jewelers, ex-R2Net)"],
        ["Cible", "Bijou-R / projet Shopify vs custom"],
        ["Méthode", "Recherche web + sources sectorielles (anti-bot bloque scraping direct)"],
    ], colWidths=(4*cm, 13*cm))
    cover_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (0, -1), BN_WHITE),
        ("BACKGROUND", (1, 0), (1, -1), BN_LIGHT),
        ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 9),
        ("FONT", (1, 0), (1, -1), "Helvetica", 9),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
    ]))
    story.append(cover_table)

    story.append(Spacer(1, 0.8*cm))
    story.append(P("⚑ Note méthodologique", H3))
    story.append(P(
        "Le site bluenile.com bloque l'accès automatisé (anti-bot 403 sur toutes les requêtes serveur). "
        "L'analyse a été reconstituée à partir : (1) sources éditoriales sectorielles (JCK, National Jeweler, "
        "Retail Dive, Rapaport), (2) reviews comparatives (Diamonds.pro, RingSpo, PriceScope, Moissanite by Aurelia), "
        "(3) bases de stack technique (StackShare, RocketReach, 6sense), (4) documents corporate Signet/R2Net, "
        "(5) ads et SEO (Meta Ad Library, SimilarWeb). Les éléments structurels ont été recoupés sur 3 sources minimum.",
        BODY_J))
    story.append(PageBreak())

    # ===== TOC =====
    story.append(P("Sommaire", H1))
    toc = [
        ("1.", "Synthèse exécutive — ce qu'il faut retenir"),
        ("2.", "Identité, société-mère & positionnement stratégique"),
        ("3.", "Architecture & structure du site (page par page)"),
        ("4.", "Maquette homepage reconstituée"),
        ("5.", "Build Your Own Ring & Creative Studio"),
        ("6.", "Photographie produit : 360°, renders 3D, IA — la vérité"),
        ("7.", "Stack technique complète détectée"),
        ("8.", "Applications & services SaaS connectés"),
        ("9.", "Paiements & financement (BNPL)"),
        ("10.", "Programmes marketing, fidélité & promotions"),
        ("11.", "Publicité & acquisition (Meta, Google, TikTok…)"),
        ("12.", "Mobile app, AR, virtual showroom"),
        ("13.", "Logistique, livraison, retours & assurance"),
        ("14.", "Réseaux sociaux, presse & PR"),
        ("15.", "Concurrents & benchmark"),
        ("16.", "Recommandations pour Bijou-R"),
        ("17.", "Sources & références"),
    ]
    t = Table(toc, colWidths=(1*cm, 16*cm))
    t.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), "Helvetica", 10),
        ("TEXTCOLOR", (0, 0), (0, -1), BN_GOLD),
        ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t)
    story.append(PageBreak())

    # ===== 1. SYNTHESE EXEC =====
    story.append(P("1. Synthèse exécutive", H1))
    story.append(P("Ce qu'il faut retenir en 60 secondes", H2))

    exec_rows = [
        ("Société", "Blue Nile · pionnier e-commerce diamant (1999, Seattle)."),
        ("Propriétaire", "Signet Jewelers (NYSE:SIG) depuis août 2022, rachat 360 M$."),
        ("Famille R2Net", "Blue Nile + James Allen + Segoma (imaging) + Brio Animation Studio."),
        ("CA web", "~358 M$ en 2025. Taux de conversion 1,5–2,0 %."),
        ("Plateforme", "Custom-built R2Net en migration cloud-native (Signet). PAS Shopify, PAS SFCC."),
        ("Catégories", "Engagement rings · Wedding rings · Loose diamonds · Fine jewelry · Pearls · Gifts."),
        ("Différentiateurs", "360° HD Segoma 40× sur ~300 K diamants, Build Your Own Ring, Creative Studio (avr-2025), virtual showroom, AR mobile."),
        ("Photos", "Diamants : photos réelles via Segoma (PAS d'IA). Bagues : photo white-bg + render 3D « sur main » (CGI, PAS d'IA générative)."),
        ("Reviews", "Trustpilot externe (~1 500 reviews déclarées) + module reviews on-site."),
        ("Paiement", "CC + Blue Nile Card + PayPal + Affirm + Klarna + Zip + SplitIt + Wire (-1,5 %)."),
        ("Stratégie 2025", "Repositionnement « elevated/curated ». Sortie des grilles massives. Recul du lab-grown (réservé à James Allen)."),
        ("Showrooms", "50+ showrooms physiques (modèle showroom-only, stock = online)."),
    ]
    story.append(kv_table(exec_rows))
    story.append(Spacer(1, 0.4*cm))
    story.append(P("⚐ <b>Verdict clé pour Bijou-R :</b> Blue Nile <b>n'est pas sur Shopify</b>. Ils tournent sur une plateforme propriétaire R2Net (couche métier diamant indispensable) + briques SaaS standards "
                   "(Cloudflare, S3, Emarsys, Freshworks). Pour un projet bijou français, <b>Shopify reste pertinent</b> tant qu'on n'a pas un catalogue diamant à plusieurs centaines de milliers de SKU avec scoring "
                   "et 360° HD propriétaire. La vraie magie Blue Nile, c'est la <b>photographie 360° Segoma</b> et le moteur <b>Build Your Own Ring</b> — pas la plateforme e-commerce elle-même.", QUOTE))

    story.append(PageBreak())

    # ===== 2. IDENTITE =====
    story.append(P("2. Identité, société-mère & positionnement", H1))

    story.append(P("Historique condensé", H2))
    history = [
        "<b>1999</b> – Lancement de Blue Nile à Seattle, pionnier du diamant en ligne.",
        "<b>2004</b> – IPO au Nasdaq.",
        "<b>2017</b> – Signet acquiert R2Net (James Allen) pour 328 M$.",
        "<b>2022</b> – Signet rachète Blue Nile pour 360 M$ (août). Blue Nile rejoint R2Net.",
        "<b>2024–2025</b> – Nouveau CEO Signet J.K. Symancyk, repositionnement « elevated » de Blue Nile.",
        "<b>8 avril 2025</b> – Lancement de <b>Creative Studio</b> (custom ring designer haut de gamme).",
        "<b>2025</b> – Stratégie : sortie progressive du tout-grille, retrait du lab-grown sur Blue Nile (réservé à James Allen).",
    ]
    story.extend(bullets(history))

    story.append(P("Positionnement actuel", H2))
    story.append(P(
        "<b>Avant 2024 :</b> volume + grille massive + lab-grown agressif. "
        "<b>Aujourd'hui :</b> « <i>elevated, curated</i> » — moins de SKU visibles en grille, plus d'édito, plus de Studio/Astor, "
        "plus de showrooms physiques (clicks &amp; bricks). L'objectif affiché par Signet est de franchir le milliard de revenus.",
        BODY_J))

    story.append(P("Marques sœurs dans le groupe Signet", H2))
    siblings = [
        ["Marque", "Positionnement", "Plateforme tech"],
        ["Blue Nile", "Premium digital + showrooms", "R2Net custom"],
        ["James Allen", "Diamond display 40× — volume", "R2Net custom (même plateforme)"],
        ["Kay Jewelers", "Mid-market mall", "Salesforce Commerce Cloud (Demandware)"],
        ["Zales", "Mass-market", "Salesforce Commerce Cloud"],
        ["Jared", "Premium mall", "Salesforce Commerce Cloud"],
        ["Diamonds Direct", "Showroom haut-mid", "Salesforce Commerce Cloud"],
    ]
    t = Table(siblings, colWidths=(3.5*cm, 7*cm, 6.5*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 9),
        ("BACKGROUND", (0, 1), (-1, -1), BN_LIGHT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)

    story.append(PageBreak())

    # ===== 3. STRUCTURE SITE =====
    story.append(P("3. Architecture & structure du site", H1))
    story.append(P("Arborescence majeure (recoupée 3 sources)", H2))

    arbo = [
        ("/", "Homepage — hero rotatif + tuiles catégories + Studio + Astor + édito + reviews."),
        ("/engagement-rings", "Engagement rings (cœur d'activité) — settings, styles, designers, Studio."),
        ("/engagement-rings/design-your-own-ring/settings", "Settings only (parcours BYO étape 2)."),
        ("/engagement-rings/styles", "Browse par style (solitaire, halo, three-stone, vintage…)."),
        ("/engagement-rings/designer/blue-nile-studio", "Blue Nile Studio — collection signature."),
        ("/diamonds", "Diamond Search — moteur principal (filtres avancés + 360° HD)."),
        ("/diamonds/round-cut-diamonds", "Browse par shape (round, princess, oval, cushion, emerald…)."),
        ("/diamonds/astor-ideal-cut-diamonds", "Astor by Blue Nile — cuts premium GCAL/GemEx."),
        ("/diamond-search/lab-grown-diamond-search", "Lab-grown (en retrait stratégique)."),
        ("/build-your-own-ring", "Configurateur — diamant → setting → preview → checkout."),
        ("/jewelry", "Fine Jewelry hub — necklaces, earrings, bracelets, pendants, rings."),
        ("/jewelry/wedding-jewelry", "Wedding jewelry collection."),
        ("/jewelry/pearl-jewelry", "Pearl Jewelry — perles classiques, wedding pearls."),
        ("/jewelry/necklaces", "/bracelets, /earrings — sous-catégories produit."),
        ("/jewelry/todays-jewelry-deals", "Deals du jour."),
        ("/education/diamonds", "Education center diamants (4C, certifications…)."),
        ("/education/diamonds/360-diamond-view", "Page dédiée à la techno 360° HD."),
        ("/education/diamonds/lab-grown-diamonds", "Education lab-grown."),
        ("/education/diamonds/certification/gcal-gemex", "Certifications GCAL & GemEx."),
        ("/education/rings", "Education bagues."),
        ("/education/rings/engagement-ring-guide", "Ultimate Engagement Ring Buying Guide."),
        ("/jewelry-stores", "Locator showrooms physiques."),
        ("/reviews", "Reviews customers (module on-site)."),
        ("/services", "Services : virtual showroom, financing, ring sizing, insurance, upgrade."),
        ("/discounts", "Promotions actives."),
        ("/policies/returns", "Politique de retours (30 jours)."),
        ("/policies/order-and-shipping", "Politique d'expédition (FedEx/UPS, free, signature)."),
        ("/policies/us-payment-methods", "Méthodes de paiement."),
        ("/about-blue-nile/help", "Help center / FAQ."),
        ("/contact-us/faq", "FAQ."),
    ]
    t = Table([["URL", "Rôle"]] + [[u, r] for u, r in arbo], colWidths=(7*cm, 10*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 8),
        ("FONT", (0, 1), (0, -1), "Helvetica-Oblique", 7.5),
        ("FONT", (1, 1), (1, -1), "Helvetica", 7.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
    ]))
    story.append(t)

    story.append(PageBreak())

    # ===== 4. MAQUETTE HOMEPAGE =====
    story.append(P("4. Maquette homepage reconstituée", H1))
    story.append(P("Représentation schématique du blocage observé chez Blue Nile (à partir des descriptions sources)", BODY))
    story.append(Spacer(1, 0.2*cm))
    story.append(HomepageMockup(width=17*cm, height=20*cm))
    story.append(Spacer(1, 0.2*cm))
    story.append(P("Décomposition bloc par bloc", H2))
    blocks = [
        ("Top utility bar (32-40 px)", "Free shipping · 30-day returns · Virtual showroom appointment · Sign In · Cart · Currency selector (40+ devises)."),
        ("Header (logo + search)", "Logo « Blue Nile » centré gauche, barre de recherche centrale, icônes utilisateur/wishlist/panier à droite."),
        ("Mega-menu principal", "ENGAGEMENT · WEDDING · DIAMONDS · JEWELRY · GIFTS · EDUCATION · SHOWROOMS. Survol = mega-menu avec colonnes (shapes, styles, designers, settings)."),
        ("Hero rotatif", "1 grand visuel + headline « Up to X% Off… » + CTA. Carrousel automatique 3-5 slides (anniversary sale, Studio, Creative Studio, new arrivals)."),
        ("Promo strip", "Bandeau secondaire : « Spring Sale – up to 30% off select fine jewelry » + code promo (mode burst).") ,
        ("Tuiles « Shop by Category »", "6 tuiles carrées : Engagement / Wedding / Diamonds / Necklaces / Earrings / Bracelets. Photos lifestyle ou produit blanc."),
        ("Bandeau « Design It »", "Build Your Own Ring + Creative Studio + Diamond Search. 3 colonnes-CTA avec étapes visuelles."),
        ("Editorial : Studio / Astor / Designer", "Section éditorial avec photos lifestyle mode (modèles humains, ambiance), titre « Blue Nile Studio », « Astor by Blue Nile »."),
        ("Reviews / social proof", "Note moyenne + extraits Trustpilot, photos clients UGC ponctuelles."),
        ("Education teasers", "Liens vers ring guides + 4C diamond education + 360 view explainer."),
        ("Email signup", "« Save up to $50 on your first order » — bandeau de capture email."),
        ("Footer dense", "8-10 colonnes : Shop, Education, About, Services, Help, Showrooms, Policies. + paiements + réseaux sociaux + langues/devises + mentions légales."),
    ]
    for title, body in blocks:
        story.append(P(f"<b>· {title}</b> — {body}", BODY_J))

    story.append(PageBreak())

    # ===== 5. BYO + CREATIVE STUDIO =====
    story.append(P("5. Build Your Own Ring & Creative Studio", H1))

    story.append(P("Le configurateur historique « Build Your Own Ring »", H2))
    story.append(P(
        "Parcours en 3 étapes principales (4 si on inclut le checkout). C'est le moteur historique qui a fait la "
        "réputation de Blue Nile depuis ~2002. Sur l'app mobile, il propose 7 catégories + des centaines de styles.",
        BODY_J))
    story.append(Spacer(1, 0.3*cm))
    story.append(BYOFlow(width=17*cm, height=4*cm))
    story.append(Spacer(1, 0.3*cm))

    story.append(P("Filtres du Diamond Search (étape 1)", H3))
    filters = [
        "<b>Shape :</b> Round · Princess · Cushion · Oval · Emerald · Pear · Marquise · Asscher · Radiant · Heart.",
        "<b>Price range :</b> slider $250 → $1 857 300 (lab-grown) ; jusqu'à 7 chiffres en natif.",
        "<b>Carat :</b> slider 0,18 → 20+ ct.",
        "<b>Cut :</b> Astor Ideal · Ideal · Very Good · Good (+ tag GIA / AGS).",
        "<b>Color :</b> D-Z (slider).",
        "<b>Clarity :</b> FL → I2 (slider).",
        "<b>Polish, Symmetry, Fluorescence, Depth, Table, L/W ratio</b> (filtres avancés).",
        "<b>Certificate :</b> GIA · AGS · IGI (lab-grown) · GCAL.",
        "<b>360° HD :</b> case à cocher « show only diamonds with 360° video ».",
    ]
    story.extend(bullets(filters))

    story.append(P("Creative Studio (lancé 8 avril 2025)", H2))
    story.append(P(
        "Surcouche premium au-dessus de BYO. Hands-on customization : mix &amp; match bands + heads + diamants. "
        "Disponible dans les showrooms physiques <i>et</i> en ligne. Positionnement « unmatched personalization in the custom engagement ring space ». "
        "10 étapes guidées d'après le guide visuel Aurelia : shape → band style → head/setting → metal → accent stones → engraving → personal storytelling.",
        BODY_J))

    story.append(P("Astor by Blue Nile (premium cut)", H3))
    story.append(P(
        "Diamants ultra-sélectionnés (proportions optiques, brillance, fire, scintillation). Chaque pierre est gradée GIA "
        "<b>et</b> ré-analysée par GemEx (light performance). Le viewer pousse au-delà du 360° standard : "
        "<b>200 frames par vidéo</b>, analyse du retour de lumière en quantité et taille des reflets colorés. C'est une "
        "<b>vraie image</b> du diamant, pas un render.",
        BODY_J))

    story.append(PageBreak())

    # ===== 6. PHOTOGRAPHIE =====
    story.append(P("6. Photographie produit : 360°, renders 3D, IA — la vérité", H1))
    story.append(Spacer(1, 0.2*cm))
    story.append(DiamondViewer(width=17*cm, height=7*cm))
    story.append(Spacer(1, 0.3*cm))

    story.append(P("Trois catégories d'images distinctes", H2))

    photo_cards = [
        ("A. Diamants individuels (loose)",
         "Photographies <b>réelles</b> via la technologie propriétaire <b>Segoma</b> (filiale R2Net). "
         "Chaque diamant est passé au scanner 360° qui prend la <b>vraie pierre vendue</b> à 40× de magnification. "
         "Vidéo composée de 200 frames. Format de diffusion : vidéo type sprite + lecteur HTML5 avec scrub + zoom. "
         "<b>~300 000 diamants natifs</b> ont une vidéo Segoma. 100% des lab-grown (~18 000) en avaient avant le repositionnement. "
         "<b>Ce ne sont PAS des images IA.</b> Ce sont des scans optiques industriels du diamant réel — d'où la valeur perçue."),
        ("B. Bagues (settings) sur fond blanc",
         "Photographie studio classique sur fond blanc, multi-angles (3 à 6 vues par bague). "
         "Production en interne (rôle <b>Studio Producer</b> Blue Nile chargé de l'intake, scheduling, "
         "responsabilité au SKU près du studio à l'upload). <b>Photo réelle</b> du produit. Pas d'IA."),
        ("C. Bagues sur main",
         "Vue clé du PDP. Sources comparatives : « Blue Nile showcases their rings on <b>realistic renders of hands</b>, "
         "with on-hand shots that are detailed and lifelike ». "
         "→ C'est du <b>render 3D / CGI</b>, pas une photo réelle de modèle, pas une IA générative. "
         "Le modèle 3D de la bague est appliqué sur un mesh de main standardisé, ce qui permet d'avoir un "
         "rendu cohérent sur tout le catalogue sans devoir refaire une séance photo par SKU."),
        ("D. Lifestyle / éditorial",
         "Photos de modèles humains, ambiances, mises en scène mariage. Production agence externe + équipe créative interne. "
         "Utilisé pour les pages hero, Studio, Astor, campagnes Anniversary/Black Friday. Photo réelle de mannequins."),
        ("E. Vidéos collection / brand",
         "Vidéos courtes (Stories/Reels) + films campagne longs. Production via Brio Animation Studio (R2Net) pour l'animation/3D, "
         "+ shootings mode externes pour le brand content."),
    ]
    for title, body in photo_cards:
        story.append(section_card(title, [P(body, BODY_J)]))
        story.append(Spacer(1, 0.15*cm))

    story.append(P("Le carrousel produit + rotation", H2))
    rotation_facts = [
        "Sur un PDP bague : 4-6 thumbnails verticales (white-bg main + détail + on-hand render + close-up + métal).",
        "Hover sur la grille catégorie : substitution image principale → image alternative (souvent on-hand render).",
        "Sur un PDP diamant : le viewer 360° est <b>autoplay loop</b> + contrôles play/pause/frame-by-frame + zoom.",
        "Sur les <i>fancy shapes</i> (oval, pear, cushion), la rotation 360° est essentielle pour vérifier le « bow-tie effect ».",
        "Frame-by-frame : navigation au scroll horizontal de souris ou drag-touch sur mobile.",
    ]
    story.extend(bullets(rotation_facts))

    story.append(PageBreak())

    # ===== 7. STACK TECH =====
    story.append(P("7. Stack technique complète détectée", H1))
    story.append(P(
        "Reconstitution recoupée via 6sense, RocketReach, StackShare, indices DNS publics et patterns observés. "
        "Précision : Blue Nile <b>n'utilise PAS Shopify, PAS Magento/Adobe Commerce, PAS Salesforce Commerce Cloud</b>. "
        "Ils tournent sur la plateforme propriétaire R2Net (héritée du rachat 2017), couplée à des briques SaaS.",
        BODY_J))
    story.append(Spacer(1, 0.2*cm))
    story.append(TechStackDiagram(width=17*cm, height=11*cm))
    story.append(Spacer(1, 0.3*cm))

    story.append(P("Détail par catégorie", H2))
    tech_rows = [
        ("Plateforme e-commerce", "R2Net (custom, propriétaire). Migration cloud-native en cours sous Signet."),
        ("Templating front", "Handlebars détecté côté client."),
        ("Data viz", "D3.js (probable pour les graphes diamond pricing/comparaison)."),
        ("CDN / Edge", "Cloudflare (avec WAF/anti-bot, ce qui explique nos 403)."),
        ("DNS", "DNSSEC activé."),
        ("Stockage médias", "Amazon S3 (assets ecommerce, images 360° Segoma)."),
        ("Viewer 360° diamants", "Segoma (R2Net, propriétaire). 40× magnification, 200 frames/diamant."),
        ("3D/CGI bague", "Renders 3D internes + Brio Animation Studio (R2Net)."),
        ("Search/merchandising", "Custom (catalogue diamant nécessite scoring spécifique). Algolia/Coveo non confirmé."),
        ("Helpdesk", "Freshworks Freshdesk (tickets) + Freshchat (live chat in-page)."),
        ("Email marketing / CRM", "Emarsys (SAP) — automation, segmentation, lifecycle."),
        ("Analytics web", "Google Analytics 4 + Google Tag Manager (standard retail US)."),
        ("A/B testing", "Non confirmé — probable Adobe Target ou Optimizely vu l'échelle."),
        ("Reviews", "Trustpilot (1 500+ reviews déclarées) + module on-site."),
        ("Auth verification", "ID.me (military/first responders), UNiDAYS (étudiants/profs)."),
        ("Paiement", "Visa/MC/Amex (acquéreur non public), Blue Nile Card propriétaire, PayPal, Affirm, Klarna, Zip, SplitIt."),
        ("BO/ERP", "SAP MRO module (back-office maintenance/ops)."),
        ("Blog", "WordPress (sous-domaine bluenile-blog.r2net.com — Cut & Polish blog)."),
        ("Mobile app", "iOS + Android natif, AR (Dream Box) via SceneKit/ARKit (iOS) + ARCore (Android)."),
        ("Sécurité", "DNSSEC + Cloudflare WAF + bot management strict (testé)."),
        ("Cookie consent", "Banner CCPA/GDPR — solution non publiquement identifiée (probable OneTrust ou Cookiebot, standard enterprise)."),
    ]
    story.append(kv_table(tech_rows))

    story.append(PageBreak())

    # ===== 8. APPLICATIONS SAAS =====
    story.append(P("8. Applications & services SaaS connectés", H1))
    story.append(P("Récap des 20+ briques tierces utilisées sur ou autour de bluenile.com", H2))

    apps_data = [
        ["Catégorie", "Outil / fournisseur", "Usage"],
        ["CDN & sécurité", "Cloudflare", "Edge, WAF, anti-bot (le 403 qu'on a hit)"],
        ["DNS", "DNSSEC", "Sécurisation DNS"],
        ["Stockage", "Amazon S3", "Médias, vidéos 360°, assets"],
        ["Imaging 360°", "Segoma (R2Net)", "Scan optique diamants 40×"],
        ["Animation 3D", "Brio Animation Studio (R2Net)", "Renders bagues + vidéos brand"],
        ["Templating", "Handlebars", "Rendu front"],
        ["Charts", "D3.js", "Data visualization"],
        ["Helpdesk", "Freshworks Freshdesk", "Tickets support"],
        ["Live chat", "Freshchat", "Chat in-page"],
        ["Email marketing", "Emarsys (SAP)", "Newsletters, lifecycle, segmentation"],
        ["ERP / BO", "SAP MRO", "Back-office, maintenance"],
        ["Reviews", "Trustpilot", "Reviews externes (1 500+)"],
        ["Verification", "ID.me", "Vérif militaires / first responders → 15%"],
        ["Verification", "UNiDAYS", "Vérif étudiants/profs → 15%"],
        ["Paiement carte", "Visa / Mastercard / Amex", "Cartes bancaires standard"],
        ["Paiement", "PayPal", "Standard + Pay Later"],
        ["BNPL", "Affirm", "Financement étalé"],
        ["BNPL", "Klarna", "Split / financement"],
        ["BNPL", "Zip", "Split en 4"],
        ["BNPL", "SplitIt", "Étalement sans intérêt"],
        ["Carte propriétaire", "Blue Nile Credit Card", "Carte de crédit maison"],
        ["Wire transfer", "Wire bank", "1,5% off pour orders > 1 000 $"],
        ["Livraison", "FedEx / UPS", "Free shipping insured + signature"],
        ["Assurance transit", "BN/transporteur", "Assuré jusqu'à livraison"],
        ["Analytics", "Google Analytics 4 + GTM", "Standard ecommerce (probable)"],
        ["Ads", "Google Ads (Search + Shopping)", "PLA + brand keywords"],
        ["Ads", "Meta Business (FB + IG)", "Visual storytelling, retargeting"],
        ["Ads", "Pinterest Ads", "Pertinent jewelry, inspirations mariage (probable)"],
        ["Ads", "TikTok Ads", "Engagement Gen Z (probable, à confirmer)"],
        ["CMS blog", "WordPress", "bluenile-blog.r2net.com"],
        ["Mobile AR", "ARKit (iOS) + ARCore (Android)", "Dream Box virtual try-on"],
        ["Showroom video", "Probable Zoom/WebRTC custom", "Virtual showroom 1-on-1"],
    ]
    t = Table(apps_data, colWidths=(3.5*cm, 5*cm, 8.5*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 8.5),
        ("FONT", (1, 1), (1, -1), "Helvetica-Bold", 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.15, colors.lightgrey),
    ]))
    story.append(t)

    story.append(PageBreak())

    # ===== 9. PAIEMENTS =====
    story.append(P("9. Paiements & financement", H1))
    pay_rows = [
        ("Carte bancaire", "Visa, Mastercard, American Express, Discover."),
        ("Carte maison", "Blue Nile Credit Card (propriétaire, options de paiement étalé internes)."),
        ("PayPal", "Paiement standard + PayPal Pay Later."),
        ("Affirm", "BNPL — financement étalé multi-mois, soft credit check."),
        ("Klarna", "Split en 4 ou financement long."),
        ("Zip (ex-Quadpay)", "Split en 4 paiements sans intérêt."),
        ("SplitIt", "Étalement sur la carte existante, sans nouveau crédit."),
        ("Wire transfer", "Virement bancaire — donne un <b>discount de 1,5%</b> sur orders ≥ 1 000 $."),
        ("PAS pris en charge", "Afterpay, Shop Pay, Apple Pay/Google Pay (non confirmés activement)."),
    ]
    story.append(kv_table(pay_rows))

    story.append(P("Logique business derrière le mix BNPL", H3))
    story.append(P(
        "Sur une bague de fiançailles à 5 000–15 000 $, le BNPL est <b>critique</b> pour la conversion. "
        "Blue Nile maximise les options pour ne perdre aucune segmentation client : Affirm (long terme, soft check), "
        "Klarna (split 4), Zip (impulse split), SplitIt (sans 2e crédit). Le wire à -1,5% capte les budgets élevés "
        "qui veulent économiser. C'est un mix <b>très américain</b> ; en France/Europe, l'équivalent serait : "
        "Alma, Klarna EU, Younited Pay, Floa, Cofidis 3xCB.",
        BODY_J))

    story.append(PageBreak())

    # ===== 10. MARKETING =====
    story.append(P("10. Programmes marketing, fidélité & promotions", H1))

    story.append(P("Calendrier promotionnel", H2))
    promos = [
        ("<b>Anniversary Sale</b> (mi-août → mi-septembre)", "Up to 40% off select jewelry + 25% off ring settings."),
        ("<b>Black Friday / Cyber Monday</b> (fin novembre)", "Up to 50% off select jewelry items."),
        ("<b>Spring Sale</b>", "Up to 30% off select fine jewelry."),
        ("<b>Limited-time bursts</b>", "Promotions courte durée avec code à entrer au checkout (pas de sitewide permanent)."),
        ("<b>First-order discount</b>", "Up to 50 $ off à l'inscription newsletter."),
        ("<b>Student/teacher</b>", "15 % via UNiDAYS."),
        ("<b>Military / vétérans / first responders / médical</b>", "15 % via ID.me (sur engagement + wedding bands)."),
        ("<b>Wire transfer</b>", "-1,5 % automatique sur orders ≥ 1 000 $."),
    ]
    for title, body in promos:
        story.append(P(f"<b>· {title}</b> — {body}", BODY_J))

    story.append(P("Programmes loyalty & rétention", H2))
    loyalty = [
        "Diamond Upgrade Program — possibilité de revenir échanger sa pierre pour une plus grosse plus tard.",
        "Lifetime warranty sur la fabrication (cleaning, polishing, prong tightening).",
        "Free ring resizing dans la première année.",
        "Newsletter avec offres exclusives + early access ventes.",
        "Mobile app — push notifications + features exclusives (AR, virtual showroom).",
    ]
    story.extend(bullets(loyalty))

    story.append(P("Stratégie de contenu / SEO", H2))
    seo = [
        "Education Center massif : 4C, certifications GCAL/GemEx, lab-grown vs natif, ring guides…",
        "Blog Cut &amp; Polish (WordPress sur sous-domaine R2Net) — content marketing recurring.",
        "Pages buying guides ultra-longues, structurées pour ranker sur les recherches haute-intention.",
        "Pages produit avec descriptions denses + reviews + Q&amp;A.",
        "Backlinks via PR jewelry (JCK, National Jeweler, Rapaport) et lifestyle (Vogue, WWD).",
    ]
    story.extend(bullets(seo))

    story.append(PageBreak())

    # ===== 11. ADS =====
    story.append(P("11. Publicité & acquisition", H1))

    story.append(P("Plateformes ads identifiées / probables", H2))
    ads_data = [
        ["Plateforme", "Activité", "Notes"],
        ["Google Search Ads", "🟢 Très active", "Brand + non-brand. Bid agressif sur « engagement ring », « loose diamonds »."],
        ["Google Shopping (PLA)", "🟢 Très active", "Feed produit complet — natural diamond, ring settings, jewelry. Conversion 8,3 % avg."],
        ["Google YouTube Ads", "🟢 Actif", "Pre-roll lifestyle + tutoriels how-to-choose-a-diamond."],
        ["Google Demand Gen", "🟡 Probable", "Standard pour catalogue retail luxe."],
        ["Meta Facebook Ads", "🟢 Très active", "Conv. 4-6 %. Storytelling, lifestyle, retargeting, lead-gen (free $5K diamond contest)."],
        ["Meta Instagram Ads", "🟢 Très active", "Stories, Reels, feed. Catalogue dynamique (DPA)."],
        ["Meta Advantage+", "🟢 Active", "Audience automation pour ROAS."],
        ["TikTok Ads", "🟡 Probable", "Gen Z fiançailles, before/after, ring reveals."],
        ["Pinterest Ads", "🟢 Pertinent", "Wedding boards, ring inspiration — audience hyper-qualifiée."],
        ["Snapchat", "🟡 Possible", "Snap AR try-on est un canal naturel pour la bijouterie."],
        ["LinkedIn", "🔴 Improbable", "Non pertinent B2C."],
        ["X (Twitter)", "🟡 Faible", "Possible PR/brand uniquement."],
        ["Affiliate", "🟢 Très active", "Couponcabin, Groupon, Picodi, Simplycodes, Marieclaire coupons listées."],
        ["Influence marketing", "🟢 Active", "Engagement ring reveals, mariage influenceurs."],
    ]
    t = Table(ads_data, colWidths=(4*cm, 3*cm, 10*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 8.5),
        ("FONT", (0, 1), (0, -1), "Helvetica-Bold", 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.15, colors.lightgrey),
    ]))
    story.append(t)

    story.append(P("Comment voir leurs ads (méthode reproductible)", H3))
    ads_methods = [
        "<b>Meta Ad Library</b> — facebook.com/ads/library → rechercher « Blue Nile » → filtrer All ads → United States. "
        "Depuis 2026 on voit aussi les impression buckets et le spend cumulé 12 mois sur la page advertiser.",
        "<b>Google Ads Transparency Center</b> — adstransparency.google.com → rechercher « Blue Nile » → voir tous les visuels Search + Shopping + YouTube.",
        "<b>TikTok Creative Center</b> → Top Ads → filtrer industrie Jewelry, region US, marque Blue Nile.",
        "<b>SimilarWeb</b> — répartition organique vs paid vs direct vs social vs email.",
        "<b>SEMrush / Ahrefs</b> — répartition par mots-clés paid et concurrence brand.",
    ]
    story.extend(bullets(ads_methods))

    story.append(P("Types de créa observés (extraits sectoriels)", H3))
    creas = [
        "Free $5 000 diamond giveaway (email capture).",
        "« Tell your love story » — UGC engagement ring reveals.",
        "Carrousels catalog DPA — settings + price + CTA shop.",
        "Vidéos AR try-on demo (app mobile).",
        "Comparateur « natural vs lab-grown » (avant le repositionnement 2025).",
        "Lifestyle wedding (couples, ambiances cinema).",
        "Astor by Blue Nile : focus brilliance/fire (motion close-up).",
    ]
    story.extend(bullets(creas))

    story.append(PageBreak())

    # ===== 12. MOBILE & AR =====
    story.append(P("12. Mobile app, AR & virtual showroom", H1))

    story.append(P("L'app Blue Nile", H2))
    app_facts = [
        "Disponible <b>iOS</b> (App Store) et <b>Android</b> (Google Play).",
        "AR « <b>Dream Box</b> » — visualisation augmentée sur la main : photo de la main + render 3D de la bague choisie.",
        "Build Your Own Ring complet : 7 catégories, centaines de styles, customisation in-app.",
        "Diamond search interactif sur <b>150 000+ diamants certifiés</b>.",
        "Conversion : Blue Nile rapporte que les utilisateurs AR sont <b>+50 % more likely</b> à finaliser un achat.",
        "Multi-devises : 40+ pays / devises supportés.",
        "Partage social du visuel AR : Facebook, X, SMS, email.",
    ]
    story.extend(bullets(app_facts))

    story.append(P("Virtual Showroom (rendez-vous expert)", H2))
    story.append(P(
        "Blue Nile propose un rendez-vous visio 1-on-1 avec un personal jeweler. L'expérience est décrite comme « very similar to interactions with sales experts in a brick-and-mortar store ». "
        "Cela complète parfaitement le réseau de showrooms physiques : le client choisit en ligne, fixe un rdv visio si besoin, OU vient en showroom essayer des replicas, ET commande en ligne pour livraison.",
        BODY_J))

    story.append(P("Showrooms physiques (clicks &amp; bricks)", H2))
    story.append(P(
        "Modèle « <b>showroom-only</b> » : pas de stock vendable sur place. Les visiteurs essaient des <b>répliques</b>, discutent avec un conseiller, "
        "puis la commande passe via l'inventaire online avec livraison. Plan d'ouverture : 50 nouveaux showrooms sur les top 50 metros US.",
        BODY_J))
    showrooms = [
        "Los Angeles, CA (10250 Santa Monica Blvd)",
        "Santa Clara, CA (Westfield Valley Fair)",
        "King of Prussia, PA",
        "Garden City, NY (Roosevelt Field – Simon)",
        "Salem, NH (Mall at Rockingham Park – Simon)",
        "+ Colorado, Illinois, Pennsylvanie (expansion en cours)",
    ]
    story.extend(bullets(showrooms))

    story.append(PageBreak())

    # ===== 13. LOGISTIQUE =====
    story.append(P("13. Logistique, livraison, retours, assurance", H1))
    logi_rows = [
        ("Transporteurs", "FedEx et UPS."),
        ("Livraison standard", "<b>Free secure shipping</b> sur toute commande US."),
        ("Livraison rapide", "Overnight gratuit sur orders ≥ 500 $."),
        ("Signature", "Requise à la livraison (anti-fraude diamants)."),
        ("Assurance", "Insurée porte-à-porte de leur facility jusqu'au client."),
        ("Retour", "30 jours <b>no questions asked</b>."),
        ("Retours gratuits", "2 retours gratuits/client/an. Au-delà : 30 $ par retour (label inclus, insuré)."),
        ("Non-returnable", "Pieces personnalisées, engraved, resized post-achat, Diamond Upgrade, Clearance, Final Sale."),
        ("Traitement retour", "5–15 jours ouvrés après réception."),
        ("Ring resizing", "Gratuit la première année."),
        ("Diamond Upgrade", "Échange pour un diamant ≥ 2× la valeur du diamant initial."),
        ("Lifetime warranty", "Cleaning, polishing, prong tightening offerts à vie."),
    ]
    story.append(kv_table(logi_rows))

    story.append(PageBreak())

    # ===== 14. SOCIAL =====
    story.append(P("14. Réseaux sociaux, presse & PR", H1))
    social_rows = [
        ("Facebook", "facebook.com/bluenile — page principale, audiences acquisition + community management."),
        ("Instagram", "@bluenile — feed shoppable, Stories/Reels, collaborations influenceurs mariage."),
        ("Pinterest", "Profil actif — boards ring inspiration, wedding, gemstones."),
        ("TikTok", "Présence active (ring reveals, behind-the-scenes Studio)."),
        ("YouTube", "Chaîne brand — diamond education tutoriels, Astor performance, Studio showcases."),
        ("X (Twitter)", "Service client + PR essentiellement."),
        ("LinkedIn", "Recrutement + corporate (sous Signet)."),
        ("Pressroom / PR", "Couverture régulière JCK, National Jeweler, Rapaport, Retail Dive, WWD, Vogue, BuiltInSeattle."),
    ]
    story.append(kv_table(social_rows))

    story.append(PageBreak())

    # ===== 15. CONCURRENTS =====
    story.append(P("15. Concurrents & benchmark", H1))
    comp_data = [
        ["Concurrent", "Position vs Blue Nile", "Plateforme tech"],
        ["James Allen", "Frère jumeau (même R2Net). 360° 40× identique.", "R2Net custom (idem)"],
        ["Brilliant Earth", "Éthique + lab-grown + showrooms. Premium éco-conscient.", "Custom + Shopify hybride (suspecté)"],
        ["With Clarity", "Custom rings + service-led.", "Custom"],
        ["Whiteflash", "Hyper-premium, A CUT ABOVE® super-ideal.", "Custom"],
        ["Tiffany & Co.", "Luxe traditionnel. Cher.", "Salesforce Commerce Cloud (LVMH)"],
        ["Mejuri", "Fine jewelry abordable DTC, social-first.", "Shopify Plus"],
        ["Catbird", "Indie premium NY.", "Shopify Plus"],
        ["Bario Neal", "Éthique, custom, showroom.", "Shopify"],
        ["Kay / Zales / Jared", "Mall mid-market (cousins Signet).", "Salesforce Commerce Cloud"],
        ["VRAI", "Lab-grown direct-to-consumer.", "Shopify Plus"],
        ["Lightbox (De Beers)", "Lab-grown $800/ct (partenaire BN historique).", "Shopify"],
    ]
    t = Table(comp_data, colWidths=(4*cm, 7.5*cm, 5.5*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("FONT", (0, 1), (0, -1), "Helvetica-Bold", 9),
        ("FONT", (1, 1), (-1, -1), "Helvetica", 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
    ]))
    story.append(t)
    story.append(P("⚐ <b>Insight clé :</b> sur le segment <b>jewelry DTC moderne</b> (Mejuri, VRAI, Catbird, Bario Neal), la quasi-totalité tourne sur <b>Shopify / Shopify Plus</b>. Le custom-built à la Blue Nile/James Allen est réservé aux catalogues diamant à plusieurs centaines de milliers de SKU. Pour Bijou-R, à moins de viser le marché diamant nu en volume, <b>Shopify reste l'option rationnelle</b>.", QUOTE))

    story.append(PageBreak())

    # ===== 16. RECO BIJOU-R =====
    story.append(P("16. Recommandations pour Bijou-R", H1))

    story.append(P("Shopify : oui ou non ?", H2))
    story.append(P(
        "Sur la base de ce que fait Blue Nile, <b>Shopify Plus reste le bon choix pour Bijou-R</b> "
        "à moins de viser explicitement le marché du diamant nu à très haute volumétrie. "
        "Blue Nile a besoin de R2Net parce qu'ils gèrent 300 000+ SKU diamants avec scoring 4C, intégration GIA/IGI, "
        "feed direct fournisseurs et un viewer 360° propriétaire qui leur coûte des millions à exploiter. "
        "Si Bijou-R fait des bagues, colliers, boucles avec un catalogue de quelques centaines à quelques milliers de SKU, "
        "Shopify Plus + bonnes apps couvre <b>tout</b> ce qu'on voit chez Blue Nile <i>sauf</i> le 360° Segoma.",
        BODY_J))

    story.append(P("Briques à reproduire (et leurs équivalents Shopify)", H2))
    repro = [
        ["Blue Nile", "Équivalent Shopify-friendly"],
        ["Build Your Own Ring (3 steps)", "Apps : Tangiblee, Inkybay, Customily, Productify (jewelry configurator)"],
        ["360° HD diamond viewer", "Magic 360, Sirv 360, Spinify — ou production maison via vidéo MP4 + lecteur custom"],
        ["Render 3D bague-sur-main", "Outsourcer chez agence CGI bijou (lyon/paris/india) — réutilisable sur tout le catalogue"],
        ["Virtual showroom (visio)", "Boxout.io, Hero, Bambuser Live (intégrations Shopify Plus)"],
        ["AR try-on", "Tangiblee, Shopify AR (modèle 3D GLB), Snap AR Lens kit"],
        ["BNPL multi", "Alma, Klarna, PayPal Pay in 4, Younited Pay — apps natives Shopify"],
        ["Reviews", "Judge.me, Yotpo, Loox, Stamped — natifs Shopify"],
        ["Email lifecycle", "Klaviyo (équivalent EU à Emarsys pour DTC)"],
        ["Wishlist + comparateur", "Smart Wishlist, Wishlist Plus"],
        ["Studio/curated editorial", "Shopify Sections + Online Store 2.0 + GemPages/PageFly"],
        ["Loyalty + diamond upgrade", "Smile.io, LoyaltyLion — programmes maison adaptables"],
        ["Education center", "Shopify Pages + bonne IA-SEO + JSON-LD"],
        ["Cookie consent EU", "OneTrust Shopify, Cookiebot, Iubenda (RGPD requis pour FR)"],
        ["Live chat", "Tidio, Gorgias, Crisp, Re:amaze"],
        ["Helpdesk", "Gorgias, Zendesk, Re:amaze"],
    ]
    t = Table(repro, colWidths=(7*cm, 10*cm))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BN_BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), BN_WHITE),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("FONT", (0, 1), (0, -1), "Helvetica-Bold", 9),
        ("FONT", (1, 1), (1, -1), "Helvetica", 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BN_LIGHT, BN_BLUE_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX", (0, 0), (-1, -1), 0.4, BN_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
    ]))
    story.append(t)

    story.append(P("Quick wins prioritaires", H2))
    quick = [
        "<b>Photo produit cohérente</b> — investir dès le départ dans un kit photo studio + une chaîne CGI pour les renders « sur main ». C'est le gros différenciateur visuel.",
        "<b>360° produit</b> — même approche bas-de-gamme pour démarrer : vidéo MP4 + lecteur Magic360. Pas besoin de Segoma tant qu'on ne vend pas du diamant nu.",
        "<b>Configurateur basic</b> — un BYO 3-steps Shopify suffit pour 90% de l'effet wow.",
        "<b>Trust signals visibles</b> — reviews on-page + Trustpilot widget + paiement BNPL bien affichés.",
        "<b>Education content</b> — un mini-hub éducation (matériaux, certifications, taille de doigt, entretien) gonfle le SEO et la conversion.",
        "<b>Email lifecycle</b> — flow Klaviyo : welcome, abandon panier, post-achat care, anniversary, win-back. Standard ROI 25-30 % du CA pour la bijouterie DTC.",
        "<b>RGPD/Cookie</b> — bien fait dès le jour 1, Cookiebot ou Iubenda intégré.",
        "<b>Virtual try-on</b> — phase 2, via Tangiblee ou Snap AR.",
    ]
    story.extend(bullets(quick))

    story.append(P("Estimation budgétaire approximative", H2))
    story.append(P(
        "Pour cloner ~80 % de l'expérience Blue Nile sur Shopify Plus, un budget réaliste se situe entre <b>25 K€ et 80 K€</b> "
        "selon le niveau de finition CGI + configurateur. Le mensuel d'apps + Shopify Plus tourne autour de <b>2 500–4 500 €/mois</b>. "
        "C'est sans commune mesure avec une plateforme custom type R2Net (millions à plusieurs millions d'investissement + équipe IT dédiée).",
        BODY_J))

    story.append(PageBreak())

    # ===== 17. SOURCES =====
    story.append(P("17. Sources & références", H1))
    sources = [
        "Blue Nile — bluenile.com (homepage, education center, policies). Note : accès direct bloqué par anti-bot Cloudflare lors de cette analyse.",
        "JCK Online — articles « Blue Nile Shifts Away From Lab-Growns and Grids » (2024-2025), « Blue Nile Believes It Can Break A Billion Bucks ».",
        "National Jeweler — couverture rachat Signet/Blue Nile (2022) et stratégie showroom.",
        "Retail Dive — « Signet buys Blue Nile for $360M ».",
        "Rapaport — « Blue Nile to Open 50 New Showrooms ».",
        "Diamonds.pro — review approfondie Blue Nile (UI/UX, photos).",
        "RingSpo — Blue Nile Engagement Rings Review.",
        "PriceScope — analyses techniques diamants Blue Nile.",
        "Moissanite by Aurelia — guide visuel Creative Studio (10 étapes) et Astor by Blue Nile.",
        "Haute Living — « Blue Nile's New Creative Studio » (juillet 2025).",
        "WWD — Blue Nile Engagement Ring Guide.",
        "R2Net.com — pages corporate Segoma, Brio Animation, Virtual Vault.",
        "Sarine.com — Sarine Loupe technology (concurrent imaging).",
        "Apptopia — Blue Nile app data iOS.",
        "BuiltWith / Wappalyzer / 6sense / RocketReach / StackShare — tech stack profiles (bloqué WebFetch, info croisée via WebSearch).",
        "SimilarWeb — bluenile.com Traffic Analytics.",
        "Trustpilot — bluenile.com reviews page.",
        "SEC filings — Signet Jewelers Form 8-K (acquisition R2Net 2017, Blue Nile 2022).",
        "Meta Ad Library, Google Ads Transparency Center, TikTok Creative Center — bases d'ads publiques.",
        "ECDB / Grips Intelligence — revenue Blue Nile 2025 (358 M$).",
        "GlobeNewswire / PRNewswire — communiqués R2Net + Segmoa.",
        "Coupon sites (CouponCabin, Groupon, Picodi, Simplycodes, Marieclaire, Savings, Vouchercloud) — promo calendar.",
        "GeekWire / Built In Seattle — couverture corporate Blue Nile.",
    ]
    story.extend(bullets(sources, SMALL))

    story.append(Spacer(1, 0.5*cm))
    story.append(P(
        "Rapport généré automatiquement à partir d'une recherche multi-sources croisée. Compte tenu du blocage anti-bot de bluenile.com, "
        "les éléments visuels (mockup, viewer 360°, flow BYO) sont des <b>reconstitutions schématiques</b> et non des captures d'écran réelles. "
        "Recommandation : compléter par 3-5 captures manuelles du site (navigation incognito) pour valider visuellement chaque section.",
        SMALL))

    # ===== Page numbers / footer =====
    def on_page(canv, doc_):
        canv.saveState()
        canv.setStrokeColor(BN_BLUE)
        canv.setLineWidth(0.4)
        canv.line(2*cm, 1.2*cm, 19*cm, 1.2*cm)
        canv.setFont("Helvetica", 8)
        canv.setFillColor(BN_GREY)
        canv.drawString(2*cm, 0.7*cm, "Analyse bluenile.com — Mai 2026 — Bijou-R")
        canv.drawRightString(19*cm, 0.7*cm, f"page {doc_.page}")
        # Header band
        canv.setFillColor(BN_BLUE_DARK)
        canv.rect(0, 28.7*cm, 21*cm, 0.4*cm, fill=1, stroke=0)
        canv.setFillColor(BN_GOLD)
        canv.rect(0, 28.65*cm, 21*cm, 0.05*cm, fill=1, stroke=0)
        canv.restoreState()

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"OK: {OUT}")

if __name__ == "__main__":
    build()
