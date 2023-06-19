<template>
    <div>
        <h1>Сервера</h1>
        <div class="form-wrapper">
            <form @submit.prevent="uploadServers">
                <p>Добавить сервер</p>
                <p><input type="text" name="name" v-model="form.name" placeholder="Имя сервера"/></p>
                <p><input type="text" name="name" v-model="form.host" placeholder="Хост"/></p>
                <p><input type="number" name="name" v-model="form.port" placeholder="Порт"/></p>
                <p><input type="text" name="name" v-model="form.login" placeholder="Логин"/></p>
                <p>
                    <select v-model="form.key_id">
                        <option v-for="key in keys" :value="key.id" :key="key.id">{{ key.name }}</option>
                    </select>
                </p>
                <p>
                    <select v-model="form.script_id">
                        <option v-for="key in scripts" :value="key.id" :key="key.id">{{ key.name }}</option>
                    </select>
                </p>
                <p><input type="submit" value="Отправить"/></p>
            </form>
        </div>
        <div id="keylist">
            <div class="wrapper" v-for="key in servers" :key="key.id">
                <div class="item-id">{{ key.id }}</div>
                <div class="item-name">{{ key.name }}</div>
                <div class="item-name">{{ key.host }}</div>
                <div class="item-name">{{ key.port }}</div>
                <div class="item-name">{{ key.user_login }}</div>
                <div class="delete" @click="del(key.id)">Удалить</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: "",
                host: "",
                port: 22,
                login: "",
                key_id: "",
                script_id: "",
                freezed: false,
            },
            scripts: [],
            servers: [],
            keys: [],
        }
    },
    methods: {
        async loadScripts() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "scripts", {credentials: "include"})).json()
            console.log(ans)
            this.scripts = ans.data
        },
        async loadKeys() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "keys", {credentials: "include"})).json()
            console.log(ans)
            this.keys = ans.data
        },
        async loadServers() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "servers", {credentials: "include"})).json()
            console.log(ans)
            this.servers = ans.data
        },
        async uploadServers() {
            let payload = {
                name: this.form.name,
                host: this.form.host,
                port: this.form.port,
                user_login: this.form.login,
                key_id: this.form.key_id,
                script_id: this.form.script_id,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "servers", {
                credentials: "include",
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadServers()
        },
        async del(id) {
            let payload = {
                id: id,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "servers", {
                credentials: "include",
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadServers()
        }
    },
    mounted() {
        this.loadScripts()
        this.loadKeys()
        this.loadServers()
    }
}
</script>

<style scoped>
.wrapper {
    display: flex;
    justify-content: space-between;
    padding: 2px;
    border-bottom: 1px solid gray;
}
.wrapper > div {
    padding: 10px;
}
.item-id {
    flex-grow: 0;
}
.item-meta {
    max-width: 400px;
    max-height: 200px;
    word-break: keep-all;
    overflow: auto;
    display: inline-block;
}
.delete {
    border: 1px solid #F92D2D;
    color: #F92D2D;
    cursor: pointer;
    padding: 10px;
}
.delete:hover {
    color: white;
    background-color: #F92D2D;
}
</style>
