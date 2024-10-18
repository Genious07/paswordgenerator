import streamlit as st
from deep_translator import GoogleTranslator
import random
import string
import uuid
import pyperclip


# Function to translate text using GoogleTranslator
def translate_text(text, dest_language='es'):
    try:
        translator = GoogleTranslator(source='auto', target=dest_language)
        return translator.translate(text)
    except Exception as e:
        st.error(f"Translation error: {e}")
        return text


# Function to generate password
def generate_password(base_text, special_chars=True, numbers=True):
    translated_text = translate_text(base_text)
    password = translated_text

    # Add special characters
    if special_chars:
        special_chars_list = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
        password += random.choice(special_chars_list)

    # Add numbers
    if numbers:
        password += str(random.randint(100, 999))

    # Ensure password is unique by adding a unique suffix
    unique_suffix = uuid.uuid4().hex[:6]
    password += unique_suffix

    return password


# Main function to define the Streamlit app
def main():
    st.title("🔐 Password Generator")
    st.write("Generate a secure password based on your input.")

    # User input for the base text
    user_input = st.text_input("Enter any English word to make a password:", "")

    # Checkbox options for customization
    special_chars = st.checkbox("Include Special Characters", value=True)
    numbers = st.checkbox("Include Numbers", value=True)

    # Button to generate the password
    if st.button("Generate Password"):
        if user_input.strip() == "":
            st.warning("Please enter a valid English word.")
        else:
            password = generate_password(user_input, special_chars, numbers)
            st.success("**Generated Password:**")
            # Display the password in a text input for easy copying
            st.text_input("Copy the generated password:", value=password, key="password",
                          help="Click inside the box and press Ctrl+C (Cmd+C on Mac) to copy.")

            # Attempt to copy to clipboard (Note: This may not work as expected in all environments)
            try:
                pyperclip.copy(password)
                st.info("Password copied to clipboard!")
            except pyperclip.PyperclipException:
                st.warning("Failed to copy to clipboard. Please copy manually.")

    # Footer
    st.markdown("---")
    st.markdown("Developed with ❤️ by satwik")


if __name__ == "__main__":
    main()
