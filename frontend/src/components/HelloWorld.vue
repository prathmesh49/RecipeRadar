<template>
  <div class="container mx-auto 2xl:max-w-4xl py-4 pl-3">
    <nav class="flex" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li class="inline-flex items-center">
          <a
            href="#"
            class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white"
          >
            <svg
              class="w-3 h-3 mr-2.5"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"
              />
            </svg>
            Home
          </a>
        </li>
        <li>
          <div class="flex items-center">
            <svg
              class="w-3 h-3 text-gray-400 mx-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 6 10"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 9 4-4-4-4"
              />
            </svg>
            <a
              href="#"
              class="ml-1 text-sm font-medium text-gray-700 hover:text-blue-600 md:ml-2 dark:text-gray-400 dark:hover:text-white"
              >Recipe</a
            >
          </div>
        </li>
      </ol>
    </nav>

    <h1
      class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
    >
      {{ data.title }}
    </h1>
    <p class="mb-6 text-sm text-gray-400 md:text-sm dark:text-gray-400">
      Recipe by <span class="text-black">{{ user }}</span
      >, Updated on {{ myDate }}
    </p>

    <img
      class="h-auto max-w-lg rounded-lg mb-5"
      :src="data.image"
      alt="image description"
    />

    <h5 class="text-xl font-bold dark:text-white mb-5">Direction</h5>

    <p
      class="mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400 2xl:pr-32 xl:pr-32 lg:pr-32"
    >
      {{ data.instructions }}
    </p>

    <h2 class="text-xl font-bold dark:text-white mb-5">Ingredients</h2>
    <ul
      class="max-w-md font-normal text-lg space-y-1 text-gray-500 list-disc list-inside dark:text-gray-400"
    >
      <li v-for="item in data.ingredients" class="block">{{ item }}</li>
    </ul>
    <div class="container mx-auto xl:max-w-xl py-4 pl-3 mt-5">
      <div class="flex items-center mb-4">
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
          class="w-4 h-4 text-gray-300 mr-1 dark:text-gray-500"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 22 20"
        >
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
          />
        </svg>
        <!-- <p class="ml-2 text-sm font-medium text-gray-500 dark:text-gray-400">
          0 to 5
        </p> -->
      </div>
      <div class="relative">
        <input
          type="text"
          id="floating_outlined"
          class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder="0 to 5"
          v-model="rating"
        />
      </div>

      <form @submit.prevent="onSubmit">
        <div
          class="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600"
        >
          <div class="px-4 py-2 bg-white rounded-t-lg dark:bg-gray-800">
            <label for="comment" class="sr-only">Your comment</label>
            <textarea
              id="comment"
              rows="4"
              class="w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400"
              placeholder="Write a comment..."
              v-model="comment"
              required
            ></textarea>
          </div>
          <div
            class="flex items-center justify-between px-3 py-2 border-t dark:border-gray-600"
          >
            <button
              @click="saveCommit"
              class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-orange-500 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800"
            >
              Post comment
            </button>

            <div class="flex pl-0 space-x-1 sm:pl-2">
              <button
                type="button"
                class="inline-flex justify-center items-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
              >
                <svg
                  class="w-4 h-4"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 12 20"
                >
                  <path
                    stroke="currentColor"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M1 6v8a5 5 0 1 0 10 0V4.5a3.5 3.5 0 1 0-7 0V13a2 2 0 0 0 4 0V6"
                  />
                </svg>
                <span class="sr-only">Attach file</span>
              </button>
              <button
                type="button"
                class="inline-flex justify-center items-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
              >
                <svg
                  class="w-4 h-4"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 16 20"
                >
                  <path
                    d="M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"
                  />
                </svg>
                <span class="sr-only">Set location</span>
              </button>
              <button
                type="button"
                class="inline-flex justify-center items-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
              >
                <svg
                  class="w-4 h-4"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 18"
                >
                  <path
                    d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z"
                  />
                </svg>
                <span class="sr-only">Upload image</span>
              </button>
            </div>
          </div>
        </div>
      </form>
      <p class="ml-auto text-xs text-gray-500 dark:text-gray-400">
        Remember, contributions to this topic should follow our
        <a href="#" class="text-blue-600 dark:text-blue-500 hover:underline"
          >Community Guidelines</a
        >.
      </p>

      <figure class="max-w-screen-md mt-3" v-for="el in reviews_data">
        <div class="flex items-center mb-4 text-yellow-300">
          <svg
            class="w-5 h-5 mr-1"
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
            class="w-5 h-5 mr-1"
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
            class="w-5 h-5 mr-1"
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
            class="w-5 h-5 mr-1"
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
            class="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path
              d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
            />
          </svg>
        </div>
        <blockquote>
          <p class="text-2xl font-semibold text-gray-900 dark:text-white">
            {{ el.comment }}
          </p>
        </blockquote>
        <figcaption class="flex items-center mt-6 space-x-3">
          <img
            class="w-6 h-6 rounded-full"
            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png"
            alt="profile picture"
          />
          <div
            class="flex items-center divide-x-2 divide-gray-300 dark:divide-gray-700"
          >
            <cite class="pr-3 font-medium text-gray-900 dark:text-white">{{
              el.date_created
            }}</cite>
            <cite class="pl-3 text-sm text-gray-500 dark:text-gray-400">{{
              el.rating
            }}</cite>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</template>

