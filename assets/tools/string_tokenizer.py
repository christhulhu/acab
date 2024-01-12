input = "Saudi-Arabien, Vereinigte Arabische Emirate (VAE), Oman, Jemen (einschließlich Socotra und Abd al Kuri), Iran, Indien"

for i in input.split(','):
    print(f'- {i.strip()}')