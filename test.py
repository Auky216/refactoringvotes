from vote_counter import count_votes, parse_votes, display_results, announce_winner
import csv

test_data = [
    ("Springfield,Alice,1200\nSpringfield,Bob,750\nShelbyville,Alice,2000\nShelbyville,Bob,2500", "Bob"),
    
    ("Springfield,Alice,invalid\nSpringfield,Bob,750\nShelbyville,Alice,2000\nShelbyville,Bob,2500", "Bob"),
    
    ("Springfield,Alice,1500\nSpringfield,Bob,1500", "Empate"),
    
    ("Springfield,Alice,3000", "Alice"),
    
    ("Springfield,Alice,invalid\nShelbyville,Bob,invalid", "No hay votos válidos")
]

def run_test():
    for idx, (csv_data, expected_winner) in enumerate(test_data):
        print(f"\nPrueba {idx + 1}:")
        with open("test_votes.csv", "w") as file:
            file.write("city,candidate,votes\n") 

        print("Resultados:")
        count_votes("test_votes.csv")

        results = {}
        with open("test_votes.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)  
            for row in reader:
                candidate = row[1]
                votes = parse_votes(row[2])
                if candidate in results:
                    results[candidate] += votes
                else:
                    results[candidate] = votes
        winner = determine_winner(results)
        
        if winner == expected_winner:
            print(f"Prueba {idx + 1} pasada: ganador esperado '{expected_winner}' coincide con el resultado.")
        else:
            print(f"Prueba {idx + 1} fallida: esperado '{expected_winner}', pero se obtuvo '{winner}'.")

def determine_winner(results):
    """Función auxiliar para determinar al ganador o manejar un empate."""
    sorted_by_votes = sorted(results.items(), key=lambda item: item[1], reverse=True)
    if len(sorted_by_votes) > 1 and sorted_by_votes[0][1] == sorted_by_votes[1][1]:
        return "Empate"
    elif sorted_by_votes:
        return sorted_by_votes[0][0]
    return "No hay votos válidos"

run_test()
