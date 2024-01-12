input = "São Tomé & Príncipe, Elfenbeinküste (Ivory Coast), Liberia, Tansania (spezifisch: Sansibar), Südafrika (spezifisch: Port Elizabeth), Seychellen, Réunion, Mauritius, Rodrigues, Madagaskar"

for i in input.split(','):
    print(f'- {i.strip()}')