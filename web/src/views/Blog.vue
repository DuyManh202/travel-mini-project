<template>
  <div>

    <v-card class="banner">
      <Menu></Menu>
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
              v-for="(items, i) in items"
              :key="i"
              :src="items.src"
              cover
            >
            </v-carousel-item>
          </v-carousel>
        </v-col>
        <v-col>
          <v-card v-for="(Blogs, i) in Blog" :key="i">
            <v-card-item>
              <div class="d-flex">
                <v-img class="img" :src="Blogs.src" height="124px "></v-img>
                <div class="text-overline mb-1 pa-2">
                  <div class="text-h6 mb-2">{{ Blogs.title }}</div>
                  <div class="text-caption">
                    {{ Blogs.subtitle }}
                  </div>
                </div>
              </div>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-card>

    <div>
      <cuisine :hotels="hotels" :travels="travel" :cuisines="cuisine"></cuisine>
    </div>
    <div>
      <end></end>
    </div>
  </div>
</template>
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
  min-width: 75%;
}
</style>
<script>
import cuisine from "../components/cuisine.vue";
import End from "../components/End.vue";
import Menu from "@/views/Menu.vue";

export default {
  components: {
    cuisine,
    End,
    Menu,
  },
  data: () => ({
    items: [
      {
        src: "https://tourdanangcity.vn/wp-content/uploads/2020/11/tour-nhat-ban-tu-da-nang-2-1.jpg",
      },
      {
        src: "https://cdn3.ivivu.com/2019/06/giao-lo-noi-hang-trieu-nguoi-qua-duong-mot-ngay-o-tokyo-ivivu-2.jpg",
      },
      {
        src: "https://wallpaperaccess.com/full/16223.jpg",
      },
    ],
    Blog: [
      {
        src: "https://datviettour.com.vn/uploads/images/tin-tuc/danh-muc-tour-tour-ngoai-nuoc/du-lich-nhat-ban/den-itsukushima.jpg",
        title: "CỔNG NỔI Ở MIẾU ITSUKUSHIMA",
        subtitle:
          "Đền Itsukushima rất ấn tượng với vẻ đẹp quyến rũ và màu đỏ son nổi trên biển đã được chỉ định là bảo vật quốc gia của Nhật Bản. Điện chính nằm ở tòa nhà chính của đền thần hiện đang thờ 3 vị thần nữ giới (※1). Khoảng cách giữa cổng Torii và điện chính khoảng 160m. ",
      },
      {
        title: "ĐỀN KINKAKU-JI",
        src: "https://datviettour.com.vn/uploads/images/tin-tuc/danh-muc-tour-tour-ngoai-nuoc/du-lich-nhat-ban/chua-vang-kinkakuji.jpg",
        subtitle:
          "Kinkakuji là một cấu trúc ấn tượng được xây dựng xung quanh một cái hồ lớn, và là tòa nhà duy nhất còn lại trong các khu nghỉ dưỡng của Yoshimitsu. Tầng đầu tiên của Kinkakuji được xây dựng theo phong cách Shinden",
      },
      {
        title: "SHINJUKU",
        src: "https://datviettour.com.vn/uploads/images/tin-tuc/danh-muc-tour-tour-ngoai-nuoc/du-lich-nhat-ban/shinjuku.jpg",
        subtitle:
          "Đứng trên tầng áp mái của những ngôi nhà chọc trời ở Shinjuku, ",
      },
    ],
    Title: [
      {
        title: "Blog cuisine 1",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "cuisine",
        comment_number: 2,
      },
      {
        title: "Blog travel 2",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "travel",
        comment_number: 2,
      },
      {
        title: "Blog cuisine 2",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "cuisine",
        comment_number: 3,
      },
      {
        title: "Blog hotel 1",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "hotel",
        comment_number: 7,
      },
      {
        title: "Blog travel 1",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "travel",
        comment_number: 1,
      },
      {
        title: "Blog hotel 2",
        src: "https://wallpaperaccess.com/full/16223.jpg",
        subtitle: "test",
        type: "hotel",
        comment_number: 7,
      },
    ],
  }),
  computed: {
    hotels() {
      const hotels = this.Title.filter((item) => item.type === "hotel");
      return hotels;
    },
    travel() {
      const travel = this.Title.filter((items) => items.type === "travel");
      return travel;
    },
    cuisine() {
      const cuisine = this.Title.filter((item) => item.type === "cuisine");
      return cuisine;
    },
  },
};
</script>
