---
title: Thalkethops
description: Gattung Thalkethops
bookHidden: true
type: page
layout: taxonomy_genus
datadir: thalkethops
---

# Die Gattung: Thalkethops
{{<disclaimer/taxonomy-genus>}}

In verschiedenen Studien (Edgecombe & Bonato 2011, Bonato et al. 2016, Lewis 2016) wird behandelt, dass **Thalkethops** und **Kethops** als Gattungen betrachtet werden. Shelley (2002) hat in seiner kurzen und nicht detaillierten Abhandlung über **Kethopinae** angemerkt, dass es kaum Unterschiede zwischen **Thalkethops** und **Kethops** gibt. Er schlug vor, dass sie möglicherweise zusammengeführt werden müssen, wenn mehr Material von beiden verfügbar ist. Er stellte fest, dass es sechs weitere Exemplare (zusätzlich zum Holotyp) aus sechs "neuen Orten" (alle in New Mexico) gibt und dass "keine beobachtbare Variation erkennbar ist".

{{<mermaid>}}
flowchart LR
    scolopendromorpha["`Ordnung
                        **Scolopendromorpha**`"]
    scolopocryptoidae["`Familie
                        **Scolopocryptoidae**`"]
        kethopinae["`Unterfamilie
                    **Kethopinae**`"]
            kethops["`Gattung
                    **Kethops**`"]
            thalkethops["`Gattung
                    **Thalkethops**`"]

    scolopendromorpha --> scolopocryptoidae
    
        scolopocryptoidae --> kethopinae
            kethopinae --> kethops; click kethops "../kethops"
            kethopinae --> thalkethops;
            kethops <-.-> thalkethops

    click scolopendromorpha ".."
{{</mermaid>}}