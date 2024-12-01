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
    <div v-if="results.length > 0" class="results-container">
      <div
        v-for="result in results"
        :key="result.id"
        class="result-item"
        @click="printResult(result)" 
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
      results: [], // Store search results
      loading: false, // Indicate if a request is in progress
      errorMessage: "", // Store error messages
    };
  },
  methods: {
    onButtonPress() {
      this.buttonPressed = true;
    },
    onButtonRelease() {
      this.buttonPressed = false;
    },
    printResult(result) {
      console.log("Selected Result:", result);
      console.log(result.id); 
      console.log(result.title);
    },
    async searchSong() {
      if (this.query.trim() === "") {
        this.results = [];
        this.errorMessage = "";
        return;
      }
      this.loading = true; // Start loading indicator
      this.errorMessage = ""; // Clear any previous error messages
      try {
        const response = await fetch("http://127.0.0.1:5000/song/search_songs", {
          method: "POST", // Use POST method
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ query: this.query }), // Send the query in the request body
        });

        if (!response.ok) {
          const errorData = await response.json();
          this.errorMessage = errorData.error || "An error occurred.";
          this.results = [];
        } else {
          this.results = await response.json(); // Populate results
        }
      } catch (error) {
        console.error("Error searching for songs:", error);
        this.errorMessage = "Failed to fetch results. Please try again.";
      } finally {
        this.loading = false; // Stop loading indicator
      }
    },
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
  transition: box-shadow 0.3s ease; /* Add transition for hover effect */
  cursor: pointer;
}

.result-item:last-child {
  border-bottom: none;
}

.result-item h3 {
  margin: 0;
  font-size: 1rem;
}

.result-item p {
  margin: 0;
  color: #666;
}

.result-item:active {
  background-color: #e0e0e0; /* Slightly darker gray */
}

.error {
  color: red;
  margin-top: 10px;
}

.result-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  background-color: #f0f0f0; /* Light gray background */
}

.select-button {
  padding: 8px 16px;
  border: none;
  background-color: #2575fc;
  color: white;
  border-radius: 8px;
  cursor: pointer; /* Change the cursor to a pointer */
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.select-button:active {
  transform: scale(0.95);
  background-color: #1a5dbf;
}

</style>
