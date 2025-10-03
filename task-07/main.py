import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Init frequency for values ​​2..12
    counts = {s: 0 for s in range(2, 13)}

    # Dice roll simulation
    for _ in range(num_rolls):
        total = random.randint(1, 6) + random.randint(1, 6)
        counts[total] += 1

    # Obtain probabilities
    probabilities = {s: counts[s] / num_rolls for s in counts}
    
    return probabilities

def plot_probabilities(probabilities, title_suffix=""):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірність суми чисел на двох кубиках {title_suffix}')
    
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.ylim(0, 0.2)
    plt.show()


if __name__ == "__main__":
    
    analytical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    # Analytical table output
    print("Аналітичні ймовірності:")
    for s, p in analytical_probs.items():
        print(f"Сума {s}: {p*100:.2f}%")

    # Running Monte Carlo with varying accuracy
    for accuracy in [100, 1000, 10000, 100000]:        
        # Dice roll simulation and obtain probabilities
        probabilities = simulate_dice_rolls(accuracy)

        print(f"\nСимуляція {accuracy} кидків:")
        for s, p in probabilities.items():
            print(f"Сума {s}: {p*100:.2f}% (аналітична {analytical_probs[s]*100:.2f}%)")

        # Graphical visualization of probabilities
        plot_probabilities(probabilities, title_suffix=f"(N={accuracy})")