# We want to creat a mail merge programm
# In this, every patient can leave his name and adress
# And we send them a chrismas card

# To complete this project, we will create variables with string values and connect them
# In this project, we will explore two ways to accomplish it

# 1. Step: create the patient name and adress as a string
patient_name = "John Doe"
patient_adress = "123 Main Street"

# 2. Step: write the card header
print("To: " + patient_name + "\n" + patient_adress)

# 3. Step: write the card body
print("Dear " + patient_name + "\n" + "We wish you a merry christmas and a happy new year!")

# 4. Step: write the card footer
print("Best regards")

# This is one way to do it
# But there is a easyer way
# Lets test a second way

# 1. Step: create patient name and adress as a string
patient_name = "Markus Müller"
patient_adress = "536 Broadway"

# 2. Step: write the card header
print(f"To: {patient_name}\n{patient_adress}")

# 3. Step: write the card body
print(f"Dear {patient_name}\nWe wish you a merry christmas and a happy new year!")

# 4. Step: write the card footer
print("Best regards")

# There are more ways to deal with this
# But this are the most common ways to do it
