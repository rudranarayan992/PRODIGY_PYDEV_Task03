# 🔐 Task 03: Password Complexity Checker
# Internship: Prodigy InfoTech - Comillas Negras
#this code is wrriten by Rudra narayan swain
import re

def check_password_complexity(password):
    """
    Evaluates the complexity of the given password based on common security rules.
    Returns feedback on how to improve the password if it's weak.
    """

    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check if all criteria are satisfied
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "\n✅ Strong password! Your password meets all recommended criteria. 👍"
    else:
        feedback = "\n❌ Weak password. Please improve the following:\n"
        if not length_criteria:
            feedback += "- 🔸 Make it at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- 🔸 Add at least one **uppercase letter**\n"
        if not lowercase_criteria:
            feedback += "- 🔸 Add at least one **lowercase letter**\n"
        if not digit_criteria:
            feedback += "- 🔸 Include at least one **number**\n"
        if not special_char_criteria:
            feedback += "- 🔸 Include at least one **special character** (e.g. !@#$%^&*)\n"

        return feedback

def main():
    print("="*40)
    print("🔐 Welcome to the Password Complexity Checker")
    print("="*40)

    password = input("🔎 Enter your password to check: ")
    result = check_password_complexity(password)
    
    print(result)
    print("="*40)

if __name__ == "__main__":
    main()
