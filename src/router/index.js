import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ServersView from '../views/ServersView.vue'
import ScriptsView from '../views/ScriptsView.vue'
import KeysView from '../views/KeysView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/vm/servers',
    name: 'servers',
    component: ServersView
  },
  {
    path: '/vm/scripts',
    name: 'vmscripts',
    component: ScriptsView
  },
  {
    path: '/vm/keys',
    name: 'keys',
    component: KeysView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
