<template>
  <div class="single-sudoku">
    <h1>{{ slug }}</h1>
  </div>
</template>

<script>
export default {
  name: "OneSudoku",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      sudoku: {}
    };
  },
  methods: {
    getSudokuData() {
      let endpoint = `api/sudoku/${this.slug}/`;
    }
  }
};
</script>

<style scoped>
h1 {
  text-align: center;
}
.single-sudoku {
  min-height: calc(100vh - 114px - 58px);
}
</style>