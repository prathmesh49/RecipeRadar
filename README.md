# Flavor Fusion - Personalized Recipe Recommendation Platform

## Introduction

Flavor Fusion is a revolutionary recipe recommendation platform that empowers users to discover new recipes, tailor recommendations to their tastes, and engage with a vibrant food-loving community. This README provides an overview of the project, its key features, and how to get started.

## Deployed App

[Flavor Fusion - Live Demo](2flavorfusion.netlify.app/)

## Video Walkthrough

[Watch Video Walkthrough](https://drive.google.com/drive/folders/1c4UwAENnihLLbOGFYz8VXc3orJcL3ars?usp=drive_link)

## Features

Flavor Fusion offers a range of features, including:

- **Personalized Recipe Recommendations**: Utilizes machine learning algorithms to analyze user profiles, ingredient preferences, and cooking behaviors to provide personalized recipe recommendations.

- **Recipe Discovery & Collection**: Allows users to explore a diverse collection of recipes based on cuisines, dietary preferences, and ingredients. Users can save recipes to their collections for easy access.

- **Community Interaction**: Fosters engagement through a community forum where users can connect, share cooking experiences, exchange culinary insights, and discuss recipes with like-minded individuals.

- **Ingredient Substitutions**: Suggests ingredient substitutions based on user preferences and dietary restrictions, making recipes more adaptable to individual needs.

- **User Ratings & Reviews**: Enables users to rate and review recipes they've tried, adding credibility to recipes and helping others make informed choices.

- **Culinary Profiles**: Allows users to create detailed culinary profiles, specifying flavor preferences, cooking techniques, and dietary restrictions. This information enhances the accuracy of recipe recommendations.

- **Recipe Sharing**: Enables users to share their favorite recipes with others, either within the community or on social media platforms, fostering knowledge sharing and engagement.

## Design Decisions & Assumptions

![database-diagram](https://github.com/prathmesh49/RecipeRadar/assets/112652930/b7a0afdf-6f4d-4f4b-95a7-c7c62f7413d1)

## Installation & Getting Started

Get Flavor Fusion up and running on your local machine with these simple steps:

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Node.js**: Make sure you have Node.js installed on your computer. You can download it from [nodejs.org](https://nodejs.org/).

- **Vue CLI**: Flavor Fusion uses Vue.js as its frontend framework. Install the Vue CLI globally using npm:
  
  ```bash
  npm install -g @vue/cli

### Clone the Repository
Start by cloning the Flavor Fusion repository to your local machine:

   ```bash
  git clone https://github.com/your-username/FlavorFusion.git
  cd FlavorFusion
  ```

### Frontend Setup
Navigate to the frontend directory:

    cd frontend
    
### Install frontend dependencies:

    npm install

### Start the development server:

    npm run serve

The frontend server will start, and you can access the application at http://localhost:8080 in your web browser.

### Backend Setup
Navigate back to the root directory of Flavor Fusion:

    cd flavorfusion/backend/

You need to set up the backend using Django. Make sure you have Python and Django installed on your system.

### Install Python dependencies:

    pip install -r requirements.txt

### Migrate the database:

    python manage.py migrate

### Start the Django development server:

    python manage.py runserver
The backend server will start and run at http://localhost:8000.

Access the admin panel to manage data (optional):

Open your web browser and go to http://localhost:8000/admin/.
Log in with the superuser credentials you created earlier.
Now you have Flavor Fusion up and running locally! You can access the application at http://localhost:8080 in your web browser and start exploring, creating, and connecting with the culinary community.

Enjoy your personalized cooking journey with Flavor Fusion!

## Usage

Flavor Fusion is designed to make your culinary experience delightful and personalized. Here's how to make the most out of it:

### 1. User Profile Setup

- **Create an Account**: If you're a new user, start by creating an account. Provide basic information and preferences to personalize your Flavor Fusion experience.

- **Update Your Culinary Profile**: Navigate to your profile settings to specify your flavor preferences, dietary restrictions, and favorite cuisines. This information helps us recommend recipes tailored to your taste.

### 2. Discover and Save Recipes

- **Explore Recipes**: Browse through our extensive collection of recipes. You can explore by cuisine, dietary preferences, or ingredients.

- **Personalized Recommendations**: Check out the personalized recipe recommendations on your dashboard. These are based on your culinary profile and past interactions.

- **Save Recipes**: When you find a recipe you love, save it to your collection for easy access. Just click the "Save" button on the recipe card.

### 3. Community Interaction

- **Join the Foodie Community**: Engage with fellow food enthusiasts on our community forum. Share your cooking experiences, exchange tips, and discover culinary insights.

- **Rate and Review**: If you try a recipe, don't forget to rate it and leave a review. Your feedback helps others make informed choices.

- **Share Your Creations**: Share your favorite recipes, cooking tips, and modifications with the community. It's a great way to connect with others who share your passion.

### 4. Practical Tools

- **Ingredient Substitutions**: If you have dietary restrictions or are missing an ingredient, use our ingredient substitution feature to adapt recipes to your needs.

- **Meal Planner**: Plan your meals for the week using our interactive meal planner. Select recipes and generate a shopping list to streamline your cooking.

### 5. AI-Powered Meal Suggestions (Optional)

- **AI Meal Suggestions**: For an enhanced experience, enable our AI-driven meal suggestion feature. It recommends complete meal plans based on your preferences and available ingredients.

With Flavor Fusion, you're in control of your culinary journey. Explore, create, and connect with a community of food lovers. Get started today and savor the flavor of personalized cooking!



## API Endpoints

    In the backend, Flavor Fusion provides the following API endpoints:

    GET /api/users: Retrieve all users.
    GET /api/recipes: Retrieve all recipes.
    GET /api/reviews: Retrieve all reviews.
    GET /api/savedrecipes: Retrieve all Saved Recipes.
    POST /api/users: Create a new users.
    POST /api/recipes: Create a new recipe.
    POST /api/reviews: Create a new reviews.
    POST /api/savedrecipes: Create a new Recipes.
    DELETE /api/users: Create a new users.
    DELETE /api/recipes: Create a new recipe.
    DELETE /api/reviews: Create a new reviews.
    DELETE /api/savedrecipes: Create a new Recipes.
    PUT /api/users: Create a new users.
    PUT /api/recipes: Create a new recipe.
    PUT /api/reviews: Create a new reviews.
    PUT /api/savedrecipes: Create a new Recipes.

## Technology Stack

    Flavor Fusion is built using the following technologies:

    Front-end: Vue.js
    Back-end: Django
    Database: MongoDB (Atlas)
    
