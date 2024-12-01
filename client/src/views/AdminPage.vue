<template>
  <div>
    <h1>Admin Page</h1>
    <p>Welcome to the admin panel. Only admins should see this page.</p>
    <button @click="fetchSongs">Select Song</button>
    <button @click="startSession">Start Session</button>
    <p v-if="message">{{ message }}</p>
  </div>

    <!-- Display the song list -->
    <div v-if="songs.length > 0" class="song-list">
    <h2>All Songs</h2>
    <div v-for="song in songs" :key="song.id" class="song-item">
        <div class="song-info">
        <h3>{{ song.name }}</h3>
        <p>{{ song.description }}</p>
        </div>
        <button class="select-button" @click="selectSong(song.name)">
        Select
        </button>
    </div>
    </div>

</template>

<script>
import { io } from "socket.io-client";


export default {
  name: "AdminPage",
    data() {
    return {
        songs: [], // List of songs fetched from the server
        selectedSong: "", // Song selected from the dropdown
    };
    },

  methods: {
    // Connect to WebSocket
    connectSocket() {
      this.socket = io("http://127.0.0.1:5000");

      // Listen for session_started event
      this.socket.on("session_started", (data) => {
        this.message = data.message;
        console.log("Session Started:", data);
      });

      // Listen for song_selected event
      this.socket.on("song_selected", (data) => {
        this.message = `Song Selected: ${data.song}`;
        console.log("Song Selected:", data);
      });

      // Listen for session_ended event
      this.socket.on("session_ended", (data) => {
        this.message = data.message;
        console.log("Session Ended:", data);
      });
    },

    // Start a new session
    async startSession() {
    const token = localStorage.getItem("access_token"); // Retrieve the token from localStorage

    console.log("sending token = ")
    console.log(token)
      try {
        const response = await fetch("http://127.0.0.1:5000/session/start_session", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`, // Include the token
            },
        });

        if (response.ok) {
          console.log("Session started successfully");
        } else {
          const errorData = await response.json();
          this.message = errorData.error || "Failed to start session";
        }
      } catch (error) {
        this.message = "An error occurred while starting the session.";
        console.error(error);
      }
    },

    // Select a song
    async selectSong() {
    const token = localStorage.getItem("access_token");

    try {
        const response = await fetch("http://127.0.0.1:5000/session/select_song", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ song: this.selectedSong }),
        });

        if (response.ok) {
        console.log("Song selected successfully");
        } else {
        const errorData = await response.json();
        console.error("Failed to select song:", errorData);
        }
    } catch (error) {
        console.error("An error occurred while selecting the song:", error);
    }
    },

    async fetchSongs() {
    const token = localStorage.getItem("access_token");

    try {
        const response = await fetch("http://127.0.0.1:5000/song/songs", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        });

        if (response.ok) {
        this.songs = await response.json();
        console.log("Songs fetched successfully:", this.songs);
        } else {
        const errorData = await response.json();
        console.error("Failed to fetch songs:", errorData);
        }
    } catch (error) {
        console.error("An error occurred while fetching songs:", error);
    }
    },
  },
  mounted() {
    // Connect to WebSocket when component is mounted
    this.connectSocket();
  },
  beforeDestroy() {
    // Disconnect from WebSocket when component is destroyed
    if (this.socket) {
      this.socket.disconnect();
    }
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

button {
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-right: 100px;
   align-items: flex-start;
}

button:hover {
  background-color: #2c8c6b;
}

select {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}


</style>
