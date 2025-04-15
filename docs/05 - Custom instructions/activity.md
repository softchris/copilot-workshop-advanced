---
sidebar_position: 2
---

# Activity: add custom instructions

Try the following activity with the Edit mode.

## -1- Create a copilot-instructions.md file

Create a `copilot-instructions.md` file in the `.github` directory of your repository. Here's an example of its content:

```text
- Start all variables with underscore
- Use camelCase for function names
- Add the text "AI generated code" right above the code block.
```

Now let's test the custom instructions.

Type the following code in the chat window (make sure you have a file open called `util.py`):

```text
create a validate_email function in util.py
```

You should see an output similar to this:

```python
# AI generated code
import re

def validateEmail(_email):
    """
    Validates an email address using a regex pattern.
    
    Args:
        _email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    _emailPattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(_emailPattern, _email) is not None
```

![Custom instruction](/img/custom-instruction.png)

Note how your instructions were followed. The variable name starts with an underscore `_emailPattern`, the function name is in camelCase `validateEmail`, and the comment "AI generated code" is added above the code block.

## -2- Create new files for Python and JavaScript instructions

However, as a Python developer, you might prefer to use snake_case for variable names. Let's move the camel case instruction to a separate file and create a new file for Python-specific instructions like so:

```text
|- .github/copilot-instructions.md
|- .github/python-instructions.md
|- .github/javascript-instructions.md
```

Let's add some reasonable instructions to the `python-instructions.md` file:

```text
- use snake_case for variable names

- use type hints for function definitions
- prefer f-strings for string formatting
- avoid wildcard imports (e.g., `from module import *`)
- write unit tests for all new features
- follow PEP 8 style guidelines
- use virtual environments for dependency management
```

and some reasonable instructions to the `javascript-instructions.md` file:

```text
- Use camelCase for function names
- Use `let` and `const` instead of `var`
- Prefer arrow functions for anonymous functions
- Always use strict equality (`===`) instead of loose equality (`==`)
- Place semicolons at the end of statements
- Use template literals for string concatenation
```

Left in the `copilot-instructions.md` file is the following:

```markdown
- Start all variables with underscore
- Add the text "AI generated code" right above the code block.
```

### Try the same prompt

Type the same prompt again with `util.py` open in the chat window:

```text
prompt
```

You should now see a slightly different output:

```python
import re

def validate_email(_email: str) -> bool:
    """
    Validates an email address using a regex pattern.
    
    Args:
        _email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    _email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(_email_pattern, _email) is not None
```

Note how the variable name is now in snake_case `_email_pattern`, and the function name is in snake_case `validate_email`. Additionally, there's now also a new file `test-util.py` with the following content:

```python
# AI generated code
import unittest
from util import validate_email

class TestValidateEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name+tag+sorting@example.com"))
        self.assertTrue(validate_email("x@example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("plainaddress"))
        self.assertFalse(validate_email("@missingusername.com"))
        self.assertFalse(validate_email("username@.com"))

if __name__ == "__main__":
    unittest.main()
```

The tests are created thanks to the instruction in `python-instructions.md` to write unit tests for all new features. 

## -3- Create a new project using custom instructions

You can use custom instructions when creating a new project as well. For example, you can describe the project and its purpose and then see if Copilot can create a project for you.

So for this prompt, we will instruct Copilot to create a new project:

```text
generate a book management system in the directory book-management, you MUST follow tech choices laid out by #file project.md
```

You should see a list of files and content being generated. It doesn't create the files but tell you what files it would create and what content. It also follows the instructions in the custom instruction files. In *project.md*, we instruct it to use JavaScript which means the custom instructions in `javascript-instructions.md` will be used. 

 