if __name__ == "__main__":
    pokedex = {
    }
    pokedex["Venosaur"] = ["Grass", "Poisen"]
    extra_dict = {
        "Charizard": ["Fire", "Flying"],
        "Blastoise": ["Water"]
    }
    pokedex.update(extra_dict)
    pokedex.pop("Blastoise")
    