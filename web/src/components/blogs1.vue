<template>
  <div class="max">
    <v-container>
      <v-row dense>
        <v-col cols="12">
          <v-card v-for="(Blogs, i) in Blog" :key="i">
            <v-card-item>
              <div class="d-flex">
                <v-img
                  class="img"
                  :src="Blogs.src"
                  height="124px"
                  width="2px"
                ></v-img>
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
      </v-row></v-container
    >
  </div>
</template>

<script>
export default {
  data: () => ({
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
.max {
  padding: 109px;
  background-color: rgb(0, 0, 0);
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
.img {
  max-width: 25%;
}
</style>
