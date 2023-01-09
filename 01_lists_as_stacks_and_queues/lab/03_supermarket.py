clients = []


while True:
    current_client = input()

    if current_client == 'Paid':
        # print('\n'.join([clients.pop(0) for x in range(len(clients))]))
        print('\n'.join(clients))
        clients = []
        continue

    if current_client == "End":
        print(f"{len(clients)} people remaining.")
        break

    clients.append(current_client)


