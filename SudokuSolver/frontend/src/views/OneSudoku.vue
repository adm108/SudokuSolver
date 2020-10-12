<template>
  <div class="single-sudoku">
    <h1>{{ sudoku.a1b1 }}</h1>
    <h1>{{ sudoku.author }}</h1>
    <h1>{{ sudoku.created_at }}</h1>
    <h1>{{ sudoku.slug }}</h1>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
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
    setPageTitle(title) {
      document.title = title;
    },
    getSudokuData() {
      let endpoint = `/api/sudoku/${this.slug}/`;
      apiService(endpoint).then(data => {
        this.sudoku = data;
        this.setPageTitle(data.slug);
      });
    }
  },
  created() {
    this.getSudokuData();
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