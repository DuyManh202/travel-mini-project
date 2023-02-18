<template>
  <v-app>

    <v-main>
<Menu ></Menu>
      <v-center>
        <div class="home_header_info" style=" margin-left: -1111px;">
          <h1
            class="typewrite"
            data-period="2000"
            data-type='[ "WELCOME TO ALPINE ASCENTS" ]'
          >
            <span class="wrap">WELCOME TO TRAVEL JAPAN</span>
          </h1>
          <p>Nhật Bản thường được biết đến với cái tên</p>
          <p>Đất nước mặt trời mọc hay xứ sở hoa anh đào</p>
        
        </div>
      </v-center>
      <div class="video">
        <video id="video" autoplay="" loop="" muted="">
          <source
            type="video/mp4"
            src="../assets/img/Kyoto Autumn - Japan.mp4"/>
        </video>
      </div>
    </v-main>
    <v-container> </v-container>
    <h2 class="text-center">Các địa điểm Japan nổi tiếng</h2>
    <div>
      <maps></maps>
    </div>
    <div>
      <v-app>
        <v-timeline direction="horizontal">
          <v-timeline-item>
            <template v-slot:opposite> Văn Hóa Ẩm Thực Nhật Bản </template>
            <div>
              <p>
                Nhắc đến ẩm thực Nhật Bản, ai cũng nghĩ ngay tới món ăn nổi
                tiếng nhất là món Sushi được chế biến bằng nhiều nguyên liệu
                khác nhau như tôm, cá, cua… gói cùng cơm trộn với giấm, đường,
                muối… Sushi rất đa dạng nhưng điểm chung không thay đổi giữa các
                loại đó là phần cơm trộn giấm. Món ngon nổi tiếng Nhật Bản có
                Sushi & Sashimi, Tempura, mỳ Udon, mỳ Soba, mỳ Ramen… Nếu có cơ
                hội đi tour du lịch Nhật Bản trọn gói, bạn nên thưởng thức những
                món ăn đặc sản ngon nức tiếng tại xứ sở hoa anh đào này.
              </p>
            </div>
          </v-timeline-item>

          <v-timeline-item>
            <template v-slot:opposite> Trang Phục Truyền Thống </template>
            <div>
              <p>
                Trang phục Kimono. Có hai loại Kimono: Tay rộng và tay ngắn, tùy
                vào sở thích của người muốn mặc để lựa chọn. Bên cạnh Kimono,
                người Nhật còn mặc Yukata được làm bằng vải cotton nhẹ nhàng,
                thoáng khí và đặc biệt dành riêng cho muà hè. Nhưng Yukata không
                được phép mặc ra những chỗ trịnh trọng đông người, vì nó giống
                như quần áo ngủ theo phong cách cổ xưa.
              </p>
            </div>
          </v-timeline-item>

          <v-timeline-item>
            <template v-slot:opposite> Văn Hoá Trà Đạo </template>
            <div>
              <p>
                Trà đạo là một trong những nét văn hóa đặc trưng của người Nhật
                bởi sự cầu kỳ, tinh tế của nó khiến cho cả thế giới phải nghiêng
                mình thán phục. Văn hóa trà đạo của Nhật không chỉ đơn thuần là
                những phép tắc pha trà và uống trà mà thông qua đó người Nhật
                muốn tìm thấy giá trị tinh thần cần có của bản thân. Tinh thần
                trà đạo được biết đến qua 4 chữ Hòa – Kính – Thanh – Tịnh. Trong
                đó, “Hòa” là sự hài hòa giữa con người và thiên nhiên; “kính” là
                tôn trọng người trên, yêu thương bố mẹ, bạn bè, con cháu;
                “Thanh” là tâm hồn thanh tịnh, thanh khiết còn “Tịnh” có nghĩa
                là sự yên tĩnh, vắng lặng mang đến cho con người cảm thấy nhẹ
                nhàng, tĩnh lặng.
              </p>
            </div>
          </v-timeline-item>
        </v-timeline>
        <h2 class="text-center">Ảnh Nổi Bật</h2>

        <v-container fluid>
          <v-row dense>
            <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
              <v-card class="mx-auto" max-width="270">
                <v-img :src="card.src" height="200px" cover>
                  <v-card-title
                    class="text-white"
                    v-text="card.title"
                  ></v-card-title>
                </v-img>

                <v-card-actions>
                  <v-spacer></v-spacer>

                  <v-btn
                    size="small"
                    color="surface-variant"
                    variant="text"
                    icon="mdi-heart"
                  ></v-btn>

                  <v-btn
                    size="small"
                    color="surface-variant"
                    variant="text"
                    icon="mdi-bookmark"
                  ></v-btn>

                  <v-btn
                    size="small"
                    color="surface-variant"
                    variant="text"
                    icon="mdi-share-variant"
                  ></v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-app>
    </div>

    <div>
      <end></end>
    </div>
  </v-app>
