<template>
<div class="Content">
  <div class="box-menu"><commentMagement></commentMagement></div>
    <div class="title-content" style="color: #eee">
      <i style="margin-right: 5px" class="fas fa-plus-square"></i>
      Thêm blogs mới
    </div>
    <v-content>
 <table style="width: 100%; margin: 5px;">
    <tbody><tr style="font-weight: 600; color: #000; font-size: 18px;">
        <td colspan="8" style="text-align: left">
            <i class="fas fa-bars" style="margin-right: 3px;"></i>
            Danh sách Comment</td>
    </tr>
    <tr style="background: #fff; text-align: center">
        <td style="color: #cc0000; font-weight: 500">STT</td>
        <td style="color: #115095; font-weight: 500">Id</td>
        <td style="color: #115095; font-weight: 500">Người dùng</td>
        <td style="color: #115095; font-weight: 500">Id Bài viết</td>
        <td style="color: #115095; font-weight: 500">Nội dung Cmt</td>
        <td style="color: #115095; font-weight: 500">Hành động</td>
    </tr>
        
 
</tbody></table>
    </v-content>
</div>
</template>

<script>

import commentMagement from '../admin/commentMagement.vue'

export default {
   components: { 
  commentMagement

} };
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
  width: 15%;
  min-height: 230px;
  height: 100%;
}

</style>