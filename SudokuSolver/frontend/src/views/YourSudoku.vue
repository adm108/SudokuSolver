<template>
  <div class="container">
    <h1>Your all solved sudoku are below!</h1>
    <h2 class="sudoku-count">Number of solved sudoku: {{ sudokuCount }}</h2>
    <h3>Click for details of each recrod!</h3>
    <br />
    <hr />

    <div v-for="sudoku in yourSudoku" :key="sudoku.id">
      <router-link :to="{ name: 'OneSudoku', params: { slug: sudoku.slug } }">
        {{ sudoku.slug }}
      </router-link>
      <h4>Created at: {{ sudoku.created_at }}</h4>
      <hr />
    </div>
    <div>
      <p v-show="loadingSudokus">...loading...</p>
      <button
        v-show="next"
        @click="getSudoku"
        class="btn btn-sm btn-outline-success"
      >
        Load More
      </button>
    </div>
    <br />
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
  name: "YourSudoku",
  data() {
    return {
      yourSudoku: [],
      next: null,
      loadingSudokus: false,
      sudokuCount: null,
    };
  },
  methods: {
    getSudoku() {
      let endpoint = "/api/sudoku/";
      if (this.next) {
        endpoint = this.next;
      }
      apiService(endpoint).then((data) => {
        this.yourSudoku.push(...data.results);
        this.loadingSudokus = false;
        this.sudokuCount = data.count;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  created() {
    this.getSudoku();
    document.title = "Your Sudoku";
    console.log(this.yourSudoku);
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}
div {
  text-align: center;
}
.container {
  min-height: calc(100vh - 114px - 58px);
}
.sudoku-count {
  color: rgb(197, 53, 202);
}
</style>