<script>
import { ref, onBeforeMount } from "vue";
import axios from "axios";
import router from "@/router";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  setup() {
    const data = ref({});
    const myDate = ref("");
    const user = ref("");
    let rating = ref("");
    let comment = ref("");
    let reviews_data = ref([]);

    onBeforeMount(async () => {
      data.value = JSON.parse(sessionStorage.getItem("clickedItem"));
      const dateObj = new Date(data.value.created_date);
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      const month = monthNames[dateObj.getUTCMonth()];
      const day = dateObj.getUTCDate();
      const year = dateObj.getUTCFullYear();
      myDate.value = `${month} ${day}, ${year}`;
      render_reviews();
      const userProfileUrl = data.value.UserProfile;
      try {
        const response = await axios.get(userProfileUrl);
        if (response.status === 200) {
          user.value = response.data.name;
        } else {
          alert("Failed to fetch user data. Please check your credentials.");
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while fetching user data.");
      }
    });

    const saveCommit = async () => {
      const url = `http://127.0.0.1:8000/api/reviews/`;
      let valid_num = parseInt(rating.value);
      let user_data = JSON.parse(sessionStorage.getItem("user_id"));
      console.log(user_data);
      if (user_data === null || user_data === undefined) {
        alert("please login first ");
        router.push('login');
        return;
      }

      if (isNaN(valid_num) || valid_num > 5 || valid_num < 0) {
        alert("Please provide a rating between 0 and 5.");
        clear_commit();
        return;
      }

      const scdata = {
        recipe: data.value.url,
        user: data.value.UserProfile,
        rating: valid_num,
        comment: comment.value,
      };

      try {
        const response = await axios.post(url, scdata);
        if (response.status === 200 || response.status === 201) {
          clear_commit();
        } else {
          alert("Failed to save the review. Please try again later.");
          clear_commit();
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while saving the review.");
        clear_commit();
      }
    };

    const clear_commit = () => {
      rating.value = "";
      comment.value = "";
      render_reviews();
    };
    const render_reviews = async () => {
      let arr = data.value.url.split("");
      let n = arr.length;
      let recipe = arr[n - 2];
      console.log(recipe);
      let url = `http://127.0.0.1:8000/api/reviews/recipe/${recipe}/`;
      if (!url) return;
      try {
        const response = await axios.get(url);
        if (response.status === 200) {
          console.log(response.data);
          reviews_data.value = response.data;
        } else {
          alert("Failed to fetch user data. Please check your credentials.");
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while fetching reviews data.");
      }
    };

    return {
      data,
      myDate,
      user,
      rating,
      comment,
      saveCommit,
      reviews_data,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
