---
sidebar_position: 2
---

# Activity: Copilot Edits

## -1- Clone the repo

Make sure you have cloned the following repository:

```bash
git clone https://github.com/softchris/flask-sample.git
```

## -2- Refactor

1. Select "Edits" in the chat window dropdown to activate the Edits mode.
1. Type the following prompt:

    ```text
    make the project easier to maintain, divide it up into layers
    ```

    You may need an additional prompt to get the desired results, something like:
    
      ```text
      create the models as classes, also add sample data
      ```

    Here's what you can expect, your `api.py` has now been divided into layers:

    - models.py
    - services.py
    - api.py

## -3- Add a new feature

Add the following prompt:

```text
add Users as a new type
```

This should make changes in the following files:

- models.py
- services.py
- api.py

## -4- Add a frontend

So far, you've been looking at the backend. Now, let's add a frontend to the project. You can use the following prompt:

```text
Add a frontend, use React and TypeScript, add a simple page to show the products. organize in a frontend and backend folder respectively
```

This will take a couple of minutes but will end producing a new folder structure, something like this:

```text
├── backend
│   ├── app.py
|   ├── models.py
│   ├── services.py
│   └── requirements.txt
├── frontend
│   ├── package.json
│   ├── src
│   │   ├── App.tsx
│   │   ├── components
│   │   │   ├── Product.tsx
│   │   │   └── User.tsx
│   │   ├── pages
│   │   │   ├── ProductPage.tsx
│   │   │   └── UserPage.tsx
│   │   └── services
│   │       ├── productService.ts
│   │       └── userService.ts
│   └── tsconfig.json
└── README.md
```

### Tweaks

:::note
You might need to do some small tweaks like adding a way to start the frontend and backend at the same time. You can use `concurrently` for that. 
:::

- Write prompt similar to:

    ```text
    Add a way to start the frontend and backend at the same time, call the script start:all
    ```

### Run the app

:::note
You might also need to add CORS support, to ensure frontend and backend can communicate. 
:::

- Write a prompt similar to:
    
    ```text
    Add CORS support to the backend
    ```

- Start the backend and frontend and check if everything is working as expected. You can use the following commands:

```bash
cd frontend
npm install
npm run start:all
```

:::note
If you run into trouble, use this branch `fullstack` before continuing:

```bash
https://github.com/softchris/flask-sample/tree/fullstack
```

If you wish to continue with your own code then ignore the below commands.
:::

If needed, run the following commands:

```bash
git fetch origin fullstack
git checkout -b fullstack origin/fullstack
```

## -5- Improve the UI


1. Now we will make things look better, you can use the following prompt:

    ```text
    add boostrap to the frontend and udr bootstrap components to show data
    ```

    This should make Copilot add bootstrap to the frontend and change the frontend code to use Boostrap components. 

    You should see an app similar to:

    ![React app](/img/react-app.png)

1. Let's add a top menu and support the other topics like users and carts:

    ```text
    Add a top menu for products, users and carts, there should be components for each topic
    ```

    ![React app with menu](/img/react-app-improved.png)

Here's the branch if you want to check out one possible outcome:

```bash
https://github.com/softchris/flask-sample/tree/fullstack-menu
```

That is, check out the `fullstack-menu` branch:

```bash
git fetch origin fullstack-menu
git checkout -b fullstack-menu origin/fullstack-menu
```