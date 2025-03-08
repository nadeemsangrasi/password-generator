import streamlit as st
import sys
import streamlit.web.cli as stcli  
import string
import random

def start():
    sys.argv = ["streamlit", "run", "src/password_generator/main.py"]
    sys.exit(stcli.main())
def main():
    st.title("Password Generator")
    st.header("Generate your secure password!")

    length = st.number_input(label="Enter password length greater then 6 and less then 32 ",value=12,min_value=6,max_value=32)

    if not length:
        st.error("Please provide valid length")
        return
  
    use_uppercase = st.checkbox("Include Uppercase Letters", value=random.choice([True,False]))
    use_lowercase = st.checkbox("Include Lowercase Letters", value=random.choice([True,False]))
    use_numbers = st.checkbox("Include Numbers", value=random.choice([True,False]))
    use_special = st.checkbox("Include Special Characters", value=random.choice([True,False]))

    password_chars=""

    if use_uppercase:
        password_chars+=string.ascii_uppercase
    if use_lowercase:
        password_chars+=string.ascii_lowercase
    if use_numbers:
        password_chars+=string.digits
    if use_special:
        password_chars+=string.punctuation
    
    generate = st.button("Generate")

    if generate:
        if password_chars:  
                password = ''.join(random.choice(password_chars) for _ in range(length))
                st.success("Generated Password:")
                st.code(password)
                if len(password) >= 24 and sum([use_uppercase, use_lowercase, use_numbers, use_special]) >= 4:
                    st.write("Password Strength: too Strong Password!💪💪")
                elif len(password) >= 12 and sum([use_uppercase, use_lowercase, use_numbers, use_special]) >= 3:
                    st.write("Password Strength: Strong Password! 💪")
                elif len(password) >= 8 and sum([use_uppercase, use_lowercase, use_numbers, use_special]) >= 2:
                    st.write("Password Strength: ⚠️ Moderate Password - Consider adding more security features.")
                elif len(password) >= 5 and sum([use_uppercase, use_lowercase, use_numbers, use_special]) >= 2:
                    st.write("Password Strength: ❌ Weak Password - Improve it using the suggestions above.")
                else:
                    st.write("Password Strength: ❌ Very Weak Password - Please increase length and add more character types.")
        else:
            st.error("Please select at least one character type")

        
            
if __name__ == "__main__":
    main()