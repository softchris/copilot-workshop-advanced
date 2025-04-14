---
sidebar_position: 2
---

# Activity: common recipes

We will work through common scenarios in a provided codebase:

- **Generating boilerplate code** (e.g., CRUD operations).
- **Writing tests.**
- **Automating repetitive tasks** (e.g., batch renaming variables) and documentation.

## Generating boilerplate code

In this section, we will quickly create a Web API for an e-commerce application. All we will provide are the names of the entities and hope that Copilot will generate the rest.

Suggested prompts:

- Create a Web API for an e-commerce application with the following entities: `Product`, `Category`, `Order`, `Customer`, `Payment`. Suggest reasonable field names and types for each entity. Use Flask and SQLAlchemy.

Here's some possible outcome:

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="javascript" label="JavaScript" default>

    ```javascript file=./code/boilerplate-js/server.js
    ```

    And you should also get instructions on how to set things up like:

    1. Install required packages

        ```bash
        npm init -y
        npm install express sequelize
        ```

    1. Create the required folder structure

        ```bash
        mkdir models
        ```
    
    1. Copy the code files into their respective locations

    1. Run the server:
    
        ```bash
        node server.js
        ```
         

  </TabItem>
  <TabItem value="python" label="Python">

   ```python file=./code/boilerplate.py
   ```

  </TabItem>
  <TabItem value="csharp" label="C#/.NET">
    
    ```csharp file=./code/boilerplate-dotnet/Program.cs
    ```

    To set up and run this project:

    1. Create a new WebAPI project:

        ```bash
        dotnet new webapi -n ECommerceApi
        ```

    1. Install required packages:

        ```bash
        dotnet add package Microsoft.EntityFrameworkCore.SqlServer
        dotnet add package Microsoft.EntityFrameworkCore.Tools
        ```

    1. Add connection string to appsettings.json:

        ```bash
        {
          "ConnectionStrings": {
            "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=ECommerceDb;Trusted_Connection=True;MultipleActiveResultSets=true"
        }
        ```

    1. Create and apply migrations:

        ```bash
        dotnet ef migrations add InitialCreate
        dotnet ef database update
        ```
    
    1. Run the application:

        ```bash
        dotnet run
        ```


  </TabItem>
</Tabs>

## Writing tests

A huge win with Copilot is that it can generate a lot of tests quickly. However, you should always review the tests and make sure they are correct. Copilot is not perfect and it can generate tests that are not correct or that do not cover all the edge cases.

<Tabs>
  <TabItem value="javascript" label="JavaScript" default>

    Open the file where you store the server code and use the Chat and ask it to generate tests for the API. You can use the following prompt:

    ```text
    Generate tests for this file
    ```

    :::note
    The more context you provide, the better the results. You could specify the the type of test, the framework you want to use, etc. 
    :::
    

    ```javascript file=./code/boilerplate-js/test-server.js
    ```
    
  </TabItem>
  <TabItem value="python" label="Python">

    Open the file where you store the server code and use the Chat and ask it to generate tests for the API. You can use the following prompt:

    ```text
    Generate tests for this file
    ```

    :::note
    The more context you provide, the better the results. You could specify the the type of test, the framework you want to use, etc. 
    :::

   ```python file=./code/test_boilerplate.py
   ```

  </TabItem>
  <TabItem value="csharp" label="C#/.NET">
    
    Open the file where you store the server code and use the Chat and ask it to generate tests for the API. You can use the following prompt:

    :::note
    The more context you provide, the better the results. You could specify the the type of test, the framework you want to use, etc. 
    :::

    ```csharp file=./code/boilerplate-dotnet/ProductControllerTest.cs
    ```

  </TabItem>
</Tabs>


## Automating repetitive tasks

There are some common tasks that you will need to do over and over again. For example, renaming variables, changing the structure of a file, etc. Your IDE can help with renaming variables, but Copilot can help with more complex tasks like adding new fields to a class, changing the structure of a file, etc. Let's try that:

:::note
Have think about the result, what would you change? You're dealing with ORMs, do we need a migration? Do we need to update the database? Do we need to update the API? As you can see, there might be a lot of things to do. Copilot can help with that, but you need to be careful and review the changes.
:::

<Tabs>
  <TabItem value="javascript" label="JavaScript" default>

    Open the file that contains a model, type the following prompt and let Copilot do the rest:

    ```text
   Add fields for create date and updated date and any restrictions you think are necessary. 
    ```

    You should get something like this:

    ```javascript file=./code/boilerplate-js/models/product.js
    ```
    
  </TabItem>
  <TabItem value="python" label="Python">

     Open the file that contains a model, type the following prompt and let Copilot do the rest:

    ```text
    Add fields for create date and updated date and any restrictions you think are necessary. 
    ```

   ```python file=./code/boilerplate-updated.py
   ```

  </TabItem>
  <TabItem value="csharp" label="C#/.NET">
    
     Open the file that contains a model, type the following prompt and let Copilot do the rest:

    ```text
    Add fields for create date and updated date and any restrictions you think are necessary. 
    ```

    ```csharp file=./code/boilerplate-dotnet/Category-updated.cs
    ```

  </TabItem>
</Tabs>