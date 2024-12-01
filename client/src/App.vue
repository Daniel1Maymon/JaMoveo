<template>
  <div id="app">
    <header v-if="showHeader">
      <h1>JaMoveo</h1>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </nav>
    </header>
    <main>
      <!-- Place for more components-->
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    // Determine whether to show the header based on the current route
    showHeader() {
      const hiddenRoutes = ["/player", '/admin']; // Add paths where the header should be hidden
      return !hiddenRoutes.includes(this.$route.path);
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #008080;
  color: white;
  padding: 10px;
  text-align: center;
}

nav {
  margin: 10px 0;
}

nav a {
  margin: 0 10px;
  color: white;
  text-decoration: none;
}

main {
  padding: 10px;
}
</style>
