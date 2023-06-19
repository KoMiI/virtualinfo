<template>
    <div>
        <h1>Скрипты</h1>
        <div class="form-wrapper">
            <form @submit.prevent="uploadScript">
                <p>Добавить скрипт</p>
                <p><input type="text" name="name" v-model="form.name" placeholder="Имя скрипта"/></p>
                <p><textarea v-model="form.script" placeholder="Скрипт"></textarea></p>
                <p><input type="submit" value="Отправить"/></p>
            </form>
        </div>
        <div id="keylist">
            <div class="wrapper" v-for="key in scripts" :key="key.id">
                <div class="item-id">{{ key.id }}</div>
                <div class="item-name">{{ key.name }}</div>
                <div class="item-meta"><pre>{{ key.script }}</pre></div>
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
                script: "",
                freezed: false,
            },
            scripts: [
            ]
        }
    },
    methods: {
        async loadScripts() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "scripts", {credentials: "include"})).json()
            console.log(ans)
            this.scripts = ans.data
        },
        async uploadScript() {
            let payload = {
                name: this.form.name,
                script: this.form.script,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "scripts", {
                credentials: "include",
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadScripts()
        },
        async del(id) {
            let payload = {
                id: id,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "scripts", {
                credentials: "include",
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadScripts()
        }
    },
    mounted() {
        this.loadScripts();
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
