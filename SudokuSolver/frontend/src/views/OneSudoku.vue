<template>
  <div class="single-sudoku">
    <br />
    <br />
    <br />
    <table>
      <caption>
        Sudoku
      </caption>
      <colgroup>
        <col />
        <col />
        <col />
      </colgroup>
      <colgroup>
        <col />
        <col />
        <col />
      </colgroup>
      <colgroup>
        <col />
        <col />
        <col />
      </colgroup>
      <tbody>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
      <tbody>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
      <tbody>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
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
table {
  border-collapse: collapse;
}
colgroup,
tbody {
  border: solid medium;
}
td {
  border: solid thin;
  height: 2em;
  width: 2em;
  text-align: center;
  padding: 0;
}
</style>