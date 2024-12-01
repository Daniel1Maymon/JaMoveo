import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/HomeView.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AdminPage from '../views/AdminPage.vue';
import PlayerPage from '../views/PlayerPage.vue';
import LivePage from '../views/LivePage.vue';

const routes = [
  {
    path: '/admin',
    component: AdminPage,
    beforeEnter: (to, from, next) => {
      const role = localStorage.getItem('role'); // Check the user's role
      if (role === 'admin') {
        next(); // Allow access if the user is an admin
      } else {
        alert("Access denied: Admins only");
        next('/player'); // Redirect unauthorized users
      }
    },
  },
  { path: "/player", name: "Player", component: PlayerPage },
  { path: "/", name: "Home", component: Home },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register },
  { path: "/live", name: "Live", component: LivePage }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
