<template>
    <v-app id="app">
      <v-app-bar >
        <v-toolbar-title>Travel Japan</v-toolbar-title>
          <v-spacer class="d-flex align-center">
          <v-btn :to='{name: "home"}' rounded>Home</v-btn>
          <v-btn text rounded>Travel</v-btn>
          <v-btn :to='{name: "login"}' >
            <v-icon icon="mdi-account-circle" ></v-icon>
          </v-btn>  
          <v-btn text rounded>Blog</v-btn>
          <v-btn text rounded>Contact</v-btn>
        </v-spacer>
      </v-app-bar>
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

  
</style>