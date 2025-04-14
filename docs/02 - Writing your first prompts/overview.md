---
sidebar_position: 1
---

# Overview of GitHub Copilot and its features

The full list of all its features can be found [here](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features).

Let's try to summarize the most important ones. Let's think of it in terms of modalities:

- **Inline**, this is the most common way to use Copilot. It will suggest code as you type, and you can accept or reject it. You can also trigger an inline menu with `Ctrl + Insert` (or `Cmd + I` on Mac) to see more suggestions. This is the default mode of Copilot.

  ![GitHub Copilot inline mode](/img/ghcp-inline.png)

- **Chat**, this is a more conversational way to interact with Copilot. You can ask it questions and get answers in a chat-like interface. This is similar to how you would interact with a chatbot. You can also use it to generate code snippets or ask for explanations of code.

    ![GitHub Copilot Chat](/img/ghcp-chat.png)

    Within the chat interface, you can switch between different modes:

    ![Chat modes](/img/ghcp-chat-modes.png)

   - **Ask**, this is a way to ask Copilot questions and get answers. You can also have code snippets generated for you. 
   - **Edits**, this is a way to ask Copilot to make changes to your code and it can change multiple lines of code at once. Great for refactoring or making large changes to your code. - - **Agent**, this mode allows you to ask Copilot to do heavy lifting for you like running tasks, installing libraries, or even deploying your code. 

- **Terminal**, this is a way to interact with Copilot in the terminal. You can use it to run commands or ask for help with command-line tasks. Here's an example of how to use it in the terminal:

    ![GitHub Copilot terminal](/img/ghcp-terminal.png)

- `@` typing `@` in the chat will bring up a list of commands that you can use to interact with Copilot. The nature of these commands is what you're speaking to like `azure` or the terminal. By using `@` you narrow down the context of what you want done.

    ![At commands](/img/ghcp-at.png)

- **Chat variables**, these type of commands act like tools, you can for example bring in an external URL or a file from your local machine to ensure that's treated as valuable context and much more. 