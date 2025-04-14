---
sidebar_position: 3
---

# Activity: Use context variables `@`

Now we will use the context variables to help us with some common scenarios. 

:::note
There are many context variables, just type `@` and you will see a full list.
:::

## Scenario: Let's work on a sample project

This sample project is a simple Flask application that provides a REST API for managing products. The API allows you to perform CRUD operations on products, including creating, reading, updating, and deleting products. The application uses SQLAlchemy as the ORM for database interactions.

Using this repo, we will explore how to use Copilot to help us context variables to help us out.

### -1- Clone the repo

Clone the following repo:

```bash
git clone https://github.com/softchris/flask-sample.git
```

### -2- Inspect the repo

Run the following prompt

```text
 tell me about this repo
``

You should see an output like this:

```text
Here are some details:

- Default Branch: main
- Visibility: Public
- Issues Enabled: Yes
- Wiki Enabled: Yes
- Forking Allowed: Yes
- Topics: None listed
- Stargazers: 0
- Forks: 0
- Created: 4 minutes ago
- Last Pushed: April 12, 2025 (future timestamp).
```

Try adding some repo issues or PRs to the repo and run the same prompt again. You should see the new issues or PRs listed in the output similar to the following:

```text
Currently, the repository softchris/flask-sample has the following open issues:

- docs: add README, CONTRIBUTION, license - Label: documentation
- feature: add requirement.txt to make it easy to install - Label: feature
```

### -3- Working with your workspace

There's another interesting context variable that you can use to get information about your workspace namely `@workspace`

Let's try it out:

```text
@workspace Tell me about this project 
```

You should see an output like this:

```text
This project is a Python Flask-based API for managing an e-commerce system. It provides CRUD (Create, Read, Update, Delete) operations for two main entities: products and carts. Here's an overview of the project:

Files
- api.py:

    Implements the Flask API.
    Contains static data for products and carts.
    Defines routes for CRUD operations on products and carts.
    api_test.py:
    

```

Next, let's add tests using `@workspace /tests`. Run the following prompt:

```text
@workspace /tests
```

This may try to install a test runner but will also generate test and test file for you. Something similar to:

```python file=./code/context/api_test.py
```

If you want, try out `@workspace /explain`, it will explain what your open file is doing.