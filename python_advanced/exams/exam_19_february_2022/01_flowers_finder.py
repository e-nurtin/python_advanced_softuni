from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {
	"rose": [],
	"tulip": [],
	"lotus": [],
	"daffodil": [],
}

word_is_found = False

while vowels and consonants:
	vowel = vowels.popleft()
	consonant = consonants.pop()
	
	for word in words:
		if vowel in word and vowel not in words[word]:
			words[word].append(vowel * word.count(vowel))
				
		if consonant in word and consonant not in words[word]:
			words[word].append(consonant * word.count(consonant))
			
		if len(word) == len(''.join(words[word])):
			print(f"Word found: {word}")
			word_is_found = True
			break
			
	if word_is_found:
		break

if not word_is_found:
	print("Cannot find any word!")

if vowels:
	print(f"Vowels left: {' '.join(vowels)}")

if consonants:
	print(f"Consonants left: {' '.join(consonants)}")
	