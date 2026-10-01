high_income = False
good_credit = True
student = True

# Short Circuit Evaluation

# Here the or operator is short circuit evaluated because the first condition is false, so the second condition is not evaluated.
if high_income and good_credit and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Here one of the condition has to be true which is good_credit, so the next condition is not evaluated.
if high_income or good_credit or not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