</template>

<script>
import maps from "../components/maps.vue";
import End from "../components/End.vue";
import Menu from "@/views/Menu.vue";


export default {
  components: {
    maps,
    End,
    Menu,
  },
  data: () => ({
    cards: [
      {
        title: "TOKYO",
        src: "https://i.pinimg.com/736x/2a/38/f1/2a38f1ce8c8d7e738711079d85083ee2.jpg",
        flex: 12,
      },
      {
        title: "Saitama",
        src: "https://content.fun-japan.jp/renewal-prod/cms/articles/content/shutterstock757821565jpg_2020-12-08-03-57-48.jpg",
        flex: 6,
      },
      {
        title: "FUKUOKA",
        src: "https://znews-photo.zingcdn.me/w660/Uploaded/mdf_eioxrd/2018_10_27/8.jpg",
        flex: 6,
      },
    ],
  }),
};
</script>

<style scoped>
.v-main {
  background-color: red;
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 200px;
  position: relative;
  background-color: rgba(0, 0, 0, 0.5);
  background-blend-mode: overlay;
  color: #fff;
}

.video {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

#video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

nav {
  position: fixed;
  z-index: 99;
  width: 100%;
  padding: 30px 0;
  transition: all 0.5s ease;
}

.nav-fixed {
  background-color: #fff;
  padding: 10px 0;
  box-shadow: 2px 2px 10px #bbb;
}

.nav-fixed h2 {
  color: #00a8b4 !important;
}

.nav-fixed .nav ul a {
  color: #00a8b4;
}

.menu-par {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav ul li {
  display: inline-block;
}

.nav ul a {
  color: #fff;
  padding: 10px;
  position: relative;
}

.nav ul a:before {
  content: "s";
  background-color: #00a8b4;
  position: absolute;
  top: 0;
  width: 0%;
  height: 2px;
  font-size: 0px;
  left: 10px;
  transition: all 0.5s ease;
}

.nav ul a:hover:before {
  width: 74%;
}

.home_header_info h1 {
  font-size: 45px;
  padding: 20px 0px;
  letter-spacing: 4px;
  text-transform: uppercase;
  font-weight: bold;
}

.logo-par h2 {
  color: #fff;
  font-size: 40px;
}

.home_header_info p {
  font-size: 15px;
  line-height: 30px;
  width: 80%;
  margin: 0 auto;
}

.home_header_info a {
  background-color: #fff;
  color: #00a8b4;
  text-decoration: none;
  padding: 17px 45px;
  margin-top: 25px;
  display: inline-block;
  font-size: 14px;
  position: relative;
  overflow: hidden;
}

.home_header_info a:hover {
  color: #fff;
}

.home_header_info a:after {
  content: "Read More";
  background-color: #00a8b4;
  width: 0%;
  font-size: 15px;
  height: 100%;
  line-height: 50px;
  color: #fff;
  position: absolute;
  top: 0;
  left: 0;
  transition: all 0.5s ease;
  right: 0;
}

.home_header_info a:hover:after {
  width: 100%;
}

.toggle-btn {
  display: none;
  color: #fff;
}
</style>
