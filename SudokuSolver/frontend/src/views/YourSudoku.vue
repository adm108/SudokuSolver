<template>
  <div class="yoursudoku">
    <h1>Here will be you sudoku puzzles!</h1>
    <table>
      <tbody>
        <tr>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case00"
              id="case00"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case01"
              id="case01"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case02"
              id="case02"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case03"
              id="case03"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case04"
              id="case04"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case05"
              id="case05"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case06"
              id="case06"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case07"
              id="case07"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case08"
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
              v-model="case10"
              id="case10"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case11"
              id="case11"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case12"
              id="case12"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case13"
              id="case13"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case14"
              id="case14"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case15"
              id="case15"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case16"
              id="case16"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case17"
              id="case17"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case18"
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
              v-model="case20"
              id="case20"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case21"
              id="case21"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case22"
              id="case22"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case23"
              id="case23"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case24"
              id="case24"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case25"
              id="case25"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case26"
              id="case26"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case27"
              id="case27"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case28"
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
              v-model="case30"
              id="case30"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case31"
              id="case31"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case32"
              id="case32"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case33"
              id="case33"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case34"
              id="case34"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case35"
              id="case35"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case36"
              id="case36"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case37"
              id="case37"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case38"
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
              v-model="case40"
              id="case40"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case41"
              id="case41"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case42"
              id="case42"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case43"
              id="case43"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case44"
              id="case44"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case45"
              id="case45"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case46"
              id="case46"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case47"
              id="case47"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case48"
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
              v-model="case50"
              id="case50"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case51"
              id="case51"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case52"
              id="case52"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case53"
              id="case53"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case54"
              id="case54"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case55"
              id="case55"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case56"
              id="case56"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case57"
              id="case57"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case58"
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
              v-model="case60"
              id="case60"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case61"
              id="case61"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case62"
              id="case62"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case63"
              id="case63"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case64"
              id="case64"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case65"
              id="case65"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case66"
              id="case66"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case67"
              id="case67"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case68"
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
              v-model="case70"
              id="case70"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case71"
              id="case71"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case72"
              id="case72"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case73"
              id="case73"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case74"
              id="case74"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case75"
              id="case75"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case76"
              id="case76"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case77"
              id="case77"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case78"
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
              v-model="case80"
              id="case80"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case81"
              id="case81"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case82"
              id="case82"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case83"
              id="case83"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case84"
              id="case84"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case85"
              id="case85"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case86"
              id="case86"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case87"
              id="case87"
            />
          </td>
          <td>
            <input
              type="number"
              min="1"
              max="9"
              step="1"
              v-model="case88"
              id="case88"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="verify()">Verify !</button>
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
      case00: "",
      case01: "",
      case02: "",
      case03: "",
      case04: "",
      case05: "",
      case06: "",
      case07: "",
      case08: "",
      case10: "",
      case11: "",
      case12: "",
      case13: "",
      case14: "",
      case15: "",
      case16: "",
      case17: "",
      case18: "",
      case20: "",
      case21: "",
      case22: "",
      case23: "",
      case24: "",
      case25: "",
      case26: "",
      case27: "",
      case28: "",
      case30: "",
      case31: "",
      case32: "",
      case33: "",
      case34: "",
      case35: "",
      case36: "",
      case37: "",
      case38: "",
      case40: "",
      case41: "",
      case42: "",
      case43: "",
      case44: "",
      case45: "",
      case46: "",
      case47: "",
      case48: "",
      case50: "",
      case51: "",
      case52: "",
      case53: "",
      case54: "",
      case55: "",
      case56: "",
      case57: "",
      case58: "",
      case60: "",
      case61: "",
      case62: "",
      case63: "",
      case64: "",
      case65: "",
      case66: "",
      case67: "",
      case68: "",
      case70: "",
      case71: "",
      case72: "",
      case73: "",
      case74: "",
      case75: "",
      case76: "",
      case77: "",
      case78: "",
      case80: "",
      case81: "",
      case82: "",
      case83: "",
      case84: "",
      case85: "",
      case86: "",
      case87: "",
      case88: ""
    };
  },
  methods: {
    getSudoku() {
      let endpoint = "api/sudoku/";
      apiService(endpoint).then(data => {
        this.sudoku.push(...data.results);
      });
    },
    verify() {
      const listOfInput = document.querySelectorAll("input");

      // every pushing button will reset all css classes
      for (const input of listOfInput) {
        input.classList.remove("invalid");
      }

      // is all numers are between 1 and 9?
      for (const input of listOfInput) {
        const validateInput = input.checkValidity();
        if (validateInput === false) {
          return;
        }
      }
      // making list of 9 lists with sudoku numbers
      const sudoku = [];
      for (let line = 0; line < 9; line += 1) {
        const sudokuLine = [];
        for (let column = 0; column < 9; column += 1) {
          const identifier = `case${line}${column}`;
          const input = document.getElementById(identifier);
          const value = input.value;
          const number = value === "" ? "" : parseInt(value, 10);
          sudokuLine.push(number);
        }
        sudoku.push(sudokuLine);
      }
      // console.log(sudoku);
      // is there any duplicates in the lines - horizontal?
      for (let line = 0; line < 9; line += 1) {
        const list = new Set();
        for (let column = 0; column < 9; column += 1) {
          const value = sudoku[line][column];
          if (value === "") {
            // console.log("lol");
          } else {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square !
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              const input = document.getElementById("case" + line + column);
              input.classList.add("invalid");
              // remove css class when user put some new walu (only once - "once" parameter)
              input.addEventListener(
                "input",
                () => {
                  input.classList.remove("invalid");
                },
                { once: true }
              );
            } else {
              list.add(value);
            }
          }
        }
      }
      // is there any duplicates in the lines - vertical?
      for (let column = 0; column < 9; column += 1) {
        const list = new Set();
        for (let line = 0; line < 9; line += 1) {
          const value = sudoku[line][column];
          if (value === "") {
            // console.log("lol");
          } else {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square !
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              const input = document.getElementById("case" + line + column);
              input.classList.add("invalid");
              // remove css class when user put some new walu (only once - "once" parameter)
              input.addEventListener(
                "input",
                () => {
                  input.classList.remove("invalid");
                },
                { once: true }
              );
            } else {
              list.add(value);
            }
          }
        }
      }
      // checking squares
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
          [2, 2]
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
          [2, 5]
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
          [2, 8]
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
          [5, 2]
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
          [5, 5]
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
          [5, 8]
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
          [8, 2]
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
          [8, 5]
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
          [8, 8]
        ]
      ];
      for (const square of squares) {
        const list = new Set();
        for (const element of square) {
          const line = element[0];
          const column = element[1];
          const value = sudoku[line][column];
          if (value === "") {
            // console.log("lol");
          } else {
            const valueExists = list.has(value);
            // if value exists in the list -> make red square !
            if (valueExists) {
              console.log("Error - double " + line + "-" + column);
              const input = document.getElementById("case" + line + column);
              input.classList.add("invalid");
              // remove css class when user put some new walu (only once - "once" parameter)
              input.addEventListener(
                "input",
                () => {
                  input.classList.remove("invalid");
                },
                { once: true }
              );
            } else {
              list.add(value);
            }
          }
        }
      }
    },
    created() {
      this.getSudoku();
      // this.listOfinputs = document.querySelectorAll("input");
    }
  }
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
/* .yoursudoku {
  text-align: center;
  vertical-align: middle;
} */
table {
  margin: 0 auto;
}
input {
  height: calc(100vh / 14);
  width: calc(100vh / 14);
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
button {
  display: block;
  margin: 1em auto;
  padding: 0.5em 2em;
  font-size: 3vh;
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
</style>
