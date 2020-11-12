<template>
  <div class="container">
    <h1>Here will be your sudoku!</h1>
    <div v-for="sudoku in yourSudoku" :key="sudoku.id">
      <router-link :to="{ name: 'OneSudoku', params: { slug: sudoku.slug } }">
        {{ sudoku.slug }}
      </router-link>
      <h4>{{ sudoku.created_at }}</h4>
      <h4>{{ sudoku.author }}</h4>
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
      loadingSudokus: false
    };
  },
  methods: {
    getSudoku() {
      let endpoint = "/api/sudoku/";
      if (this.next) {
        endpoint = this.next;
      }
      apiService(endpoint).then(data => {
        this.yourSudoku.push(...data.results);
        this.loadingSudokus = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
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
div {
  text-align: center;
}
.container {
  min-height: calc(100vh - 114px - 58px);
}
</style>
