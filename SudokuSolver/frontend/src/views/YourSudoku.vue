<template>
  <div class="main">
    <h1>Here will be your sudoku!</h1>
    <div v-for="sudoku in yourSudoku" :key="sudoku.id">
      <p>{{ sudoku.author }}</p>
      <h4>{{ sudoku.a1b1 }}</h4>
      <router-link :to="{ name: 'OneSudoku', params: { slug: sudoku.slug } }">
        {{ sudoku.slug }}
      </router-link>
      <h4>{{ sudoku.created_at }}</h4>
      <hr />
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
  name: "YourSudoku",
  data() {
    return {
      yourSudoku: []
    };
  },
  methods: {
    getSudoku() {
      let endpoint = "/api/sudoku/";
      apiService(endpoint).then(data => {
        this.yourSudoku.push(...data.results);
      });
    }
  },
  created() {
    this.getSudoku();
    document.title = "Your Sudoku";
    console.log(this.yourSudoku);
  }
};
</script>

<style scoped>
h1 {
  text-align: center;
}
.main {
  min-height: calc(100vh - 114px - 58px);
}
div {
  text-align: center;
}
</style>
