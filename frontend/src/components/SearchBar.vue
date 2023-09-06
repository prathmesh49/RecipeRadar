<template>
  <form @submit.prevent="onsubmit">
    <label
      for="default-search"
      class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
      >Search</label
    >
    <div class="relative">
      <div
        class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
      >
        <svg
          class="w-4 h-4 text-gray-500 dark:text-gray-400"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 20 20"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
          />
        </svg>
      </div>
      <input
        v-model="searchQuery"
        type="text"
        id="default-search"
        class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Search Mockups, Logos..."
        required
      />
      <div
        v-if="showDropdown"
        class="absolute z-10 mt-2 bg-white border border-gray-300 rounded-lg shadow-lg max-h-40 overflow-y-auto"
      >
        <ul class="p-2">
          <li v-for="result in searchResults" :key="result.id">
            <!-- Display each search result here -->

            <p @click="saveToSessionStorage(result)">{{ result.title }}</p>
          </li>
        </ul>
      </div>
    </div>
  </form>
</template>

<script>
import { ref, watch } from "vue"; // Import the watch function
import { debounce } from "lodash"; // Import the debounce function'
import axios from "axios";
import router from "@/router";

export default {
  setup() {
    const searchQuery = ref("");
    const debouncedSearch = debounce(searchRecipes, 1000); // Adjust the delay as needed
    const showDropdown = ref(false); // Variable to control the visibility of the dropdown
    const searchResults = ref([]);

    async function searchRecipes() {
      // Your API request logic here
      console.log("Searching for recipes:", searchQuery.value);
      if (searchQuery.value === "") {
        // Clear the results and hide the dropdown when the search query is empty
        searchResults.value = [];
        showDropdown.value = false;
        return;
      }
      const apiUrl = `http://127.0.0.1:8000/api/recipe/search/?query=${searchQuery.value}`;
      //   http://127.0.0.1:8000/api/recipe/search/?query=crockpot
      try {
        const response = await axios.get(apiUrl);
        if (response.status === 200) {
          // Handle the successful response, which contains the search results
          console.log("Search results:", response.data);
          searchResults.value = response.data; // Store the search results
          showDropdown.value = true; //
        } else {
          // Handle other response statuses if needed
        }
      } catch (error) {
        // Handle any errors that occur during the request
        console.error("Error searching recipes:", error);
      }
    }
    function saveToSessionStorage(item) {
      // Save the clicked item in session storage
      sessionStorage.setItem("clickedItem", JSON.stringify(item));
      router.push("recipe");
      showDropdown.value = false;
      searchQuery.value = "";
    }

    // Watch for changes in the searchQuery and debounce the search
    watch(searchQuery, () => {
      debouncedSearch();
    });

    return {
      searchQuery,
      showDropdown,
      searchResults,
      saveToSessionStorage,
    };
  },
};
</script>
