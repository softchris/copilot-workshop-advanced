---
sidebar_position: 5
---

# Activity: Use slash commands

Slash commands can be seen as commands doing valuable things for you. There are typically two types of them:

- **Prompt type**: These are commands you can use instead of writing a prompt. For example:
  - `/docs`: Generate documentation comments for all or only the selected methods and functions in the editor.
  - `/fix`: Ask Copilot for suggestions on how to fix a block of code or how to resolve any compiler or linting errors in your code. For example, to help fix unresolved Node.js package names.
  - `/tests`: Generate tests for all or only the selected methods and functions in the editor. The generated tests are appended in an existing tests file or a new tests file is created.
- **Scaffolding type**. These commands create new files or folders in your workspace. For example:
  - `/new`: Use the `/new` command in the Chat view to scaffold a new project or a new file. Use natural language to describe the type of project/file you need, and preview the scaffolded content before creating it. Example: `/new Express app using typescript and svelte`.
  - `newNotebook`: Use the `/newNotebook` command in the Chat view to generate a new Jupyter notebook based on your requirements. Use natural language to describe what the notebook should contain. Example: `/newNotebook get census data and preview key insights with Seaborn`.

## -1- Creating a new project

Let's say you want to create a completely new project and you have an idea for framework and language. You can use the `/new` command to create a new project. For example, you can use the following prompt:

```text
/new React app, need a crud app with a backend in Node.js and a frontend in React. Use TypeScript for both the backend and frontend. App should manage products, carts and users.
```

You should see a proposed structure for both backend and frontend and you're asked to create said workspace.

```text
├── backend
│   ├── src
│   │   ├── app.ts
│   │   ├── controllers
│   │   │   ├── cartController.ts
│   │   │   ├── productController.ts
│   │   │   └── userController.ts
│   │   ├── models
│   │   │   ├── cartModel.ts
│   │   │   ├── productModel.ts
│   │   │   └── userModel.ts
│   │   ├── routes
│   │   │   ├── cartRoutes.ts
│   │   │   ├── productRoutes.ts
│   │   │   └── userRoutes.ts
│   │   └── types
│   │       └── index.ts
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── Cart.tsx
│   │   │   ├── Product.tsx
│   │   │   └── User.tsx
│   │   ├── pages
│   │   │   ├── CartPage.tsx
│   │   │   ├── ProductPage.tsx
│   │   │   └── UserPage.tsx
│   │   ├── services
│   │   │   ├── cartService.ts
│   │   │   ├── productService.ts
│   │   │   └── userService.ts
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── types
│   │       └── index.ts
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── README.md
```

## -2- Inspect your workspace

Now that you've created a new project, let's see what was actually created. You can use the `/explain` command like so:

```text
@workspace /explain
```

You should see response explaining the various parts of the project.

You could even ask it specific questions on things like:

- what do I need to do to setup the database and tell me more about the database?
- Tell me how to run the project