from solver import DecisionTree, solver
import random

def train(iterations):
    for i in range(iterations):
        cards = ["Jack", "Queen", "King"]
        first_card = cards[random.randint(0,2)]
        cards.pop(cards.index(first_card))
        second_card=cards[random.randint(0,1)]
        solver([first_card, second_card], "", [1.0, 1.0])
        print(i)

if __name__=="__main__":
    train(100000)
    for node in DecisionTree:
        print(node, DecisionTree[node].compute_average_strategy())
        