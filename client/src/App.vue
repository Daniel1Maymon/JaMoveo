<template>
  <div id="app">
    <header>
      <h1>JaMoveo</h1>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
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
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #42b983;
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
  padding: 20px;
}
</style>
