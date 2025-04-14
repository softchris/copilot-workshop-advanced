---
sidebar_position: 2
---

# Activity: Writing your first prompts

- **Add features**, add features to a basic codebase using comments (e.g., add user input, simple calculations).
- **Fix bugs**, let's fix a bug in the codebase using Copilot's suggestions.
- **Refactor**, let's improve a codebase using Copilot's suggestions.

## Add features

Let's take this REST API and add more features to it. The API manages your product catalog:

```python file=./code/feature.py
```

Task: Write a prompt to support pagination, client should be able to specify the page and the number of items per page. The API should return a paginated list of products.

1. Try typing it as a comment directly in a code file. For example:

```python
# Add pagination to the /products endpoint. The client should be able to specify the page and the number of items per page. The API should return a paginated list of products.
```

1. Try the same comment in the chat interface.

## Refactor

Refactor the code to something you want to maintain, i.e a class-based approach where responsibilities are separated. For example, you can create a `Product` class and a `ProductService` class to handle the business logic. You can also create a `ProductController` class to handle the API endpoints.

1. Use the chat interface for this.

Suggested prompts:

- Refactor the code to use a class-based approach and separating concerns.

## Fix a bug

```python file=./code/discount.py
```

Here's the test file:

```python file=./code/test_discount.py

```

Suggested prompts:

- What does this code do?
- Change it to "behavior"

## Optional: Improve security

The idea here is to make the API more secure. Ask Copilot to consider how to make the code more secure. 

Suggested prompts:

- How would you make this code more secure?
- Add authentication to the API.
- Add authorization to the API.