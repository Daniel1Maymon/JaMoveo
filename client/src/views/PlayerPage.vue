<template>
  <div>
    <header>
      <h1>Player Page</h1>
    </header>
    <main>
      <div v-if="!isLive" class="waiting-message">
        <h2>Waiting for next song</h2>
      </div>
      <div v-else class="song-details">
        <h2>{{ song.title }}</h2>
        <p><strong>Artist:</strong> {{ song.artist }}</p>
        <div v-if="instrument === 'singer'" class="lyrics">
          <h3>Lyrics</h3>
          <p>{{ song.lyrics }}</p>
        </div>
        <div v-else class="chords-and-lyrics">
          <h3>Chords</h3>
          <pre>{{ song.chords }}</pre>
          <h3>Lyrics</h3>
          <p>{{ song.lyrics }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "PlayerPage",
  data() {
    return {
      isLive: false, // Indicates if a song is selected
      song: {
        title: "",
        artist: "",
        lyrics: "",
        chords: "",
      },
      instrument: localStorage.getItem("instrument") || "player", // Default to player
    };
  },
  methods: {
    updateSong(songData) {
      this.song = songData;
      this.isLive = true;
    },
    reset() {
      this.song = { title: "", artist: "", lyrics: "", chords: "" };
      this.isLive = false;
    },
  },
  created() {
    // Simulating socket connection for live updates
    const socket = new WebSocket("ws://127.0.0.1:5000");
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === "song_selected") {
        this.updateSong(data.song);
      } else if (data.type === "reset") {
        this.reset();
      }
    };
  },
};
</script>

<style scoped>
.waiting-message {
  text-align: center;
  margin-top: 50px;
}

.song-details {
  margin: 20px auto;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.song-details h2 {
  color: #008080;
}

.lyrics,
.chords-and-lyrics {
  margin-top: 20px;
}

pre {
  background: #f0f0f0;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
</style>
