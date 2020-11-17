import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import YourSudoku from "../views/YourSudoku.vue";
import OneSudoku from "../views/OneSudoku.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/yoursudoku/:slug",
    name: "OneSudoku",
    component: OneSudoku,
    props: true,
  },
  {
    path: "/yoursudoku",
    name: "YourSudoku",
    component: YourSudoku,
  },
  {
    path: "*",
    name: "PageNotFound",
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
