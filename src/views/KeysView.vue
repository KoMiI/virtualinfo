<template>
    <div>
        <h1>Ключи</h1>
        <div class="form-wrapper">
            <form @submit.prevent="uploadKey">
                <p>Добавить ключ</p>
                <p><input type="text" name="name" v-model="form.name" placeholder="Имя ключа"/></p>
                <p><textarea v-model="form.private_key" placeholder="Приватный ключ"></textarea></p>
                <p><textarea v-model="form.public_key" placeholder="Публичный ключ"></textarea></p>
                <p><input type="submit" value="Отправить"/></p>
            </form>
        </div>
        <div id="keylist">
            <div class="wrapper" v-for="key in keys" :key="key.id">
                <div class="item-id">{{ key.id }}</div>
                <div class="item-name">{{ key.name }}</div>
                <div class="item-meta">{{ key.pub_key }}</div>
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
                private_key: "",
                public_key: "",
                freezed: false,
            },
            keys: [
            ]
        }
    },
    methods: {
        async loadKeys() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "keys", {credentials: "include"})).json()
            console.log(ans)
            this.keys = ans.data
        },
        async uploadKey() {
            let payload = {
                name: this.form.name,
                key: this.form.private_key,
                pub_key: this.form.public_key,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "keys", {
                credentials: "include",
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadKeys()
        },
        async del(id) {
            let payload = {
                id: id,
            }
            await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "keys", {
                credentials: "include",
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            this.loadKeys()
        }
    },
    mounted() {
        this.loadKeys();
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
    max-width: 200px;
    word-break: keep-all;
    overflow: hidden;
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
