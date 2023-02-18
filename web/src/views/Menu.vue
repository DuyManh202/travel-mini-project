<template>
  <v-container>
      <v-app-bar>
        <v-toolbar-title>
          <v-avatar class="ma-3" size="121" rounded="0">
            <v-img src="https://www.otani.vn/images/logo.svg"></v-img>
          </v-avatar>
        </v-toolbar-title>
        <v-spacer class="d-flex align-center">
          <v-btn :to="{ name: 'home' }">Home</v-btn>
          <v-btn :to="{ name: 'blog' }">Blog</v-btn>
          <v-btn :to="{ name: 'login' }">
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-btn>
          <v-btn :to="{ name: 'travel' }">Travel</v-btn>
          <v-btn :to="{ name: 'contact' }">Contact</v-btn>
        </v-spacer>
      </v-app-bar>
  </v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>