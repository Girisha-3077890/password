This Python script generates secure random passwords.

It imports the random and string modules.

The main function is generate_password().

It accepts parameters for length and character types.

Options include digits, special characters, uppercase, and lowercase.

A character pool is built based on user preferences.

If no character set is selected, it raises a ValueError.

The password is created by randomly choosing characters.

The default password length is 12 characters.

The function returns the generated password as a string.

Another function, generate_multiple_passwords(), creates several passwords.

It calls generate_password() repeatedly in a list comprehension.

The user can specify count and length for multiple passwords.

Example usage shows generating one 16-character password.

It also demonstrates generating three 10-character passwords without special symbols.

