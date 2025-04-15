---
sidebar_position: 1
---

# Custom instructions for GitHub Copilot

The idea with custom instructions is that you provide instructions to GitHub Copilot to help it understand your preferences and the context of your project. This can help improve the quality of the code suggestions you receive.

Imagine you instruct Copilot on the following:

- Code style: Do you prefer functional programming, object-oriented programming, or a specific framework?
- Project context: What is the purpose of your project? What are the main features or functionalities?
- Preferred libraries: Are there any specific libraries or tools you want to use in your project?
- Code quality: Do you have any specific coding standards or best practices you want to follow?

You get the idea. The more context you provide, the better Copilot can tailor its suggestions to your needs.  

So how do you set up custom instructions?

## Setting up custom instructions

- **Create a copilot-instructions.md file** in .github directory of your repository. Here's an example:

```markdown
- Start all variables with underscore
- Use camelCase for function names
- Add the text "AI generated code" right above the code block.
```


- **Add entries to your settings**. Here you can both add instructions straight into the settings file or point out a file with instructions.