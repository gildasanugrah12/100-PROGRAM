def habitat_hewan(hewan):
    habitat = {
        "gajah": "Hutan",
        "kucing": "Rumah",
        "burung": "Hutan",
        "ikan": "Laut",}
    return habitat.get(hewan, "Habitat tidak diketahui")

hewan_input = input("Masukkan nama hewan: ")
print(f"Habitat {hewan_input} adalah: {habitat_hewan(hewan_input)}")