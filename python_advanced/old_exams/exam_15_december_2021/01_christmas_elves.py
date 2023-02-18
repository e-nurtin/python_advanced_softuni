from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

elf_number, total_energy, toys_made = 0, 0, 0


while elves_energy and materials:
	current_elf = elves_energy.popleft()
	
	if current_elf < 5:
		continue
	elf_number += 1
	
	needed_energy = materials.pop()
	if needed_energy <= current_elf:
		
		if elf_number % 3 == 0:
			
			if needed_energy * 2 > current_elf:
				elves_energy.append(current_elf * 2)
				materials.append(needed_energy)
				continue
		
			if elf_number % 5 == 0:
				total_energy += needed_energy * 2
				elves_energy.append(current_elf - (needed_energy * 2))
				continue
				
			total_energy += needed_energy
			current_elf -= needed_energy
			toys_made += 1
			
		elif elf_number % 5 == 0:
			total_energy += needed_energy
			elves_energy.append(current_elf - needed_energy)
			continue
		
		toys_made += 1
		current_elf -= needed_energy
		total_energy += needed_energy
		elves_energy.append(current_elf + 1)
		
	else:
		elves_energy.append(current_elf * 2)
		materials.append(needed_energy)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy}")

if elves_energy:
	print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")

if materials:
	print(f"Boxes left: {', '.join([str(x) for x in materials])}")
