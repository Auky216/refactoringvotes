import csv

def count_votes(file_path):
    results = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip the header

        for row in reader:
            city = row[0]
            candidate = row[1]
            votes = parse_votes(row[2])  # Extracción de método para manejo de votos

            if candidate in results:
                results[candidate] += votes
            else:
                results[candidate] = votes

    display_results(results)  # Extracción de método para mostrar resultados
    announce_winner(results)  # Extracción de método para anunciar ganador

def parse_votes(vote_count):
    """Intenta convertir los votos a entero, retorna 0 si no es posible."""
    try:
        return int(vote_count)
    except ValueError:
        return 0

def display_results(results):
    """Muestra los resultados de cada candidato."""
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

def announce_winner(results):
    """Determina y muestra al ganador basado en la cantidad de votos."""
    sorted_by_votes = sorted(results.items(), key=lambda item: item[1], reverse=True)
    print(f"winner is {sorted_by_votes[0][0]}")
