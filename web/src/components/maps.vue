.
<template>
  <div class="container">
    <div class="slides">
      <div class="slide_1">
        <div class="slide_info">
          <p>Tokyo</p>
        </div>
      </div>
      <div class="slide_1 slide_2">
        <div class="slide_info">
          <p>Okayama</p>
        </div>
      </div>
      <div class="slide_1 slide_3">
        <div class="slide_info">
          <p>Aomori</p>
        </div>
      </div>
      <div class="slide_1 slide_4">
        <div class="slide_info">
          <p>Fukui</p>
        </div>
      </div>
      <div class="slide_1 slide_5">
        <div class="slide_info">
          <p>Shizuoka</p>
        </div>
      </div>
      <div class="slide_1 slide_6">
        <div class="slide_info">
          <p>Osaka</p>
        </div>
      </div>
      <div class="slide_1 slide_7">
        <div class="slide_info">
          <p>Hiroshima</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scope>

section#slides_parent {
    padding-bottom: 150px;
}

.slides {
    display: flex;
    justify-content: center;
    padding: 29px;
}

.slides h4 {
    color: #444;
    font-size: 24px;
    font-weight: 700;
    margin-top: 50px;
}

.slide_1 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://content.r9cdn.net/rimg/dimg/ca/7e/9ae1c4b2-city-21033-16c1b1c620d.jpg?crop=true&width=1020&height=498);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    width: 60px;
    min-width: 60px;
    height: 310px;
    border-radius: 40px;
    margin: 0 15px;
    position: relative;
    transition: all 0.5s ease;
}

.slide_1:hover {
    min-width: 250px;
}

.slide_1:hover .slide_info {
    transform: rotate(0deg);
    left: 20px;
    bottom: 20px;
    font-size: 22px;
}

.slide_2 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://a2.cdn.japantravel.com/photo/232-218308/1200x630!/okayama-okayama-prefecture-218308.jpg);
}

.slide_3 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://xuatkhaulaodong.com.vn/images/2018/12/06/aomori-hirosaki-city-176001-min.jpg);
}

.slide_4 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/7c/82/cf/caption.jpg?w=700&h=500&s=1);
}

.slide_5 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://laodongnhatban.com.vn/images/2018/06/02/tinh-shizuoka-nhat-ban.jpg);
}

.slide_6 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://gaijinpot.scdn3.secure.raxcdn.com/app/uploads/sites/6/2019/10/DOTONBORI-1024x677.jpg);
}

.slide_7 {
    background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(https://xuatkhaulaodong.com.vn/images/2017/03/25/lau-dai-Hiroshima-nhat-ban.jpg);
}

.slide_info {
    position: absolute;
    bottom: 51px;
    color: #ffff;
    transform: rotate(-90deg);
    right: 0px;
    font-weight: 700;
    font-size: 12px;
}

</style>
