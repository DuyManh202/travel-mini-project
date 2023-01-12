// @ts-nocheck
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import HomeView from '../views/HomeView.vue'
import Blog from '../views/Blog.vue'
import Travel from '../views/Travel.vue'
import Contact from '../views/Contact.vue'


const router = createRouter({
    history: createWebHistory(
        // @ts-ignore
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'home',
            component: HomeView
        },

        {

            path: '/login',
            name: 'login',
            component: Login
        },

        {
            path: '/blog',
            name: 'blog',
            component: Blog
        },
        {
            path: '/travel',
            name: 'travel',
            component: Travel
        },
        {
            path: '/contact',
            name: 'contact',
            component: Contact
        }
    ]
})

export default router