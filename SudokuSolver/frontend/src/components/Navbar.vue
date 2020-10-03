<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'Home' }" class="navbar-brand"
        >Sudoku Solver</router-link
      >
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link
              :to="{ name: 'Sudoku' }"
              class="btn btn-sm btn-primary mx-2"
              >Your Sudoku</router-link
            >
          </li>
          <li class="nav-item">
            <a href="/accounts/logout/" class="btn btn-sm btn-outline-danger"
              >Logout</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style scoped>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}
.navbar-brand:hover {
  color: blue !important;
}
</style>