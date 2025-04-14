---
sidebar_position: 4
---

# Activity: Use chat variables `#`

Chat variables are a powerful way to interact with Copilot. They act like tools to carry out specific tasks.

## Scenario: Let's keep working on our sample project

If you haven't done it already, clone the following repo:

```bash
git clone https://github.com/softchris/flask-sample.git
```

### -1- Ask about a specific file

Let's ask Copilot about a specific file. For example, let's ask about the `app.py` file:

```text
tell me about #codebase api.py
```

You should see an output like this:

```text file=./code/chat/codebase.md
```

### -2- Do a change in the workspace

Let's say you've done a change in the workspace and you want to know what files have changed so you know what to commit. You can use the following prompt:

```text
#changes
```

If you've added to the products list, you should see an output like this:

```text
The api.py file has been updated with additional static data for products. Specifically, the following products were added:

Tablet
Headphones
Smartwatch
Charger
Mouse
Keyboard
Monitor
Printer
Let me know if you need further assistance!
```

### -3- Ask about a specific file

If you're interested in a specific file, like if it has this or that feature, or if you just want to know what it does, you can use the following prompt:

```text
#file: LICENSE
```

You should see an output like this:

```text
The LICENSE file contains the MIT License, which is a permissive open-source license. It allows anyone to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, as long as the original copyright notice and permission notice are included in all copies or substantial portions of the software.

The license also states that the software is provided "as is," without any warranty of any kind, and the authors are not liable for any claims, damages, or other liabilities arising from its use.
```

### -4- Bringing in extra context

Imagine a situation where you need code to be generated based on a specific context. Your company for example, might have placed a style guide at a specific URL and you would like it so that Copilot can look at that URL and generate code based on that.  

Or maybe you saw an interesting article but you don't have time to read it but still want to know the most important parts of it. You can use the `#fetch` variable to fetch the content of a URL and use it as context for Copilot. For example:

```text
what are some practices to avoid according to #fetch https://docs.python-guide.org/writing/style/
```

It will now ask for your permission before fetching the content of the URL. If you allow it, it will fetch the content and use it as context. Here's a sample output:

```markdown file=./code/chat/fetch.md
```