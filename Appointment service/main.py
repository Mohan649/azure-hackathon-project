def book_appointment():
    print("\n--- Book Appointment ---")

    patient_name = input("Enter Patient Name: ")
    disease = input("Enter Disease: ")

    # Automatically converts date (DD-MM-YYYY) to day of the week
    date_str = input("Enter Appointment Date (DD-MM-YYYY): ")
    try:
        parsed_date = datetime.strptime(date_str, "%d-%m-%Y")
        day = parsed_date.strftime("%A")  
    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY.")
        return

    print(f"System detected day of appointment: {day}")

    # Display active doctors
    print("\nOur Active Doctors:")
    for doc in doctors:
        print(f"{doc['id']} - Dr. {doc['name']} ({doc['specialization']}) | Status: {doc['status']}")

    doctor_id = input("\nEnter Doctor ID to book: ")

    selected_doctor = None
    for doc in doctors:
        if str(doc["id"]) == doctor_id:
            selected_doctor = doc
            break

    if not selected_doctor:
        print("Invalid Doctor ID")
        return

    # Check Doctor availability rules
    if selected_doctor["week_off"].lower() == day.lower():
        print(f"Booking Failed: Dr. {selected_doctor['name']} has their day off on {day}s!")
        return

    if selected_doctor["status"] == "emergency":
        print(f"Booking Failed: Dr. {selected_doctor['name']} is restricted to Emergency duties.")
        return

    # Select Time Slot
    print("\nAvailable Time Slots:")
    for i, slot in enumerate(time_slots, start=1):
        print(i, slot)

    time_choice = input("\nSelect time slot number: ")

    if not time_choice.isdigit() or int(time_choice) < 1 or int(time_choice) > len(time_slots):
        print("Invalid time slot")
        return

    time = time_slots[int(time_choice) - 1]

    # Save Appointment
    appointment = {
        "patient_name": patient_name,
        "doctor_name": selected_doctor["name"],
        "disease": disease,
        "date": date_str,
        "day": day,
        "time": time
    }
    appointments.append(appointment)

    print("\nAppointment Booked Successfully!")


def view_appointments():
    print("\n--- All Appointments ---")
    if len(appointments) == 0:
        print("No appointments booked yet.")
        return

    for i, appt in enumerate(appointments, start=1):
        print(
            i,
            "| Patient:", appt["patient_name"],
            "| Doctor:", appt["doctor_name"],
            "| Disease:", appt["disease"],
            "| Day:", appt["day"],
            "| Date:", appt["date"],
            "| Time:", appt["time"]
        )
Step 3: Update Your Main Menu Loop
Finally, replace your while True: loop at the very bottom of the script to reflect the new divided sections:

Python
# ---------------- Main Menu Loop ----------------
while True:
    print("\n===== HOSPITAL SYSTEM MENU =====")
    print("1. Show Doctors")
    print("2. Register Patient (Patient Service)")
    print("3. Search Patient   (Patient Service)")
    print("4. Book Appointment (Appointment Service)")
    print("5. View Appointments (Appointment Service)")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_doctors()
    elif choice == "2":
        register_patient()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        book_appointment()
    elif choice == "5":
        view_appointments()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")