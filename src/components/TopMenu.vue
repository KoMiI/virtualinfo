<template>
    <div id="top-menu-container">
        <div v-if="isLoggedIn">Вы вошли под пользователем {{ getLogin }} <button @click.prevent="logout">Выйти</button></div>
        <div v-else>
            <div v-if="processed">Загрузка...</div>
            <div v-else-if="uncorrect">Неверные пользователь или пароль</div>
            <div class="login-form" v-else>
                <form @submit.prevent="tryLogin">
                    <input placeholder="Логин" type="text" name="login" v-model="login" />
                    <input placeholder="Пароль" type="password" name="password" v-model="password" />
                    <input type="submit" value="Войти" />
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data() {
        return {
            login: "",
            password: "",
            processed: false,
            uncorrect: false
        }
    },
    computed: {
        ...mapGetters('Auth', ['isLoggedIn', "getLogin"]),
    },
    methods: {
        ...mapActions('Auth', ['loginAction', 'logoutAction']),
        async tryLogin() {
            this.processed = true
            let res = await this.loginAction({login: this.login, password: this.password})
            this.processed = false
            if (!res) {
                this.uncorrect = true
                setTimeout(()=>this.uncorrect = false, 1000)
            }
        },
        logout() {
            this.logoutAction()
        }
    }
}
</script>

<style scoped>
#top-menu-container {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
