<template>
  <div>
    <Menu></Menu>
    <v-card class="banner">
      <v-row>
        <v-col class="style1">
          <v-carousel
            cycle
            hide-delimiter-background
            :show-arrows="'hover'"
            cover
          >
            <v-carousel-item
              cycle
              v-for="(Travels, i) in Travel"
              :key="i"
              :src="Travels.src"
              cover
            >
            </v-carousel-item>
          </v-carousel>
        </v-col>
        <v-col>
          <v-card v-for="(Blogs, i) in Blog" :key="i">
            <v-card-item>
              <div class="d-flex">
                <v-img :src="Blogs.src" height="124px" width="2px"></v-img>
                <div class="text-overline mb-1">
                  <div class="text-h6 mb-1">{{ Blogs.title }}</div>
                  <div class="d-flex justify-space-evenly">
                    <div class="text-caption">
                      <v-icon icon="mdi-antenna" size="x-large"></v-icon>
                      {{ Blogs.subtitle }}
                    </div>
                    <div class="text-caption">
                      <v-icon icon="mdi-antenna" size="x-large"></v-icon>
                      {{ Blogs.subtitle }}
                    </div>
                  </div>
                </div>
              </div>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
    <div class="end"><End></End></div>
  </div>
</template>

<script>
import End from "../components/End.vue";
import Menu from "@/views/Menu.vue";

export default {
  components: {
    End,
    Menu,
  },
  data: () => ({
    Travel: [
      {
        src: "https://s3-ap-northeast-1.amazonaws.com/thegate/2021/06/19/01/01/02/Tsukishima%20monja%20street_600x400.jpg",
      },
      {
        src: "https://luhanhliendaiduong.vn/wp-content/uploads/2017/09/Th%E1%BB%A7-%C4%91%C3%B4-kyoto-1-1-1140x530.jpg",
      },
      {
        src: "https://atta.ai/media/en/wp-content/uploads/2021/06/Main-Picture.jpg",
      },
    ],
    Blog: [
      {
        src: "https://brandcom.vn/wp-content/uploads/2018/04/tap-chi-tieng-nhat-6.jpg",
        title: "HERITAGE",
        subtitle: "bai viet",
      },
      {
        title: "noi dung",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        
      },
      {
        title: "noi dung",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
      },
    ],
  }),
};
</script>

<style scoped>
.banner {
  padding: 12px;
}
/* flexbox */
.f-grid {
  display: flex;
  justify-content: space-between;
  margin-left: -1rem;
  flex-flow: row wrap;
}
.f-grid-col {
  flex: 1 0;
  margin-left: 1rem;
  margin-bottom: 1rem;
  padding: 1rem;
}
.style1 {
  background-color: rgb(255, 241, 241);
  border: 2px;
  border-radius: 25px;
  padding: 0 !important;
  overflow: hidden;
  height: 400px;
  margin-top: 33px;
}
.banner {
  padding: 20px;
  background-color: rgb(253, 241, 241);
  height: auto;
  width: auto;
}
.test {
  width: 250px;
  height: 150px;
}
.img {
  max-width: 25%;
}
.text-overline {
  max-width: 75%;
  min-width: 65%;
}
.end {
  margin-top: 157px;
}
.btn {
  margin-left: 300px;
  margin-top: 12px;
}
</style>
