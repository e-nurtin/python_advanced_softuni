gamers = input().split()
elimination_n = int(input())
index = 0
count = 1

while len(gamers) > 1:  # Josephus permutation algorithm
    # This line makes sure that we are always in the boundaries of the list
    if index == len(gamers):
        index -= len(gamers)
    # remove the player if the count matches our elimination number
    if count == elimination_n:
        print(f"Removed {gamers.pop(index)}")
        count = 0  # Count is reset after successful elimination
        index -= 1  # We need to remove from index because we popped the item on the
        # index and next item is on the same index as the removed one.

    count += 1
    index += 1
print(f"Last is {''.join(gamers)}")
