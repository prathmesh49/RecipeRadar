<template>
  <nav
    class="bg-orange-500 dark:bg-gray-900 fixed w-full z-10 top-0 left-0 border-b border-gray-200 dark:border-gray-600"
  >
    <div
      class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-0"
    >
      <a class="flex items-center">
        <router-link to="/">
          <img
            src="../public/img/icons/FlavorFusionbg.png"
            class="h-8 mr-3"
            alt="Flowbite Logo"
          />
        </router-link>
      </a>
      <div class="flex md:order-2">
        <button
          data-collapse-toggle="navbar-sticky"
          type="button"
          class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-sticky"
          aria-expanded="false"
        >
          <span class="sr-only">Open main menu</span>
          <svg
            class="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button>
      </div>
      <div
        class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
        id="navbar-sticky"
      >
        <ul
          class="flex flex-col md:p-0 mt-4 md:flex-row md:space-x-8 md:mt-0 md:border-0 bg-orange-500"
        >
          <li>
            <p
              class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:underline underline-offset-4 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
            >
              <router-link to="/">Home</router-link>
            </p>
          </li>
          <li>
            <p
              class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:underline underline-offset-4 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
            >
              <router-link to="/about">Add Recipe</router-link>
            </p>
          </li>
          <li>
            <a
              href="#"
              class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:underline underline-offset-4 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
              >Services</a
            >
          </li>
          <li>
            <a
              href="#"
              class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:underline underline-offset-4 md:p-0 md:dark:hover:underline dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
              ><router-link to="/login">Log in</router-link></a
            >
          </li>
          <li>
            <a
              href="#"
              class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:underline underline-offset-4 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
            >
              <router-link to="/register">Sign Up</router-link></a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="pdt-40">
    <router-view />
  </div>
  <Footer msg="" />
</template>
<script setup>
import Footer from "./views/Footer.vue";
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // color: #2c3e50;
}
.pdt-40 {
  padding-top: 80px;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    // color: #2c3e50;

    &.router-link-exact-active {
      text-decoration: underline;
      text-underline-offset: 5px;
    }
  }
}
</style>
