input = "USA (spezifisch: Ein Bereich, der sich von Südost-North Carolina bis Süd-Nevada erstreckt), Mexiko, Länder in Zentralamerika, die sich bis Zentral-Panama erstrecken (dazu gehören beispielsweise Guatemala, Honduras, El Salvador, Nicaragua und Costa Rica), Panama (spezifisch: Ehemalige Kanalzone und die Perleninseln)"

for i in input.split(','):
    print(f'- {i.strip()}')