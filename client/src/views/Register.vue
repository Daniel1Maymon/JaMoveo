<template>
  <div class="register-container">
    <form @submit.prevent="handleRegister">
      <h2>Register</h2>
      <div class="form-group">
        <label for="username">User Name</label>
        <input
          type="text"
          id="username"
          v-model="username"
          placeholder="Enter your username"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Enter your password"
          required
        />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          placeholder="Confirm your password"
          required
        />
      </div>
      <div class="form-group">
        <label for="instrument">Instrument</label>
        <input
          type="text"
          id="instrument"
          v-model="instrument"
          placeholder="Enter your instrument (drums, guitars, bass,
saxophone, keyboards, and vocals)"
          required
        />
      </div>
      <button type="submit" class="register-button">Register</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success">{{ successMessage }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      instrument: "",
      errorMessage: null,
      successMessage: null,
    };
  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        this.errorMessage = "Passwords do not match.";
        return;
      }

      try {
        const response = await fetch("http://127.0.0.1:5000/auth/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
            instrument: this.instrument 
          }),
        });

        if (!response.ok) {
          const error = await response.json();
          this.errorMessage = error.error || "An error occurred";
          return;
        }

        const data = await response.json();
        this.successMessage = data.message || "Registration successful!";
        this.errorMessage = null;

        // Clear form fields
        this.username = "";
        this.password = "";
        this.confirmPassword = "";
        this.instrument = "";

        // Navigate to login page
        this.$router.push("/login"); // Vue Router navigation
      } catch (error) {
        this.errorMessage = "Failed to connect to the server.";
      }
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  background: linear-gradient(45deg, #3a3dff, #ff65a3);
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-container {
  background: rgba(255, 255, 255, 0.1);
  padding: 20px 40px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  text-align: center;
  color: white;
  width: 300px;
}

h2 {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: none;
  outline: none;
}

input[type="text"],
input[type="password"] {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.register-button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background: #008080;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

.register-button:hover {
  background: #36a370;
}

.error {
  color: red;
  margin-top: 10px;
}

.success {
  color: green;
  margin-top: 10px;
}
</style>
