<template>
  <div class="single-sudoku">
    <br />
    <h3>Statistics:</h3>
    <h4>Number of funcion calls: XXX</h4>
    <h4>Data: XXX</h4>
    <h4>Slug of sudoku: XXX</h4>
    <table>
      <h3 style="color: red">Sudoku before solve:</h3>
      <tbody>
        <tr>
          <td>1</td>
          <td>2</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>6</td>
          <td>7</td>
          <td>8</td>
          <td>9</td>
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
    <table>
      <h3 style="color: green">Solved sudoku:</h3>
      <tbody>
        <tr>
          <td>1</td>
          <td>2</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
          <td>6</td>
          <td>7</td>
          <td>8</td>
          <td>9</td>
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
          <td>1</td>
          <td>2</td>
          <td>3</td>
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
* {
  margin: 0;
  padding: 0;
  outline: 0;
  border: 0;
  border-spacing: 0;
  box-sizing: border-box;
}
table {
  float: left;
  margin-left: 300px;
  margin-bottom: 30px;
}
td {
  height: calc(100vh / 18);
  width: calc(100vh / 18);
  background-color: #efefef;
  font-size: 4vh;
  text-align: center;
  border-right: 1px solid #ccc;
}
tr {
  border-bottom: 1px solid #ccc;
  border-left: 1px solid #ccc;
  display: block;
}
tr:nth-of-type(1) {
  border-top: 1px solid #ccc;
}
tr:nth-of-type(3),
tr:nth-of-type(6) {
  border-bottom: 1px solid #000;
}
td:nth-of-type(3),
td:nth-of-type(6) {
  border-right: 1px solid #000;
}
h3,
h4 {
  text-align: center;
}
</style>