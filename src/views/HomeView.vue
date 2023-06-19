<template>
    <div>
        <h1>Виртуальные машины</h1>
        <div class="form-wrapper">
            
        </div>
        <div class="delete">Удалить выделенные</div>
        <div id="keylist">
            <div class="wrapper" v-for="key in vms" :key="key.name">
                <div class="item-id"><input type="checkbox" v-if="!key.isreserved"></div>
                <div class="item-name">{{ key.status }}</div>
                <div class="item-name">{{ key.name }}</div>
                <div class="item-name">{{ key.server }}</div>
                <div class="delete" @click="del(key.id)" v-if="!key.isreserved">Удалить</div>
                <div class="reserve" @click="del(key.id)">Зарезервировать</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                server_id: -1,
                name: "",
                until_date: "",
                until_time: "",
                freezed: false,
            },
            servers: [],
            vms: [
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--rhel-9-29924", "status": "paused"},
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--rocky-9-29890", "status": "paused"},
                {"isreserved":true, "server": "tstfrm2", "name": "pgt--debian-9-1383", "status": "paused"},
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--oraclelinux-8-16394", "status": "running"},
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--sles-15-29486", "status": "running"},
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--alteros-7-25553", "status": "running"},
                {"isreserved":false, "server": "tstfrm2", "name": "pgt--altlinux-8-18185", "status": "running"},
                {"isreserved":true, "server": "tstfrm3", "name": "pgt--debian-11-9132", "status": "paused"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--alt-sp-8.4-25628", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--alma-9-22141", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--rocky-9-12205", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--altlinux-10-17762", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--astra-orel-2.12-32760", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--ubuntu-23.04-19599", "status": "running"},
                {"isreserved":true, "server": "tstfrm3", "name": "pgt--ubuntu-22.04-17251", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--rhel-8-11327", "status": "running"},
                {"isreserved":false, "server": "tstfrm3", "name": "pgt--redos-7.3-28216", "status": "running"}
            ],
            vm_reserve: [],
        }
    },
    methods: {
        async loadServers() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "servers", {credentials: "include"})).json()
            console.log(ans)
            this.servers = ans.data
        },
        async loadReserve() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "vm_reserve", {credentials: "include"})).json()
            console.log(ans)
            this.servers = ans.data
        },
        async loadVms() {
            let ans = await (await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "vm", {credentials: "include"})).json()
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
        // this.loadScripts()
        // this.loadKeys()
        // this.loadServers()
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
.item-name {
    flex-grow: 1;
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
.reserve {
    border: 1px solid #2c95d1;
    color: #2c95d1;
    cursor: pointer;
    padding: 10px;
}
.reserve:hover {
    color: white;
    background-color: #2c95d1;
}
</style>
