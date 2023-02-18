// @ts-nocheck
import { createRouter, createWebHistory } from "vue-router";

import Login from "../components/Login.vue";
import HomeView from "../views/HomeView.vue";
import Blog from "../views/Blog.vue";
import Travel from "../views/Travel.vue";
import Contact from "../views/Contact.vue";
import Register from "../components/Register.vue";
import blogs1 from "../components/blogs1.vue";
import blogs2 from "../components/blogs2.vue";
import blogs3 from "../components/blogs3.vue";
import commentMagement from "../admin/commentMagement.vue";
import addBlogs from "../admin/addBlogs.vue";
import addTravel from "../admin/addTravel.vue";
import managerBlog from '../admin/managerBlog.vue';
import managerTravel from "../admin/managerTravel.vue"
const router = createRouter({
    history: createWebHistory(
        // @ts-ignore
        import.meta.env.BASE_URL
    ),
    routes: [{
            path: "/",
            name: "home",
            component: HomeView,
        },

        {
            path: "/login",
            name: "login",
            component: Login,
        },

        {
            path: "/register",
            name: "register",
            component: Register,
        },
        {
            path: "/blog",
            name: "blog",
            component: Blog,
        },
        {
            path: "/travel",
            name: "travel",
            component: Travel,
        },
        {
            path: "/contact",
            name: "contact",
            component: Contact,
        },
        {
            path: "/blogs1",
            name: "blogs1",
            component: blogs1,
        },
        {
            path: "/blogs2",
            name: "blogs2",
            component: blogs2,
        },
        {
            path: "/blogs3",
            name: "blogs3",
            component: blogs3,
        },
        {
            path: "/magement",
            name: "magement",
            component: commentMagement,
        },
        {
            path: "/addBlogs",
            name: "addBlogs",
            component: addBlogs,
        },
        {
            path: "/addTravel",
            name: "addTravel",
            component: addTravel,

        },
        {
            path: "/managerBlog",
            name: "managerBlog",
            component: managerBlog,
        },

        {
            path: "/managerTravel",
            name: "managerTravel",
            component: managerTravel,
        },
    ],
});

export default router;