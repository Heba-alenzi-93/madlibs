def main():
	# write your code here
	number = input("Enter a number from 1 to 12:")
	print(number)
	noun = input("Enter a noun (plural):")
	print(noun)
	name = input("Enter a name:")
	print(name)
	capitalized_name = name.capitalize()
	sentence = input("Enter any sentence:")
	print(sentence)
	capitalized_sent = sentence.upper()
	verb = input("Enter a verb:")
	print(verb)
	print("It was "+" " + number +" "+ "o'clock when I heard a knock at the door.")
	print("I opened the door and there was a box full of " + noun +  " with a note saying From Mr." + capitalized_name)
	print("Just as I closed the door I heard a scream " +  capitalized_sent)
	print("I froze in place and all I could do was " + verb)



if __name__ == '__main__':
	main()
