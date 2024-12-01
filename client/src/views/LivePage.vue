<template>
  <div class="live-container">
    <h1>Now Playing</h1>
    <!-- <p><strong>Song ID:</strong> {{ songId }}</p>
    <p><strong>Title:</strong> {{ songTitle }}</p> -->

    <div class="song-lyrics">
      <!-- Iterate over the lines of the song -->
      <div v-for="(lineGroup, index) in songContent" :key="index" class="song-line-group">
        <!-- Display chords on one line -->
        <div class="song-line">
          <span v-for="(word, wordIndex) in lineGroup" :key="wordIndex" class="chords">
            {{ word.chords ? word.chords : '' }}
          </span>
        </div>
        <!-- Display lyrics on the next line -->
        <div class="song-line">
          <span v-for="(word, wordIndex) in lineGroup" :key="wordIndex" class="lyrics">
            {{ word.lyrics }}
          </span>
        </div>
      </div>
    </div>

    <!-- Add a floating button to control auto-scrolling -->
    <button class="scroll-toggle">Start/Stop Scrolling</button>

    <!-- Add a quit button for the admin -->
    <button class="quit-button">Quit</button>
  </div>
</template>

<script>
export default {
  name: "LivePage",
  data() {
    return {
      songId: null,
      songTitle: "",
      songContent: [], // Will be populated from the API response
    };
  },
  mounted() {
    const songData = localStorage.getItem("songData");
    const token = localStorage.getItem("access_token"); // Retrieve the token from localStorage

    if (songData && token) {
      const parsedSongData = JSON.parse(songData);
      this.songId = parsedSongData.id;

      console.log("Loaded songData from localStorage:", parsedSongData);
      console.log("Loaded authToken from localStorage:", token);

      // Call the API to fetch the song details
      this.fetchSongDetails(token);
    } else {
      console.log("No songData or authToken found in localStorage.");
    }
  },
  methods: {
    async fetchSongDetails(token) {
      try {
        console.log("Fetching song details for ID:", this.songId);
        const response = await fetch(`http://127.0.0.1:5000/song/select_song`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`, // Include the token
          },
          body: JSON.stringify({
            song_id: this.songId,
          }),
        });

        if (!response.ok) {
          throw new Error("Failed to fetch song details");
        }

        const song = await response.json();
        this.songTitle = song.message || "Unknown Title";
        this.songContent = song.song.content; // Assuming the content is inside `song.song.content`
        console.log("Fetched song details:", song);
      } catch (error) {
        console.error("Error fetching song details:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Gradient background for the page */
body {
  background: linear-gradient(to right, #8e2de2, #4a00e0); /* Gradient colors */
  color: #fff;
  font-family: 'Roboto', sans-serif;
  font-size: 24px;
  line-height: 1.6;
  margin: 0;
  padding: 20px;
  text-align: center;
}

/* Styling for song lyrics and chords */
.song-lyrics {
  margin-top: 30px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  max-width: 95%;
  width: 95%;
  min-height: 300px;
  margin: auto;
  font-size: 24px;
  word-wrap: normal;
  white-space: pre-wrap;
}

.song-line {
  margin-bottom: 10px;
}

.chords {
  font-weight: bold;
  color: #ffcc00; /* Highlighted chord color */
  margin-right: 10px;
}

.lyrics {
  margin-right: 10px;
  word-wrap: break-word; /* Prevent words from overflowing the container */
  display: inline; /* Ensures the lyrics are shown inline with the chords */
}

/* Floating buttons (auto-scroll and quit) */
.scroll-toggle,
.quit-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #ffcc00;
  color: white;
  padding: 12px 20px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.quit-button {
  background-color: #e74c3c; /* Red color for quit button */
}
</style>
