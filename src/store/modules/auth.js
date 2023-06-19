export default {
    namespaced:true,
    state:{
        loggedIn: false,
        login: ""

    },
    actions: {
        async checkLogin (ctx){
            let ans = await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "/login", {credentials: "include"})
            if (ans.status == 200) {
                ans = await ans.json()
                console.log(ans)
                ctx.commit("setState", {loggedIn:ans["loggedin"], login:ans["login"]})
            }
            else {
                ctx.commit("setState", {loggedIn: false, login: ""})
            }
        },
        async loginAction(ctx, data) {
            let payload = {login:data.login, password:data.password}
            let ans
            try {
                ans = await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "login", {
                    credentials: "include",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(payload)
                })
            }
            catch {
                return false
            }
            if (ans.status == 200) {
                ctx.commit("setState", {loggedIn: true, login: data.login})
                return true
            }
            return false
        },
        async logoutAction(ctx) {
            let ans = await fetch(process.env.VUE_APP_API_BASE_ADDRESS + "login", {
                credentials: "include",
                method: "DELETE",
            })
            if (ans.status == 200) {
                ctx.commit("setState", {loggedIn: false, login: ""})
                return true
            }
            return false
        }
    },
    mutations: {
        setState(state, payload) {
            state.loggedIn = payload.loggedIn
            state.login = payload.login
        }
    },
    getters: {
        isLoggedIn (state){
            return state.loggedIn
        },
        getLogin (state) {
            return state.login
        }
    },
}
