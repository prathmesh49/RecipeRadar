<template>
  <div class="container mx-auto xl:max-w-xl m-10">
    <h1
      class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
    >
      Cooking Chronicles:
      <span
        class="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600"
        >Submit Your Recipe</span
      >
    </h1>
    <p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
      Outline the format you'd like users to follow when submitting a recipe.
      Mention details such as ingredient lists, cooking instructions, and
      optional photos.
    </p>
  </div>

  <div class="container mx-auto lg:max-w-lg m-10">
    <div class="my-4">
      <label
        for="small-input"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Title</label
      >
      <input
        type="text"
        id="small-input"
        v-model="title"
        class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
    <div>
      <label
        for="small-input"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Ingredients
        <label class="text-xs">( add ingredients by "," saperated )</label></label
      >
      <input
        type="text"
        id="small-input"
        v-model="ingredients"
        class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
    <div>
      <label
        for="message"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Instructions</label
      >
      <textarea
        id="message"
        rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Write your thoughts here..."
        v-model="instructions"
      ></textarea>
    </div>
    <div>
      <label
        for="small-input"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Cuisine</label
      >
      <input
        type="text"
        id="small-input"
        v-model="cuisine"
        class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
    <div>
      <label
        for="small-input"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Category</label
      >
      <input
        type="text"
        id="small-input"
        v-model="category"
        class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
    <div>
      <label
        for="small-input"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Image</label
      >
      <input
        type="text"
        id="small-input"
        v-model="image"
        class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
    <button
      type="button"
      @click="submitRecipe"
      class="text-white my-3 bg-orange-500 hover:bg-orange-400 focus:ring-4 focus:outline-none focus:ring-[#3b5998]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#3b5998]/55 mr-2 mb-2"
    >
      <path
        fill-rule="evenodd"
        d="M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z"
        clip-rule="evenodd"
      />

      Post
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // Define data properties for form fields
      title: "",
      ingredients: "",
      instructions: "",
      cuisine: "",
      category: "",
      image: "",
    };
  },
  methods: {
    async submitRecipe() {
      try {
        if (
          this.title === "" ||
          this.ingredients === "" ||
          this.instructions === "" ||
          this.cuisine == "" ||
          this.category == "" ||
          this.image == ""
        ) {
          alert("details should not be empty");
        }
        let user_id = "";
        let udata = JSON.parse(sessionStorage.getItem("user_id"));
        console.log(udata);
        if (udata === "") {
          alert("please login first");
          return;
        } else {
          user_id = udata.url;
        }
        // Create an object with the recipe data
        const data = {
          title: this.title,
          ingredients: this.ingredients.split(", "), // Split ingredients into an array
          instructions: this.instructions,
          cuisine: this.cuisine,
          category: this.category,
          image: this.image,
          UserProfile: user_id,
        };

        // Make a POST request using Axios
        const response = await axios.post(
          "http://127.0.0.1:8000/api/recipes/",
          data
        );

        // Handle success response here
        console.log("Recipe saved:", response.data);
        alert("recipe saved!");
        // Clear the form fields
        this.title = "";
        this.ingredients = "";
        this.instructions = "";
        this.cuisine = "";
        this.category = "";
        this.image = "";
      } catch (error) {
        // Handle error response here
        console.error("Error:", error);
      }
    },
  },
};
</script>
