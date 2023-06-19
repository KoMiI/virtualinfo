<template>
  <div id="application-level">
        <left-menu />
        <div id="main-section">
            <top-menu />
            <router-view id="main" v-if="isLoggedIn"/>
            <div v-else><h1>Для просмотра страниц необходимо авторизоваться</h1></div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import LeftMenu from './components/LeftMenu.vue'
import TopMenu from './components/TopMenu.vue'

export default {
    data() {
        return {
            s: ""
        }
    },
    computed: {
        ...mapGetters('Auth', ['isLoggedIn']),
    },
    methods: {
        ...mapActions('Auth', ['checkLogin'])
    },
    mounted() {
        this.checkLogin()
    },
    components: {
        LeftMenu, TopMenu
    }
}
</script>

<style>

</style>
