<template>
  <div class="home-container">
    <h2>Welcome to JaMoveo</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      songs: [],
    };
  },
  // async mounted() {
  //   const response = await fetch("http://127.0.0.1:5000/song/songs");
  //   this.songs = await response.json();
  // },
};
</script>

<style>

.home-container {
  margin-top: 20px;
  text-align: center; 
}


h2 {
  font-size: 24px;
  color: black;
  margin: 0;
}
</style>
