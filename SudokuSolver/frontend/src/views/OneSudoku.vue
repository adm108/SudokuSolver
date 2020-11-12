<template>
  <div class="single-sudoku">
    <br />
    <h3>STATISTICS</h3>
    <h5>Number of funcion calls:</h5>
    <h5 class="statistics">{{ sudoku.solve_counter }}</h5>
    <h5>Time of algorithm:</h5>
    <h5 class="statistics">{{ sudoku.solve_time }} [s]</h5>
    <table>
      <h3 style="color: red">Sudoku before solve:</h3>
      <tbody>
        <tr>
          <td>{{ sudoku.case00 }}</td>
          <td>{{ sudoku.case01 }}</td>
          <td>{{ sudoku.case02 }}</td>
          <td>{{ sudoku.case03 }}</td>
          <td>{{ sudoku.case04 }}</td>
          <td>{{ sudoku.case05 }}</td>
          <td>{{ sudoku.case06 }}</td>
          <td>{{ sudoku.case07 }}</td>
          <td>{{ sudoku.case08 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case10 }}</td>
          <td>{{ sudoku.case11 }}</td>
          <td>{{ sudoku.case12 }}</td>
          <td>{{ sudoku.case13 }}</td>
          <td>{{ sudoku.case14 }}</td>
          <td>{{ sudoku.case15 }}</td>
          <td>{{ sudoku.case16 }}</td>
          <td>{{ sudoku.case17 }}</td>
          <td>{{ sudoku.case18 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case20 }}</td>
          <td>{{ sudoku.case21 }}</td>
          <td>{{ sudoku.case22 }}</td>
          <td>{{ sudoku.case23 }}</td>
          <td>{{ sudoku.case24 }}</td>
          <td>{{ sudoku.case25 }}</td>
          <td>{{ sudoku.case26 }}</td>
          <td>{{ sudoku.case27 }}</td>
          <td>{{ sudoku.case28 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case30 }}</td>
          <td>{{ sudoku.case31 }}</td>
          <td>{{ sudoku.case32 }}</td>
          <td>{{ sudoku.case33 }}</td>
          <td>{{ sudoku.case34 }}</td>
          <td>{{ sudoku.case35 }}</td>
          <td>{{ sudoku.case36 }}</td>
          <td>{{ sudoku.case37 }}</td>
          <td>{{ sudoku.case38 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case40 }}</td>
          <td>{{ sudoku.case41 }}</td>
          <td>{{ sudoku.case42 }}</td>
          <td>{{ sudoku.case43 }}</td>
          <td>{{ sudoku.case44 }}</td>
          <td>{{ sudoku.case45 }}</td>
          <td>{{ sudoku.case46 }}</td>
          <td>{{ sudoku.case47 }}</td>
          <td>{{ sudoku.case48 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case50 }}</td>
          <td>{{ sudoku.case51 }}</td>
          <td>{{ sudoku.case52 }}</td>
          <td>{{ sudoku.case53 }}</td>
          <td>{{ sudoku.case54 }}</td>
          <td>{{ sudoku.case55 }}</td>
          <td>{{ sudoku.case56 }}</td>
          <td>{{ sudoku.case57 }}</td>
          <td>{{ sudoku.case58 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case60 }}</td>
          <td>{{ sudoku.case61 }}</td>
          <td>{{ sudoku.case62 }}</td>
          <td>{{ sudoku.case63 }}</td>
          <td>{{ sudoku.case64 }}</td>
          <td>{{ sudoku.case65 }}</td>
          <td>{{ sudoku.case66 }}</td>
          <td>{{ sudoku.case67 }}</td>
          <td>{{ sudoku.case68 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case70 }}</td>
          <td>{{ sudoku.case71 }}</td>
          <td>{{ sudoku.case72 }}</td>
          <td>{{ sudoku.case73 }}</td>
          <td>{{ sudoku.case74 }}</td>
          <td>{{ sudoku.case75 }}</td>
          <td>{{ sudoku.case76 }}</td>
          <td>{{ sudoku.case77 }}</td>
          <td>{{ sudoku.case78 }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case80 }}</td>
          <td>{{ sudoku.case81 }}</td>
          <td>{{ sudoku.case82 }}</td>
          <td>{{ sudoku.case83 }}</td>
          <td>{{ sudoku.case84 }}</td>
          <td>{{ sudoku.case85 }}</td>
          <td>{{ sudoku.case86 }}</td>
          <td>{{ sudoku.case87 }}</td>
          <td>{{ sudoku.case88 }}</td>
        </tr>
      </tbody>
    </table>
    <table>
      <h3 style="color: green">Solved sudoku:</h3>
      <tbody>
        <tr>
          <td>{{ sudoku.case00s }}</td>
          <td>{{ sudoku.case01s }}</td>
          <td>{{ sudoku.case02s }}</td>
          <td>{{ sudoku.case03s }}</td>
          <td>{{ sudoku.case04s }}</td>
          <td>{{ sudoku.case05s }}</td>
          <td>{{ sudoku.case06s }}</td>
          <td>{{ sudoku.case07s }}</td>
          <td>{{ sudoku.case08s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case10s }}</td>
          <td>{{ sudoku.case11s }}</td>
          <td>{{ sudoku.case12s }}</td>
          <td>{{ sudoku.case13s }}</td>
          <td>{{ sudoku.case14s }}</td>
          <td>{{ sudoku.case15s }}</td>
          <td>{{ sudoku.case16s }}</td>
          <td>{{ sudoku.case17s }}</td>
          <td>{{ sudoku.case18s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case20s }}</td>
          <td>{{ sudoku.case21s }}</td>
          <td>{{ sudoku.case22s }}</td>
          <td>{{ sudoku.case23s }}</td>
          <td>{{ sudoku.case24s }}</td>
          <td>{{ sudoku.case25s }}</td>
          <td>{{ sudoku.case26s }}</td>
          <td>{{ sudoku.case27s }}</td>
          <td>{{ sudoku.case28s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case30s }}</td>
          <td>{{ sudoku.case31s }}</td>
          <td>{{ sudoku.case32s }}</td>
          <td>{{ sudoku.case33s }}</td>
          <td>{{ sudoku.case34s }}</td>
          <td>{{ sudoku.case35s }}</td>
          <td>{{ sudoku.case36s }}</td>
          <td>{{ sudoku.case37s }}</td>
          <td>{{ sudoku.case38s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case40s }}</td>
          <td>{{ sudoku.case41s }}</td>
          <td>{{ sudoku.case42s }}</td>
          <td>{{ sudoku.case43s }}</td>
          <td>{{ sudoku.case44s }}</td>
          <td>{{ sudoku.case45s }}</td>
          <td>{{ sudoku.case46s }}</td>
          <td>{{ sudoku.case47s }}</td>
          <td>{{ sudoku.case48s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case50s }}</td>
          <td>{{ sudoku.case51s }}</td>
          <td>{{ sudoku.case52s }}</td>
          <td>{{ sudoku.case53s }}</td>
          <td>{{ sudoku.case54s }}</td>
          <td>{{ sudoku.case55s }}</td>
          <td>{{ sudoku.case56s }}</td>
          <td>{{ sudoku.case57s }}</td>
          <td>{{ sudoku.case58s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case60s }}</td>
          <td>{{ sudoku.case61s }}</td>
          <td>{{ sudoku.case62s }}</td>
          <td>{{ sudoku.case63s }}</td>
          <td>{{ sudoku.case64s }}</td>
          <td>{{ sudoku.case65s }}</td>
          <td>{{ sudoku.case66s }}</td>
          <td>{{ sudoku.case67s }}</td>
          <td>{{ sudoku.case68s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case70s }}</td>
          <td>{{ sudoku.case71s }}</td>
          <td>{{ sudoku.case72s }}</td>
          <td>{{ sudoku.case73s }}</td>
          <td>{{ sudoku.case74s }}</td>
          <td>{{ sudoku.case75s }}</td>
          <td>{{ sudoku.case76s }}</td>
          <td>{{ sudoku.case77s }}</td>
          <td>{{ sudoku.case78s }}</td>
        </tr>
        <tr>
          <td>{{ sudoku.case80s }}</td>
          <td>{{ sudoku.case81s }}</td>
          <td>{{ sudoku.case82s }}</td>
          <td>{{ sudoku.case83s }}</td>
          <td>{{ sudoku.case84s }}</td>
          <td>{{ sudoku.case85s }}</td>
          <td>{{ sudoku.case86s }}</td>
          <td>{{ sudoku.case87s }}</td>
          <td>{{ sudoku.case88s }}</td>
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
  font-size: 3.5vh;
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
  border-bottom: 2px solid rgb(80, 78, 78);
}
td:nth-of-type(3),
td:nth-of-type(6) {
  border-right: 2px solid rgb(80, 78, 78);
}
h3,
h5 {
  text-align: center;
}
.statistics {
  color: rgb(197, 53, 202);
}
</style>  