---
title: Cryptopidae
description: Familie Cryptopidae
bookHidden: true
type: page
layout: taxonomy_genus
datadir: cryptopidae
---

# Die Familie: Cryptopidae
{{<disclaimer/taxonomy-genus>}}

Die Familie Cryptops wurde in verschiedenen Studien behandelt und von Edgecombe und Bonato (2011) in zwei eng verwandte Gattungen unterteilt: [**Cryptops**](../cryptops) und **Paracryptops**. Vahtera et al. (2012) schlugen vor, dass letzteres ein Synonym des ersteren ist, wodurch diese Familie monotypisch wird.

{{<mermaid>}}
    flowchart TB
        scolopendromorpha["`Ordnung
                            **Scolopendromorpha**`"]
        cryptopidae["`Familie
                    **Cryptopidae**`"]
            cryptops["`Gattung
                    **Cryptops**`"]
            paracryptops["`Synonym:
                        **Paracryptops**`"]
            
                        

    scolopendromorpha ==> cryptopidae
    cryptopidae ==> cryptops; click cryptops "../cryptops"
    cryptopidae -.-> paracryptops
    cryptops <-.-> paracryptops
    click scolopendromorpha ".."
{{</mermaid>}}