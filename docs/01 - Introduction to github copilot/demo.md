---
sidebar_position: 2
---

# Demo of GitHub Copilot

Let's show you how to use GitHub Copilot in a real-world scenario. In this demo, we will create a simple Python script that generates random passwords. We will use GitHub Copilot to help us write the code and provide suggestions.

## -1- Create a new Python file

Let's start by opening our code editor and creating a new Python file called `password_generator.py`. We will then write a function that generates a random password based on user-defined criteria.

## -2- Write the function signature

Provide the following prompt to GitHub Copilot:

```python
Create a function called `generate_password` that generates a random password. 
```

## -3- Accept the suggestion

Let's see what GitHub Copilot suggests. It should provide a function signature and some code to generate a random password. Accept the suggestion by pressing `Tab`.

You should see code similar to this:

```python
def generate_password(length: int, use_special_chars: bool = True) -> str:
    import random
    import string

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

## -4- Add a docstring

Now, let's add a docstring to the function to explain what it does. Provide the following prompt to GitHub Copilot:

```text
Add a docstring to the function `generate_password` that explains what it does and its parameters.
```

Accept the suggestion by pressing `Tab`.
You should see a docstring similar to this:

```python
def generate_password(length: int, use_special_chars: bool = True) -> str:
    """
    Generate a random password.

    Parameters:
    length (int): The length of the password.
    use_special_chars (bool): Whether to include special characters in the password.

    Returns:
    str: The generated password.
    """
```

## -5- Add a test

Now, let's add a test for the `generate_password` function. Provide the following prompt to GitHub Copilot:

```text
Create a test for the `generate_password` function using the `unittest` framework.
```

Accept the suggestion by pressing `Tab`.

You should see a test similar to this:

```python
import unittest

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password(12, True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
```

As you can see, GitHub Copilot has generated a test case that checks if the password meets the specified criteria. It's up to you to modify the test case to fit your needs.
