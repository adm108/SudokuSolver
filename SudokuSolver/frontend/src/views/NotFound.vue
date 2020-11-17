<template>
  <div class="not-found">
    <h1 id="not-found">{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found",
    };
  },
  created() {
    document.title = "404 - Page Not Found";
  },
};
</script>

<style scoped>
.not-found {
  min-height: calc(100vh - 114px - 58px);
  position: relative;
}
#not-found {
  color: red;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}
</style>