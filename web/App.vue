<template>
  <v-app id="app">
   
      <v-main class="fill-height">
        <router-view></router-view>
      </v-main>
  </v-app> 
</template>
<script>
export default {
  setup() {
    const goTo = (to) => {
      console.log(to);
    };
    return { goTo };
  },
};
</script>
<style scoped>
div.pullUpDown a:before,
div.pullUpDown a:after {
  position: absolute;
  width: 100%;
  height: 2px;
  left: 0px;
  content: "";
  background: rgba(184, 184, 184, 0);
  opacity: 0.3;
  transition: all 0.3s;
}

div.pullUpDown a:before {
  top: 0px;
}

div.pullUpDown a:after {
  bottom: 0px;
}

div.pullUpDown a:hover:before,
div.pullUpDown a:hover:after {
  height: 100%;
}

/* Pull right and left  */
div.pullRightLeft a:before,
div.pullRightLeft a:after {
  position: absolute;
  width: 2px;
  height: 100%;
  top: 0px;
  content: "";
  background: rgba(255, 255, 255, 0.07);
  opacity: 0.3;
  transition: all 0.3s;
}

div.pullRightLeft a:before {
  left: 0px;
}

div.pullRightLeft a:after {
  right: 0px;
}

div.pullRightLeft a:hover:before,
div.pullRightLeft a:hover:after {
  width: 100%;
}
</style>
