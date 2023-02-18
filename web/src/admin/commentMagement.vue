<template>
  <v-app>
    <div class="Container">
      
      <div class="box-menu">
        <div class="administrator-logo">
          <img
            style="width: 27px; float: left; height: 100%"
            src="https://png.pngtree.com/png-vector/20191122/ourmid/pngtree-beautiful-admin-roles-glyph-vector-icon-png-image_2002847.jpg"
          />
          <a href="./"
            ><p style="color: #ff7610; float: left">Administrators</p></a
          >
        </div>

        <form method="get" >
          <router-link class="btnkgvien" to="addBlogs" >
            <div class="line-menu" style="color: #fff">
              <i class="fas fa-plus-square"></i>
              Thêm BLOG
            </div>
          </router-link>
        </form>

        <form method="get" >
          <router-link class="btnkgvien" to="addTravel">
            <div class="line-menu" style="color: #fff">
              <i class="fab fa-pied-piper-square"></i>
              Thêm Travel
            </div>
          </router-link>
        </form>

        <form method="get" action="#">
          <input name="select" value="postmanagement" style="display: none" />
          <button class="btnkgvien">
            <div class="line-menu" style="color: #fff">
              <i class="fas fa-tasks"></i>
              Quản lý BLOG
            </div>
          </button>
        </form>

        <form method="get" action="#">
        
          <button class="btnkgvien">
            <div class="line-menu" style="color: #fff">
              <i class="fas fa-location-arrow"></i>
              Quản lý TRAVEL
            </div>
          </button>
        </form>
        <form method="get" action="#">
          <input
            name="select"
            style="display: none"
          />
          <button class="btnkgvien">
            <div class="line-menu" style="color: #fff">
              <i class="fas fa-comment-medical"></i>
              Quản lý Comment
            </div>
          </button>
        </form>

        <form method="post" action="#">
          <input name="act" value="true" style="display: none" />
          <button class="btnkgvien">
            <div class="line-menu" style="color: #ee1111">
              <i class="fas fa-sign-out-alt"></i>
              Đăng xuất
            </div>
          </button>
        </form>
      </div>

    </div>
  </v-app>
</template>
<script>
export default {
  components:{

  }
};
</script>

<style scoped>
.Container {
  width: 100%;
  min-width: 1300px;
  min-height: 100%;
  height: 100%;
}
.box-menu {
  float: left;
  background: #234;
  width: 19%;
  min-height: 230px;
  height: 100%;
}
.screen-menu {
  line-height: 30px;
  background: #234;
  width: 100%;
  min-width: 1070px;
  height: 30px;
}
td {
  border: solid 1px #123;
}
.main-screen {
  background: #eee;
  float: left;
  width: 85%;
  min-width: 1070px;
  min-height: 100%;
}
.title-content {
  line-height: 30px;
  padding-left: 5px;
  background: #0056b3;
  width: 100%;
  min-width: 1070px;
  height: 30px;
}
.content {
  padding: 5px;
  width: 100%;
  min-width: 1070px;
  height: 100%;
}
.administrator-logo {
  margin-top: 15px;
  height: 30px;
  margin-left: 10px;
}
.btnkgvien {
  text-align: left;
  width: 100%;
  border: 0px;
  padding: 0px;
  margin: 0px;
  background: #234;
}
.btnkgvien:hover {
  background: #ff6600;
}

.line-menu {
  padding-left: 7px;
  padding-right: 5px;
  line-height: 35px;
  height: 35px;
  color: #eee;
  font-size: 15px;
  border-bottom: solid 2px #345;
}
.line-menu:hover {
  background: #0062cc;
}
.box-login {
  position: absolute;
  top: 30%;
  left: 40%;
  background: #fff;
  width: 350px;
  height: 300px;
  padding: 25px;
  border: 1px solid #666;
}
</style>
