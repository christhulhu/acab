---
title: Kethops
description: Gattung Kethops
bookHidden: true
type: page
layout: taxonomy_genus
datadir: kethops
---

# Die Gattung: Kethops
{{<disclaimer/taxonomy-genus>}}

Wird von diversen Autoren als Gattung anerkannt.

Chamberlin (1912) stellte fest, dass Sternite normalerweise zwei oder mehr schwächere und weniger definierte transversale Sulci aufweisen, was für Scolopendromorpha ungewöhnlich ist.

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
            kethopinae --> kethops; 
            kethopinae --> thalkethops;
            click thalkethops "../thalkethops"
            kethops <-.-> thalkethops
    click scolopendromorpha ".."
{{</mermaid>}}