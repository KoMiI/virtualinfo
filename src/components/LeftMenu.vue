<template>
    <div id="left-menu-container">
        <div id="left-menu-logo-container">
            <img src="/static/img/PostgresPro_logo.svg" alt="PPG_LOGO" />
            <div style="position: absolute; right: 22px; bottom: 50px;">QA</div>
        </div>
        <div>
            <ul id="menu">
                <router-link v-for="menuitem in menu.items" :to="menuitem.path" :key="menuitem">
                    <li>
                        <span class="menu-icon"><img v-if="menuitem.icon != ''" :src="menuitem.icon" :alt="menuitem.name" /></span>
                        {{ menuitem.name }}
                    </li>
                </router-link>
            </ul>
        </div>
    </div>
  </template>
  
  <script>
    
  export default {
      data() {
          return {
              menu: {
                  isFull: true,
                  items: [
                      {
                          name: "Виртуальные машины",
                          path: {name: "home"},
                          icon: "",
                      },
                      {
                          name: "Сервера",
                          path: "/vm/servers",
                          icon: "",
                      },
                      {
                          name: "Обработчики",
                          path: "/vm/scripts",
                          icon: "",
                      },
                      {
                          name: "Ключи",
                          path: "/vm/keys",
                          icon: "",
                      },
                  ]
              },
          }
      },
      computed: {
      },
      methods: {
      }
  }
  </script>
  
<style scoped>
#left-menu-container {
    width: 224px;
    flex-grow: 0 !important;
    background-color: #272C31;
    color: #C1CEDB;
    font-family: Arial, Helvetica, sans-serif;
}

#left-menu-logo-container {
    position: relative;
}

#left-menu-logo-container > img {
    margin: 20px 20px;
    width: 184px;
}

#menu {
    padding: 0;
    position: relative;
}

#menu a {
    text-decoration: none;
    color: #C1CEDB;
}

#menu li {
    list-style: none;
    height: 48px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    text-decoration: none;
    position: relative;
}

#menu .router-link-exact-active li {
    background-color: #0BA6F5;
}

#menu li:hover {
    list-style: none;
    height: 48px;
    background-color: #0BA6F5;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    text-decoration: none;
}


</style>
  