.
<template>
  
    <v-row>
      <v-container>
        <v-col class="style1">
          <v-carousel
            cycle
            hide-delimiter-background
            :show-arrows="'hover'"
            cover
          >
            <v-carousel-item
              cycle
              v-for="(items, i) in items"
              :key="i"
              :src="items.src"
              cover
              rounded="lg"
            ><footer>
              <h2></h2>
            </footer>
            </v-carousel-item>
          </v-carousel>
        </v-col>

        <v-col></v-col>
        <footer style="margin-top: -85px; margin-left: 12px" rounded="lg">
          <p class="text">Món ăn nhất định phải thử</p>
        </footer>
      </v-container>
    </v-row>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        src: "https://imgs.vietnamnet.vn/Images/2017/09/26/12/20170926122146-mon-an-nhat-1.jpg",
      },
      {
        src: "https://tokyometro.vn/wp-content/uploads/2022/07/1658105509_729_7-thien-duong-cho-tin-do-am-thuc-o-Nhat.jpg",
      },
      {
        src: "https://wallpaperaccess.com/full/16223.jpg",
      },
    ],
  }),
};
</script>

<style scoped>
.text {
  margin-top: 20px;
  max-width: 280px;
  margin-left: 11px;
  text-align: center;
  background-color: #070e0f;
  color: #fff;
  padding: 14px 0px;
  margin: 50px 0px 0px 0px;
}
</style>
>
