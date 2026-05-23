def register_patient():
    print("\n--- Patient Registration ---")

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    aadhaar = input("Enter Aadhaar Number: ")
    gender = input("Enter Gender: ")
    address = input("Enter Address: ")
    disease = input("Enter Disease: ")
    duration = input("Since how long: ")

    patient = {
        "name": name,
        "age": age,
        "aadhaar": aadhaar,
        "gender": gender,
        "address": address,
        "disease": disease,
        "duration": duration
    }

    patients.append(patient)
    print("\nPatient Registered Successfully!")


def search_patient():
    print("\n--- Search Patient ---")
    if not patients:
        print("No patients registered in the system yet.")
        return

    search_term = input("Enter Patient Name or Aadhaar to search: ").strip().lower()
    found_patients = []

    for p in patients:
        if search_term in p["name"].lower() or search_term in p["aadhaar"]:
            found_patients.append(p)

    if not found_patients:
        print("No matching patient found.")
    else:
        print(f"\nFound {len(found_patients)} matching record(s):")
        for i, p in enumerate(found_patients, start=1):
            print(f"\n[{i}] Name: {p['name']} | Age: {p['age']} | Gender: {p['gender']}")
            print(f"    Address: {p['address']}")
            print(f"    Condition: {p['disease']} ({p['duration']})")