


from storage import load_habits, save_habits

def display_habits(habits):
    print("\n--- 🎯 Your Habits ---")
    if not habits:
        print("No habits added yet!")
    for habit, completed in habits.items():
        status = "✅ Done" if completed else "❌ Pending"
        print(f"- {habit}: {status}")
    print("-" * 22)

def main():
    habits = load_habits()
    
    while True:
        display_habits(habits)
        print("\n1. Add Habit\n2. Toggle Habit Status\n3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            name = input("Enter habit name: ").strip()
            if name:
                habits[name] = False
                save_habits(habits)
        elif choice == "2":
            name = input("Enter habit name to toggle: ").strip()
            if name in habits:
                habits[name] = not habits[name]
                save_habits(habits)
            else:
                print("Habit not found!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()



