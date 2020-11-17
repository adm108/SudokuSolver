<template>
  <div class="container">
    <br />
    <h3>
      Your all solved sudoku are below! Click for solving details for each
      record or delete it. :)
    </h3>
    <h3 class="sudoku-count">Number of solved sudoku: {{ sudokuCount }}</h3>
    <br />
    <hr />

    <div v-for="sudoku in yourSudoku" :key="sudoku.id">
      <router-link :to="{ name: 'OneSudoku', params: { slug: sudoku.slug } }">
        {{ sudoku.slug }}
      </router-link>
      <h4>Created at: {{ sudoku.created_at }}</h4>
      <button
        class="btn btn-sm btn-outline-danger"
        @click="deleteSudoku(sudoku)"
      >
        DELETE
      </button>
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
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    async deleteSudoku(sudoku) {
      let endpoint = `/api/sudoku/${sudoku.slug}/`;
      let method = "DELETE";
      try {
        await apiService(endpoint, method);
        this.$delete(this.yourSudoku, this.yourSudoku.indexOf(sudoku));
        this.sudokuCount -= 1;
      } catch (err) {
        console.log(err);
      }
    },
  },
  created() {
    this.getSudoku();
    this.setRequestUser();
    document.title = "Your Sudoku";
  },
};
</script>

<style scoped>
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
