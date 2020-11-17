<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import { apiService } from "./common/api.service";
import NavbarComponent from "./components/Navbar.vue";
import FooterComponent from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    NavbarComponent,
    FooterComponent,
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Fredoka One", sans-serif;
  font-weight: normal;
}
.btn:focus {
  box-shadow: none !important;
  background-color: none !important;
}
</style>
