<template>
  <div class="login-container">
    <form @submit.prevent="handleLogin">
      <h2>Login</h2>
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
      <button type="submit" class="login-button">Login</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: null,
    };
  },
  methods: {
  async handleLogin() {
  try {
    const response = await fetch("https://considerate-nourishment-production.up.railway.app:5000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: this.username,
        password: this.password,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      this.errorMessage = error.error || "An error occurred";
      return;
    }

    console.log("auth/login SUCCESS!")
    const data = await response.json();
    this.errorMessage = null;

    console.log("data = ")
    console.log(data)


    // Temporary test: Check access to a protected endpoint
    localStorage.setItem("access_token", data.token);
    localStorage.setItem("role", data.role); // Save the role
  

    const token = localStorage.getItem("access_token"); // Retrieve the token from localStorage

    console.log(`token = ${token}`)

    const testResponse = await fetch("https://127.0.0.1:5000/auth/protected", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`, // Include the token
      },
    });

    console.log("AFTER auth/protected")
    if (!testResponse.ok) {
      console.error("Failed to access protected endpoint.");
      const error = await testResponse.json();
      console.error("Error:", error);
      this.errorMessage = "Protected endpoint access failed.";
      return;
    }


    console.log("auth/protected SUCCESS!")
    const testData = await testResponse.json();
    console.log("Protected endpoint data:", testData);


    // Navigate based on role
    console.log("data = " + data)

    if (data.role === "admin") {
      this.$router.push("/admin");
    } else if (data.role === "player") {
      this.$router.push("/player");
    }
  } catch (error) {
    this.errorMessage = "Failed to connect to the server.";
  }
}
  },
};
</script>

<style>
/* Background and general body style */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  background: linear-gradient(45deg, #3a3dff, #ff65a3);
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Login container style */
.login-container {
  background: rgba(255, 255, 255, 0.1);
  padding: 20px 40px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  text-align: center;
  color: white;
  width: 300px;
}

/* Title style */
h2 {
  margin-bottom: 20px;
}

/* Form field styles */
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

/* Button style */
.login-button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background: #008080;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

.login-button:hover {
  background: #008080;
}

/* Error message style */
.error {
  color: red;
  margin-top: 10px;
}
</style>
