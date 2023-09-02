<template>
  <div class="container mx-auto lg:max-w-lg m-10">
    <h4 class="font-serif font-bold to-blue-800 my-5">Log in</h4>

    <form>
      <div class="mb-6">
        <label
          for="email"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Your email</label
        >
        <input
          type="email"
          id="email"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="name@flowbite.com"
          v-model="email"
          required
        />
      </div>
      <div class="mb-6">
        <label
          for="password"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Your password</label
        >
        <input
          type="password"
          id="password"
          v-model="password"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          required
        />
      </div>
      <div class="flex items-start mb-6">
        <div class="flex items-center h-5">
          <input
            id="remember"
            type="checkbox"
            value=""
            class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800"
            required
          />
        </div>
        <label
          for="remember"
          class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
          >Remember me</label
        >
      </div>
      <button
        type="submit"
        @click="login"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        // Retrieve email and password from data properties
        let { email, password } = this;

        // Construct the URL with query parameters
        const url = `http://127.0.0.1:8000/api/users/username/${email}`;

        // Send a GET request to the server
        const response = await axios.get(url);

        // Check if the response indicates successful authentication
        if (response.status === 200) {
          // Store user data in sessionStorage
        //   console.log(response.data);
          if (response.data.password === password)
            sessionStorage.setItem("user_id", JSON.stringify(response.data));

          this.email = "";
          this.password = "";
          this.$router.push("/");
          // Redirect the user or perform other actions as needed
          // For example, you can use Vue Router to navigate to a different page.
        } else {
          // Handle authentication failure
          alert("Login failed. Please check your credentials.");
        }
      } catch (error) {
        console.error("Error:", error);
        // Handle any errors that occur during the request
      }
    },
  },
};
</script>
