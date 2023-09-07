<template>
  <div class="container mx-auto 2xl:max-w-5xl grid 2xl:grid-cols-3 gap-5 p-4 sm:grid-cols-2 py5">
    
    <div
      class="w-full max-w-sm bg-white border-gray-200 rounded-lg"
      v-for="el in data"
    >
      <a href="#">
        <img
          class="rounded-t-lg h-3/5 w-full"
          :src="el.image"
          alt="product image"
        />
      </a>
      <div class="px-5 pb-5 mt-2">
        <router-link to="/recipe">
          <a href="#" @click="saveToSessionStorage(el)">
            <h5
              class="text-xl font-semibold tracking-tight text-gray-900 dark:text-white hover:underline decoration-orange-500"
            >
              {{ el.title }}
            </h5>
          </a>
        </router-link>

        <div class="flex items-center mt-2.5 mb-5">
          <svg
            class="w-4 h-4 text-yellow-300 mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
          <svg
            class="w-4 h-4 text-yellow-300 mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
          <svg
            class="w-4 h-4 text-yellow-300 mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
          <svg
            class="w-4 h-4 text-yellow-300 mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
          <svg
            class="w-4 h-4 text-gray-200 dark:text-gray-600"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
          <span
            class="bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 ml-3"
            >5.0</span
          >
        </div>
        <div class="flex items-center justify-between">
          <span class="text-3xl font-bold text-gray-900 dark:text-white">{{
            el.cuisine
          }}</span>
          <a
            href="#"
            class="text-white or hover:bg-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >save</a
          >
        </div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";
import { ref, onBeforeMount } from "vue";
export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
  setup() {
    // Define your method
    let data = ref([]);

    onBeforeMount(async () => {
      try {
        // Retrieve email and password from data properties

        // Construct the URL with query parameters
        const url = `http://127.0.0.1:8000/api/recipes/`;

        // Send a GET request to the server
        let response = await axios.get(url);

        // Check if the response indicates successful authentication
        if (response.status === 200) {
          data.value = response.data;
          console.log(data);
        } else {
          // Handle authentication failure
          alert("Login failed. Please check your credentials.");
        }
      } catch (error) {
        console.error("Error:", error);
        // Handle any errors that occur during the request
      }
    });

    function saveToSessionStorage(item) {
      // Save the clicked item in session storage
      sessionStorage.setItem("clickedItem", JSON.stringify(item));
    }

    return {
      data,
      saveToSessionStorage,
    };
  },
};
</script>

<style scoped lang="scss">
.or {
  background-color: #f15025;
}
</style>
