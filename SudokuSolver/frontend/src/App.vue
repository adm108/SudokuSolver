<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue";
import FooterComponent from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    NavbarComponent,
    FooterComponent
  }
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
