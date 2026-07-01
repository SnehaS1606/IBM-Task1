from langchain.tools import tool

@tool
def attendance_checker(classes_attended: int, total_classes: int) -> str:
    """
    Calculate attendance percentage and check exam eligibility.
    A student is eligible if attendance >= 75%.
    """
    attendance_percentage = (classes_attended / total_classes) * 100
    is_eligible = attendance_percentage >= 75
    
    status = "Eligible for Exam" if is_eligible else "Not Eligible for Exam"
    
    return (
        f"Attendance Percentage: {attendance_percentage:.2f}%\n"
        f"Status: {status}"
    )

@tool
def grade_calculator(mark1: int, mark2: int, mark3: int, mark4: int, mark5: int) -> str:
    """
    Calculate average marks, grade and pass/fail status.
    """
    marks = [mark1, mark2, mark3, mark4, mark5]
    average = sum(marks) / 5
    
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"
    
    status = "PASS" if average >= 50 else "FAIL"
    
    return (
        f"Average Marks: {average:.2f}\n"
        f"Grade: {grade}\n"
        f"Result: {status}"
    )

@tool
def fee_balance_calculator(total_course_fee: float, amount_paid: float) -> str:
    """
    Calculate pending fee balance for a course.
    """
    pending = total_course_fee - amount_paid
    
    if pending <= 0:
        return f"No pending fee. You have paid the full amount of {total_course_fee:.2f}"
    
    return (
        f"Total Course Fee: {total_course_fee:.2f}\n"
        f"Amount Paid: {amount_paid:.2f}\n"
        f"Pending Fee: {pending:.2f}"
    )

@tool
def library_fine_calculator(days_late: int) -> str:
    """
    Calculate library late return fine.
    Fine is ₹5 per day for late return.
    """
    fine_per_day = 5
    total_fine = days_late * fine_per_day
    
    return (
        f"Days Late: {days_late}\n"
        f"Fine per day: ₹{fine_per_day}\n"
        f"Total Fine: ₹{total_fine:.2f}"
    )

@tool
def hostel_fee_calculator(monthly_fee: float, months_stayed: int) -> str:
    """
    Calculate hostel fee based on monthly fee and duration of stay.
    """
    total = monthly_fee * months_stayed
    
    return (
        f"Monthly Hostel Fee: {monthly_fee:.2f}\n"
        f"Months Stayed: {months_stayed}\n"
        f"Total Hostel Fee: {total:.2f}"
    )
