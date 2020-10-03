<template>
  <footer>
    <div class="footer1">
      <a href="https://www.facebook.com/adam.rogacewicz" target="_blank">
        <i class="fa fa-facebook fa-lg white-text mr-md-5 mr-3 fa-2x"></i>
      </a>
      <a href="https://www.linkedin.com/in/adam-rogacewicz/" target="_blank">
        <i class="fa fa-linkedin fa-lg white-text mr-md-5 mr-3 fa-2x"></i>
      </a>
      <a href="https://github.com/adm108" target="_blank">
        <i class="fa fa-github fa-lg white-text mr-md-5 mr-3 fa-2x"></i>
      </a>
    </div>
    <div class="footer2">
      <h6>&copy; 2020. All rights reserved. Created by Adam Rogacewicz.</h6>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent"
};
</script>

<style scoped>
.footer1 {
  width: 100%;
  height: 57px;
  background: #d9dce2;
  display: flex;
  align-items: center;
  justify-content: center;
}
.footer1 a {
  vertical-align: middle;
}
.footer2 {
  width: 100%;
  height: 57px;
  background: #bec2ca;
  display: flex;
  align-items: center;
  justify-content: center;
}
.footer2 h6 {
  vertical-align: middle;
}
</style>