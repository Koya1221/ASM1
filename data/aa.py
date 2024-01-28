full_name = input("What is your full name? ")
credit_1 = int(input("Enter the credit for English course: "))
credit_2 = int(input("Enter the credit for C# course: "))
credit_3 = int(input("Enter the credit for Python course: "))
point_1 = float(input("Enter the point for English course: "))
point_2 = float(input("Enter the point for C# course: "))
point_3 = float(input("Enter the point for Python course: "))

credits = [credit_1, credit_2, credit_3]
points = [point_1, point_2, point_3]

def calculate_gpa(credits, points):
    weighted_sum = sum(credits[i] * points[i] for i in range(len(points)))
    total_credits = sum(credits)
    gpa = weighted_sum / total_credits
    return gpa

def show_student_gpa(name, gpa):
    print("Student:", name)
    print("Cumulative Grade Point Average:", gpa)
    try:
        file = open('data/point.txt', 'w')
        file.write("Student: " + name + " Cumulative Grade Point Average: " + str(gpa))
        file.close()
    except:
        print("An error occurred.")

gpa = calculate_gpa(credits, points)
show_student_gpa(full_name, gpa)


