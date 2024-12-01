<template>
  <div class="search-container">
    <h1>Search for a Song</h1>
    <input
      v-model="query"
      @input="searchSong"
      type="text"
      placeholder="Enter song name..."
      class="input-field"
    />
    <div v-if="Array.isArray(results) && results.length > 0" class="results-container">
    <div
        v-for="result in results"
        :key="result.id"
        class="result-item"
        @click="navigateToLivePage(result)"
    >
        <h3>{{ result.title }}</h3>
    </div>
    </div>
    <p v-else-if="query && !loading">No results found.</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "AdminMainPage",
    data() {
    return {
        query: "",
        results: [], // Always initialized as an empty array
        loading: false,
        errorMessage: "",
    };
    },
  methods: {
    navigateToLivePage(result) {
      const songData = { id: result.id, title: result.title };
      localStorage.setItem('songData', JSON.stringify(songData));

      this.$router.push({ name: "Live" });
    },
   async searchSong() {
    if (this.query.trim() === "") {
      this.results = []; // Reset results
      this.errorMessage = "";
      return;
    }
    this.loading = true;
    this.errorMessage = "";
  try {
    const response = await fetch("http://127.0.0.1:5000/song/search_songs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: this.query }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      this.errorMessage = errorData.error || "An error occurred.";
      this.results = []; // Reset results
    } else {
      const data = await response.json();
      this.results = Array.isArray(data) ? data : []; // Ensure results is an array
    }
  } catch (error) {
    console.error("Error searching for songs:", error);
    this.errorMessage = "Failed to fetch results. Please try again.";
    this.results = []; // Reset results on error
  } finally {
    this.loading = false;
  }
    }   
  },
};
</script>


<style scoped>
/* Results container styling */
.results-container {
  margin-top: 10px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.result-item {
  padding: 10px;
  border-bottom: 1px solid #eee;
  transition: box-shadow 0.3s ease;
  cursor: pointer;
}

.result-item:last-child {
  border-bottom: none;
}

.result-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  background-color: #f0f0f0;
}

.result-item:active {
  background-color: #e0e0e0;
}
</style>
