<template>
    <v-app id="app">
    <div class="container orange pullUpDown">
      <v-app-bar >
        <v-toolbar-title>
                 <v-avatar
                  class="ma-3"
                  size="121"
                  rounded="0">
    <v-img src="https://www.otani.vn/images/logo.svg"></v-img>
                </v-avatar>
        </v-toolbar-title>
          <v-spacer class="d-flex align-center">
          <v-btn :to='{name: "home"}' >Home</v-btn>
          <v-btn :to='{name: "blog"}' >Blog</v-btn>
          <v-btn :to='{name: "login"}' >
            <v-icon    icon="mdi-account-circle" ></v-icon>
          </v-btn>  
          <v-btn :to='{name: "travel"}'>Travel</v-btn>
          <v-btn :to='{name: "contact"}'>Contact</v-btn>
        </v-spacer>
      </v-app-bar>
    </div>
      <v-main class="fill-height">
        <router-view></router-view>
      </v-main>
  </v-app>
</template>
<script>
export default {
  setup() {
    const goTo = (to) => {
      console.log(to)
    }
    return {goTo}
  }
}
</script>
<style scoped>
div.pullUpDown a:before, div.pullUpDown a:after
{
    position: absolute;
    width: 100%;
    height: 2px;
    left: 0px;
    content: '';
    background: rgba(252, 251, 251, 0.878);
    opacity: 0.3;
    transition: all 0.3s;
}

div.pullUpDown a:before
{
    top: 0px;
} 

div.pullUpDown a:after
{
    bottom: 0px;
}

div.pullUpDown a:hover:before, div.pullUpDown a:hover:after
{
    height: 100%;
}

/* Pull right and left  */
div.pullRightLeft a:before, div.pullRightLeft a:after
{
    position: absolute;
    width: 2px;
    height: 100%;
    top: 0px;
    content: '';
    background: rgba(214, 12, 12, 0.07);
    opacity: 0.3;
    transition: all 0.3s;
}

div.pullRightLeft a:before
{
    left: 0px;
} 

div.pullRightLeft a:after
{
    right: 0px;
}

div.pullRightLeft a:hover:before, div.pullRightLeft a:hover:after
{
    width: 100%;
}


</style>