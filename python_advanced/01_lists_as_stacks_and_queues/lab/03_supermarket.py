from _collections import deque
clients = deque()


while True:
    current_client = input()
    
    if current_client == "End":
        print(f"{len(clients)} people remaining.")
        break

    elif current_client == 'Paid':
        while clients:
            print(clients.popleft())
            
    else:
        clients.append(current_client)


