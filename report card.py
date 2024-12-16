import csv

# Function to input marks for a subject
def input_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter number of {subject} out of 100: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter a valid number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to check if the student failed in any subject
def check_failures(p, c, m):
    failed = False
    if p <= 33:
        print("Failed in Physics")
        failed = True
    if c <= 33:
        print("Failed in Chemistry")
        failed = True
    if m <= 33:
        print("Failed in Maths")
        failed = True
    return failed

# Function to calculate total marks and percentage
def calculate_total_and_percentage(p, c, m):
    total = p + c + m
    percentage = total * 100 / 300
    return total, percentage

# Function to determine the division based on percentage
def determine_division(percentage):
    if percentage >= 70:
        return "Grade A (First Division)"
    elif percentage >= 50:
        return "Grade B (Second Division)"
    elif percentage >= 33:
        return "Grade C (Pass)"
    else:
        return "Fail"

# Function to save results to a CSV file
def save_to_csv(student_results):
    with open("student_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(student_results)

# Function to display detailed report card
def display_report_card(name, p, c, m, total, percentage, division):
    print("\n*** Report Card ***")
    print(f"Student Name: {name}")
    print(f"Physics: {p}")
    print(f"Chemistry: {c}")
    print(f"Maths: {m}")
    print(f"Total Marks: {total} / 300")
    print(f"Percentage: {percentage}%")
    print(f"Division: {division}")
    print("\n***************************")

# Main function to run the program
def main():
    # Input student name
    name = input("Enter student name: ")

    student_results = []

    # Input marks for each subject
    p = input_marks("Physics")
    c = input_marks("Chemistry")
    m = input_marks("Maths")

    # Display the marks
    print("Marks in Physics:", p)
    print("Marks in Chemistry:", c)
    print("Marks in Maths:", m)

    # Check for failures
    if check_failures(p, c, m):
        print("You have failed. Please try again next year.")
        return

    # Calculate total marks and percentage
    total, percentage = calculate_total_and_percentage(p, c, m)
    division = determine_division(percentage)

    # Display the report card
    display_report_card(name, p, c, m, total, percentage, division)

    # Save results to CSV
    student_results = [name, p, c, m, total, percentage, division]
    save_to_csv(student_results)

    # Ask if the user wants to enter another student's data
    another_student = input("\nDo you want to enter marks for another student? (y/n): ").lower()
    if another_student == 'y':
        main()  # Recursively call main to allow multiple students

# Run the main function
main()
