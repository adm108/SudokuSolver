<template>
  <div>
    <br />
    <h1>Here will be description of sudoku puzzle!</h1>
    <br />
    <table id="myTable">
      <tbody>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case00"
              id="case00"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case01"
              id="case01"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case02"
              id="case02"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case03"
              id="case03"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case04"
              id="case04"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case05"
              id="case05"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case06"
              id="case06"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case07"
              id="case07"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case08"
              id="case08"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case10"
              id="case10"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case11"
              id="case11"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case12"
              id="case12"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case13"
              id="case13"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case14"
              id="case14"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case15"
              id="case15"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case16"
              id="case16"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case17"
              id="case17"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case18"
              id="case18"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case20"
              id="case20"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case21"
              id="case21"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case22"
              id="case22"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case23"
              id="case23"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case24"
              id="case24"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case25"
              id="case25"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case26"
              id="case26"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case27"
              id="case27"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case28"
              id="case28"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case30"
              id="case30"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case31"
              id="case31"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case32"
              id="case32"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case33"
              id="case33"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case34"
              id="case34"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case35"
              id="case35"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case36"
              id="case36"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case37"
              id="case37"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case38"
              id="case38"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case40"
              id="case40"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case41"
              id="case41"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case42"
              id="case42"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case43"
              id="case43"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case44"
              id="case44"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case45"
              id="case45"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case46"
              id="case46"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case47"
              id="case47"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case48"
              id="case48"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case50"
              id="case50"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case51"
              id="case51"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case52"
              id="case52"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case53"
              id="case53"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case54"
              id="case54"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case55"
              id="case55"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case56"
              id="case56"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case57"
              id="case57"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case58"
              id="case58"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case60"
              id="case60"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case61"
              id="case61"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case62"
              id="case62"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case63"
              id="case63"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case64"
              id="case64"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case65"
              id="case65"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case66"
              id="case66"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case67"
              id="case67"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case68"
              id="case68"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case70"
              id="case70"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case71"
              id="case71"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case72"
              id="case72"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case73"
              id="case73"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case74"
              id="case74"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case75"
              id="case75"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case76"
              id="case76"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case77"
              id="case77"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case78"
              id="case78"
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case80"
              id="case80"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case81"
              id="case81"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case82"
              id="case82"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case83"
              id="case83"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case84"
              id="case84"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case85"
              id="case85"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case86"
              id="case86"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case87"
              id="case87"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model.number="case88"
              id="case88"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <br />
    <p v-if="firstError" class="error-message">{{ firstError }}</p>
    <p v-if="secondError" class="error-message">{{ secondError }}</p>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    <p v-if="loadingSudoku" class="success-message">...SOLVING SUDOKU...</p>
    <div id="container">
      <button id="button1" @click="verify()">Verify</button>
      <button id="button2" @click="clear()">Clear</button>
      <button id="button3" @click="solveSudoku()">Solve</button>
    </div>
    <br />
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
  name: "yoursudoku",
  data() {
    return {
      sudoku: [],
      case00: null,
      case01: null,
      case02: null,
      case03: null,
      case04: null,
      case05: null,
      case06: null,
      case07: null,
      case08: null,
      case10: null,
      case11: null,
      case12: null,
      case13: null,
      case14: null,
      case15: null,
      case16: null,
      case17: null,
      case18: null,
      case20: null,
      case21: null,
      case22: null,
      case23: null,
      case24: null,
      case25: null,
      case26: null,
      case27: null,
      case28: null,
      case30: null,
      case31: null,
      case32: null,
      case33: null,
      case34: null,
      case35: null,
      case36: null,
      case37: null,
      case38: null,
      case40: null,
      case41: null,
      case42: null,
      case43: null,
      case44: null,
      case45: null,
      case46: null,
      case47: null,
      case48: null,
      case50: null,
      case51: null,
      case52: null,
      case53: null,
      case54: null,
      case55: null,
      case56: null,
      case57: null,
      case58: null,
      case60: null,
      case61: null,
      case62: null,
      case63: null,
      case64: null,
      case65: null,
      case66: null,
      case67: null,
      case68: null,
      case70: null,
      case71: null,
      case72: null,
      case73: null,
      case74: null,
      case75: null,
      case76: null,
      case77: null,
      case78: null,
      case80: null,
      case81: null,
      case82: null,
      case83: null,
      case84: null,
      case85: null,
      case86: null,
      case87: null,
      case88: null,
      sudokuExample: [],
      sudokuTable: [],
      firstError: null,
      secondError: null,
      successMessage: null,
      loadingSudoku: false,
    };
  },
  methods: {
    getSudoku() {
      let endpoint = "api/sudoku/";
      apiService(endpoint).then((data) => {
        this.sudokuExample.push(...data.results);
      });
    },
    makeErrorSquare(line, column) {
      const input = document.getElementById("case" + line + column);
      input.classList.add("invalid");
      this.firstError = "Wrong value in your sudoku!";
      // remove css class when user put some new value (only once - "once" parameter)
      input.addEventListener(
        "input",
        () => {
          input.classList.remove("invalid");
        },
        { once: true }
      );
    },
    checkNumbers() {
      const listOfInput = document.querySelectorAll("input");
      for (const input of listOfInput) {
        input.classList.remove("invalid");
      }
      var numbersOfValues = 0;
      for (const input of listOfInput) {
        const validateInput = input.checkValidity();
        if (validateInput === false) {
          this.firstError = "Wrong value in your sudoku!";
        }
        if (input.value !== "") {
          numbersOfValues += 1;
        }
      }
      if (numbersOfValues < 3) {
        this.secondError = "Your sudoku need to have at least 3 values!";
      }
    },
    makeSudokuTable() {
      for (let line = 0; line < 9; line += 1) {
        const sudokuLine = [];
        for (let column = 0; column < 9; column += 1) {
          const identifier = `case${line}${column}`;
          const input = document.getElementById(identifier);
          const value = input.value;
          const number = value === "" ? "" : parseInt(value, 10);
          sudokuLine.push(number);
        }
        this.sudokuTable.push(sudokuLine);
      }
    },
    checkHorizontal() {
      for (let line = 0; line < 9; line += 1) {
        const list = new Set();
        for (let column = 0; column < 9; column += 1) {
          const value = this.sudokuTable[line][column];
          if (value !== "") {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              this.makeErrorSquare(line, column);
              this.firstError = "Wrong value in your sudoku!";
            } else {
              list.add(value);
            }
          }
        }
      }
    },
    checkVertical() {
      for (let column = 0; column < 9; column += 1) {
        const list = new Set();
        for (let line = 0; line < 9; line += 1) {
          const value = this.sudokuTable[line][column];
          if (value !== "") {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              this.makeErrorSquare(line, column);
              this.firstError = "Wrong value in your sudoku!";
            } else {
              list.add(value);
            }
          }
        }
      }
    },
    checkSquares() {
      const squares = [
        [
          [0, 0],
          [0, 1],
          [0, 2],
          [1, 0],
          [1, 1],
          [1, 2],
          [2, 0],
          [2, 1],
          [2, 2],
        ],
        [
          [0, 3],
          [0, 4],
          [0, 5],
          [1, 3],
          [1, 4],
          [1, 5],
          [2, 3],
          [2, 4],
          [2, 5],
        ],
        [
          [0, 6],
          [0, 7],
          [0, 8],
          [1, 6],
          [1, 7],
          [1, 8],
          [2, 6],
          [2, 7],
          [2, 8],
        ],
        [
          [3, 0],
          [3, 1],
          [3, 2],
          [4, 0],
          [4, 1],
          [4, 2],
          [5, 0],
          [5, 1],
          [5, 2],
        ],
        [
          [3, 3],
          [3, 4],
          [3, 5],
          [4, 3],
          [4, 4],
          [4, 5],
          [5, 3],
          [5, 4],
          [5, 5],
        ],
        [
          [3, 6],
          [3, 7],
          [3, 8],
          [4, 6],
          [4, 7],
          [4, 8],
          [5, 6],
          [5, 7],
          [5, 8],
        ],
        [
          [6, 0],
          [6, 1],
          [6, 2],
          [7, 0],
          [7, 1],
          [7, 2],
          [8, 0],
          [8, 1],
          [8, 2],
        ],
        [
          [6, 3],
          [6, 4],
          [6, 5],
          [7, 3],
          [7, 4],
          [7, 5],
          [8, 3],
          [8, 4],
          [8, 5],
        ],
        [
          [6, 6],
          [6, 7],
          [6, 8],
          [7, 6],
          [7, 7],
          [7, 8],
          [8, 6],
          [8, 7],
          [8, 8],
        ],
      ];
      for (const square of squares) {
        const list = new Set();
        for (const element of square) {
          const line = element[0];
          const column = element[1];
          const value = this.sudokuTable[line][column];
          if (value !== "") {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              this.makeErrorSquare(line, column);
              this.firstError = "Wrong value in your sudoku!";
            } else {
              list.add(value);
            }
          }
        }
      }
    },
    // I am not sure this is correct solution, I have to check it.
    verify() {
      this.sudokuTable = [];
      this.firstError = null;
      this.secondError = null;
      this.successMessage = null;
      this.checkNumbers();
      this.makeSudokuTable();
      this.checkHorizontal();
      this.checkVertical();
      this.checkSquares();
      if (this.firstError === null && this.secondError === null) {
        this.successMessage = "Everything is ok! :)";
      }
    },
    // I would like to clear all inputs without reloading the page, for now it's ok
    clear() {
      location.reload();
    },
    solveSudoku() {
      console.log("first step");
      this.verify();
      if (this.firstError === null && this.secondError === null) {
        this.loadingSudoku = true;
        let endpoint = "/api/sudoku/";
        let method = "POST";
        // ternatry operators changes empty strings to null (it's for preventing errors)
        apiService(endpoint, method, {
          case00: this.case00 === "" ? (this.case00 = null) : this.case00,
          case01: this.case01 === "" ? (this.case01 = null) : this.case01,
          case02: this.case02 === "" ? (this.case02 = null) : this.case02,
          case03: this.case03 === "" ? (this.case03 = null) : this.case03,
          case04: this.case04 === "" ? (this.case04 = null) : this.case04,
          case05: this.case05 === "" ? (this.case05 = null) : this.case05,
          case06: this.case06 === "" ? (this.case06 = null) : this.case06,
          case07: this.case07 === "" ? (this.case07 = null) : this.case07,
          case08: this.case08 === "" ? (this.case08 = null) : this.case08,
          case10: this.case10 === "" ? (this.case10 = null) : this.case10,
          case11: this.case11 === "" ? (this.case11 = null) : this.case11,
          case12: this.case12 === "" ? (this.case12 = null) : this.case12,
          case13: this.case13 === "" ? (this.case13 = null) : this.case13,
          case14: this.case14 === "" ? (this.case14 = null) : this.case14,
          case15: this.case15 === "" ? (this.case15 = null) : this.case15,
          case16: this.case16 === "" ? (this.case16 = null) : this.case16,
          case17: this.case17 === "" ? (this.case17 = null) : this.case17,
          case18: this.case18 === "" ? (this.case18 = null) : this.case18,
          case20: this.case20 === "" ? (this.case20 = null) : this.case20,
          case21: this.case21 === "" ? (this.case21 = null) : this.case21,
          case22: this.case22 === "" ? (this.case22 = null) : this.case22,
          case23: this.case23 === "" ? (this.case23 = null) : this.case23,
          case24: this.case24 === "" ? (this.case24 = null) : this.case24,
          case25: this.case25 === "" ? (this.case25 = null) : this.case25,
          case26: this.case26 === "" ? (this.case26 = null) : this.case26,
          case27: this.case27 === "" ? (this.case27 = null) : this.case27,
          case28: this.case28 === "" ? (this.case28 = null) : this.case28,
          case30: this.case30 === "" ? (this.case30 = null) : this.case30,
          case31: this.case31 === "" ? (this.case31 = null) : this.case31,
          case32: this.case32 === "" ? (this.case32 = null) : this.case32,
          case33: this.case33 === "" ? (this.case33 = null) : this.case33,
          case34: this.case34 === "" ? (this.case34 = null) : this.case34,
          case35: this.case35 === "" ? (this.case35 = null) : this.case35,
          case36: this.case36 === "" ? (this.case36 = null) : this.case36,
          case37: this.case37 === "" ? (this.case37 = null) : this.case37,
          case38: this.case38 === "" ? (this.case38 = null) : this.case38,
          case40: this.case40 === "" ? (this.case40 = null) : this.case40,
          case41: this.case41 === "" ? (this.case41 = null) : this.case41,
          case42: this.case42 === "" ? (this.case42 = null) : this.case42,
          case43: this.case43 === "" ? (this.case43 = null) : this.case43,
          case44: this.case44 === "" ? (this.case44 = null) : this.case44,
          case45: this.case45 === "" ? (this.case45 = null) : this.case45,
          case46: this.case46 === "" ? (this.case46 = null) : this.case46,
          case47: this.case47 === "" ? (this.case47 = null) : this.case47,
          case48: this.case48 === "" ? (this.case48 = null) : this.case48,
          case50: this.case50 === "" ? (this.case50 = null) : this.case50,
          case51: this.case51 === "" ? (this.case51 = null) : this.case51,
          case52: this.case52 === "" ? (this.case52 = null) : this.case52,
          case53: this.case53 === "" ? (this.case53 = null) : this.case53,
          case54: this.case54 === "" ? (this.case54 = null) : this.case54,
          case55: this.case55 === "" ? (this.case55 = null) : this.case55,
          case56: this.case56 === "" ? (this.case56 = null) : this.case56,
          case57: this.case57 === "" ? (this.case57 = null) : this.case57,
          case58: this.case58 === "" ? (this.case58 = null) : this.case58,
          case60: this.case60 === "" ? (this.case60 = null) : this.case60,
          case61: this.case61 === "" ? (this.case61 = null) : this.case61,
          case62: this.case62 === "" ? (this.case62 = null) : this.case62,
          case63: this.case63 === "" ? (this.case63 = null) : this.case63,
          case64: this.case64 === "" ? (this.case64 = null) : this.case64,
          case65: this.case65 === "" ? (this.case65 = null) : this.case65,
          case66: this.case66 === "" ? (this.case66 = null) : this.case66,
          case67: this.case67 === "" ? (this.case67 = null) : this.case67,
          case68: this.case68 === "" ? (this.case68 = null) : this.case68,
          case70: this.case70 === "" ? (this.case70 = null) : this.case70,
          case71: this.case71 === "" ? (this.case71 = null) : this.case71,
          case72: this.case72 === "" ? (this.case72 = null) : this.case72,
          case73: this.case73 === "" ? (this.case73 = null) : this.case73,
          case74: this.case74 === "" ? (this.case74 = null) : this.case74,
          case75: this.case75 === "" ? (this.case75 = null) : this.case75,
          case76: this.case76 === "" ? (this.case76 = null) : this.case76,
          case77: this.case77 === "" ? (this.case77 = null) : this.case77,
          case78: this.case78 === "" ? (this.case78 = null) : this.case78,
          case80: this.case80 === "" ? (this.case80 = null) : this.case80,
          case81: this.case81 === "" ? (this.case81 = null) : this.case81,
          case82: this.case82 === "" ? (this.case82 = null) : this.case82,
          case83: this.case83 === "" ? (this.case83 = null) : this.case83,
          case84: this.case84 === "" ? (this.case84 = null) : this.case84,
          case85: this.case85 === "" ? (this.case85 = null) : this.case85,
          case86: this.case86 === "" ? (this.case86 = null) : this.case86,
          case87: this.case87 === "" ? (this.case87 = null) : this.case87,
          case88: this.case88 === "" ? (this.case88 = null) : this.case88,
        }).then((sudoku_data) => {
          console.log(sudoku_data);
          this.loadingSudoku = false;
          this.$router.push({
            name: "OneSudoku",
            params: { slug: sudoku_data.slug },
          });
        });
      } else {
        this.loadingSudoku = false;
      }
    },
  },
  created() {
    this.getSudoku();
    document.title = "Sudoku Solver";
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  outline: 0;
  border: 0;
  border-spacing: 0;
  box-sizing: border-box;
}
table {
  margin: 0 auto;
}
input {
  height: min(calc(100vh / 14), calc(100vw / 14));
  width: min(calc(100vh / 14), calc(100vw / 14));
  background-color: #efefef;
  font-size: 5vh;
  text-align: center;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input:invalid,
.invalid {
  border: 1px solid red;
  background-color: #eec3c3;
}
#container {
  text-align: center;
}
#button1,
#button2,
#button3 {
  color: white;
  margin: 1em 0.35em;
  padding: 0.5em 2em;
  font-size: 3vh;
  border-radius: 10px;
  outline: 0 !important;
}
#button1 {
  background-color: #4361ee;
}
#button2 {
  background-color: #da4655;
}
#button3 {
  background-color: #579b38;
}
#button1:hover {
  background-color: #183ddf;
}
#button2:hover {
  background-color: #fa0b23;
}
#button3:hover {
  background-color: #56c224;
}
tr {
  border-bottom: 1px solid #ccc;
  display: block;
}
tr:nth-of-type(3),
tr:nth-of-type(6) {
  border-bottom: 1px solid #000;
}
td {
  border-right: 1px solid #ccc;
}
td:nth-of-type(3),
td:nth-of-type(6) {
  border-right: 1px solid #000;
}
h1 {
  text-align: center;
}
.error-message {
  color: red;
  text-align: center;
}
.success-message {
  color: #56c224;
  text-align: center;
}
</style>
