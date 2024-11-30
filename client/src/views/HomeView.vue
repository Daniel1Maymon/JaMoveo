<template>
  <div>
    <h2>Welcome to JaMoveo</h2>
    <ul>
      <li v-for="song in songs" :key="song.id">
        {{ song.title }} by {{ song.artist }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      songs: [],
    };
  },
  async mounted() {
    const response = await fetch("http://127.0.0.1:5000/song/songs");
    this.songs = await response.json();
  },
};
</script>

<style>
ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 10px 0;
}
</style>
