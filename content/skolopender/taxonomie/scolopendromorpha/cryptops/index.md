---
title: Cryptops
description: Gattung Cryptops
bookHidden: true
type: page
layout: taxonomy_genus
datadir: cryptops
---

# Die Gattung: Cryptops
{{<disclaimer/taxonomy-genus>}}

Laut Edgecombe & Bonato (2011) und Lewis (2016) umfasst die Gattung **Cryptops** vier Unterarten: **Cryptops** (Cryptops), **Trigonocryptops** (Verhoeff, 1906), **Haplocryptops** (Verhoeff, 1934) und **Chromatanops** (Verhoeff, 1906). Allerdings wird letzteres als Synonym von **Cryptops** (Cryptops) betrachtet.

**Cryptops** wird als Gattung und nominelles Unterart in verschiedenen Studien behandelt. Die Unterart **Trichocryptops** wurde von Lewis (2016) zu **Cryptops** (Cryptops) synonymisiert. 

**Chromatanops** wird als Unterart in verschiedenen Studien behandelt. Sowohl Chagas-Jr et al. (2014) als auch Bonato et al. (2016) betrachteten **Chromatanops bivittatus** (die einzige Art von Chromatanops) als Mitglied von Cryptops, gleichzeitig schlossen Bonato et al. (2016) **Chromatanops** als Unterart von Cryptops ein. Es gibt keine zuverlässigen diagnostischen Merkmale, um **Chromatanops** als Unterart zu bestätigen, daher wird **Cryptops (Chromatanops)** jüngeres Synonym von Cryptops betrachtet und **Cryptops (Chromatanops) bivittatus** (Pocock, 1893) sollte **Cryptops (Cryptops) bivittatus** _stat. nov._ sein.

**Trigonocryptops** wird als Unterart in verschiedenen Studien behandelt. Cryptops (**Paratrigonocryptops**) wurde von Lewis (2005) zu Cryptops (**Trigonocryptops**) synonymisiert.

**Haplocryptops** wird als Unterart in verschiedenen Studien behandelt. Es gibt keine zuverlässigen diagnostischen Merkmale, um **Haplocryptops** als Unterart zu bestätigen, daher wird die Gültigkeit des letzteren in Frage gestellt. Schileyko et al. (2020) behalten den Unterartenstatus bis zur vollständigen Klärung jedoch bei.

Basierend auf sowohl molekularen als auch morphologischen Ergebnissen schrieben Vahtera et al. (2012), dass **Paracryptops** "innerhalb von Cryptops verschachtelt" ist, ohne den neuen taxonomischen Status des letzteren zu formalisieren. Unter Berücksichtigung der eindeutigen Ergebnisse, die von Vahtera et al. (2012) erhalten wurden, schlagen Schileyko et al. (2020) vor, dass diese Taxon eine Unterart von **Cryptops** sein sollte.

{{<mermaid>}}
    flowchart LR
        scolopendromorpha["`Ordnung
                            **Scolopendromorpha**`"]
        cryptopidae["`Familie
                    **Cryptopidae**`"]
            cryptops["`Gattung
                    **Cryptops**`"]
            trichocryptops["`Synonym:
                        **Trichocryptops**`"]
            chromatanops["`Synonym 
                        **Chromatanops**`"]
                trigonocryptops["`Untergattung 
                            **Trigonocryptops**`"]
                paratrigonocryptops["`Synonym:
                        **Paratrigonocryptops**`"]
                paplocryptops["`Untergattung 
                            **Haplocryptops**`"]
                paracryptops["`Untergattung 
                            **Paracryptops**`"]
                        

    scolopendromorpha ==> cryptopidae
    cryptopidae ==> cryptops
    trichocryptops <-.-> cryptops
    chromatanops <.-> cryptops
            cryptops ==> trigonocryptops
            paratrigonocryptops <-.-> trigonocryptops
            cryptops ==> paplocryptops
            cryptops ==> paracryptops
    click scolopendromorpha ".."
    click cryptopidae "../family-cryptopidae"
{{</mermaid>}}