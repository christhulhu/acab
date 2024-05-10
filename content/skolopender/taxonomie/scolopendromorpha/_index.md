---
title: Taxonomie der Ordnung Scolopendromorpha
bookHidden: true
layout: taxonomy_overview
type: page
---

# Taxonomie der Ordnung Scolopendromorpha

{{<hint "warning">}}
Dieser Abschnitt befindet sich noch im Aufbau. Alle Inhalte sind aktuell lediglich eine öffentliche Beta-Vorschau.
{{</hint>}}

{{<mermaid>}}
flowchart TD
    scolopendromorpha["`Ordnung
                        **Scolopendromorpha**`"]
    cryptopidae["`Familie
                **Cryptopidae**`"]
        cryptops["`Gattung
                **Cryptops**`"]
            %% chromatanops["`Untergattung 
            %%             **Chromatanops**`"]
            %% trigonocryptops["`Untergattung 
            %%             **Trigonocryptops**`"]
            %% paplocryptops["`Untergattung 
            %%             **Haplocryptops**`"]
            %% paracryptops["`Untergattung 
            %%             **Paracryptops**`"]
    scolopocryptoidae["`Familie
                        **Scolopocryptoidae**`"]
        kethopinae["`Unterfamilie
                    **Kethopinae**`"]
            kethops["`Gattung
                    **Kethops**`"]
            thalkethops["`Gattung
                    **Thalkethops**`"]
        newportiinae["`Unterfamilie
                    **Newportiinae**`"]
            newportia["`Gattung
                     **Newportia**`"]
                %% tidops["`Untergattung 
                %%         **Tidops**`"]
                %% ectonocryptops["`Untergattung 
                %%         **Ectonocryptops**`"]
                %% ectonocryptoides["`Untergattung 
                %%         **Ectonocryptoides**`"]
                %% newportides["`Untergattung 
                %%         **Newportides**`"]
        %% ectonocryptopinae["`Unterfamilie 
        %%                 **Ectonocryptopinae**`"]
        scolopocryptopinae["`Unterfamilie 
                            **Scolopocryptopinae**`"]
            scolopocryptops["`Gattung
                            **Scolopocryptops**`"]
            %% dinocryptops["`Gattung
            %%             **Dinocryptops**`"]
    mimopidae["`Familie
                **Mimopidae**`"]
        mimops["`Gattung
                **Mimops**`"]
    plutoniumidae["`Familie
                **Plutoniumidae**`"]
        plutonium["`Gattung
                **Plutonium**`"]
        theatops["`Gattung
                **Theatops**`"]
    scolopendridae["`Familie
                **Scolopendridae**
                TBD`"]


    scolopendromorpha ==> scolopocryptoidae
    %% click scolopocryptoidae "./family-scolopocryptoidae"
    
        scolopocryptoidae ==> kethopinae
            kethopinae ==> kethops; click kethops "./kethops"
            kethopinae ==> thalkethops; click thalkethops "./thalkethops"
            %% kethops <-.-> thalkethops
        scolopocryptoidae ==> newportiinae
            newportiinae ==> newportia; click newportia "./newportia"
            %% newportia ==> tidops
            %% newportia ==> ectonocryptops
            %% newportia ==> ectonocryptoides
            %% newportia ==> newportides
            %% newportiinae <-.-> ectonocryptopinae
        scolopocryptoidae ==> scolopocryptopinae; 
            scolopocryptopinae ==> scolopocryptops; click scolopocryptops "./scolopocryptops"
            %% scolopocryptopinae -.-> dinocryptops; click dinocryptops "./scolopocryptops"
            %% scolopocryptops <==> dinocryptops
        scolopendromorpha ==> cryptopidae; click cryptopidae "./family-cryptopidae"
            cryptopidae ==> cryptops; click cryptops "./cryptops"
                %% cryptops ==> chromatanops
                %% cryptops ==> trigonocryptops
                %% cryptops ==> paplocryptops
                %% cryptops ==> paracryptops
        scolopendromorpha ==> mimopidae; click mimopidae "./family-mimopidae"
                mimopidae ==> mimops; click mimops "./mimops"
        scolopendromorpha ==> plutoniumidae
                plutoniumidae ==> plutonium; click plutonium "./plutonium"
                plutoniumidae ==> theatops;  click theatops "./theatops"
        scolopendromorpha ==> scolopendridae

{{</mermaid>}}


{{<mermaid>}}
        flowchart TD
{{</mermaid>}}





