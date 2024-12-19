def create_acronym():
    while True:
        print("Welcome to the Acronym Creator!")
        phrase = input("Enter a phrase or sentence: ").strip()
        
        # Split the phrase into words and create an acronym
        words = phrase.split()
        acronym = "".join(word[0].upper() for word in words)
        
        print(f"The acronym for '{phrase}' is: {acronym}")

if __name__ == "__main__":
    create_acronym()
