import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'

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
            path: '/about',
            name: 'about',
            component: AboutView
        }
    ]
})

export default router