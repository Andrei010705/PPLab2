print("\nAici e coul nou python: ")

n = len(lista)
if n != 0:
    sorted_list = sorted(lista)
    remove_count = int(n * 0.2)
    trimmed = sorted_list[remove_count : n - remove_count]
    if trimmed:  # dacă lista rezultată e goală
        mean = sum(trimmed) / len(trimmed)
        print(mean)