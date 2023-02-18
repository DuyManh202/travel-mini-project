<template>
<div class="Content">
  <div class="box-menu"><commentMagement></commentMagement></div>
    <div class="title-content" style="color: #eee">
      <i style="margin-right: 5px" class="fas fa-plus-square"></i>
      Thêm blogs mới
    </div>
    <v-content>
      <v-row>
        <div class="col-9">
          <h2 class="copyright">Thêm Blogs</h2>
          <QuillEditor theme="snow" />
        </div>
        <div class="col-3">
          <v-table>
            <tbody>
              <tr>
                <td>
                  <i class="fas fa-plus-square"></i>
                  <span style="font-weight: 600">Các thành phần</span>
                </td>
              </tr>
              <tr>
                <td style="background: #f2f2f2; padding: 5px">
                  <label style="color: #000; font-weight: 500" for=""
                    >Tiêu đề bài viết</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    id="password"
                    required=""
                    placeholder="enter post title"
                    name="title"
                  />
                  <br />
                  <div class="form-group">
                    <label style="color: #000; font-weight: 500" for=""
                      >Ảnh đại diện cho bài viết</label
                    ><br />
                    <img
                      id="blah"
                      src=""
                      alt="Ảnh đại diện"
                      style="height: 140px; width: 200px"
                    /><br /><br />
                    <input
                      type="file"
                      style="font-size: 12px"
                      name="imgInp"
                      id="imgInp"
                    />
                  </div>

                  <br /><v-select
                    label="Select"
                     variant="solo"
                    :items="[
                      ' Khách sạn ',
                      ' Phương tiện ',
                      ' Ẩm thực ',
                    ]"
                  ></v-select
                  ><br />
                  <div style="width: 100%; text-align: center">
                    <button class="btn btn-danger">Tải lên bài viết</button>
                  </div>
                  <br />
                </td>
              </tr>
            </tbody>
          </v-table>
        </div>
      </v-row>
    </v-content>
</div>
</template>

<script>
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import commentMagement from '../admin/commentMagement.vue'

export default {
   components: { 
    QuillEditor,
    commentMagement

} };
</script>

<style scoped>
.td {
  border: solid 1px #123;
}
.label {
  display: inline-block;
  margin-bottom: 0.5rem;
}
.form-control {
  display: block;
  width: 100%;
  height: calc(1.5em + 0.75rem + 2px);
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
.col-9 {
  -ms-flex: 0 0 75%;
  flex: 0 0 75%;
  max-width: 72%;
  padding: 11px;
  margin-left: -11px;
}
.col-3 {
  -ms-flex: 0 0 25%;
  flex: 0 0 25%;
  max-width: 25%;
  padding: 20px;
}
.copyright {
  background-color: #070e0f;
  color: #fff;
margin-left: -0px;
  margin-top: -0px;
}
.title-content {
  line-height: 30px;
  padding-left: 5px;
  background: #0056b3;
  width: 100%;
  min-width: 1070px;
  height: 30px;
}
.tr {
  display: table-row;
  vertical-align: inherit;
  border-color: inherit;
}
.tbody {
  display: table-row-group;
  vertical-align: middle;
  border-color: inherit;
}
.box-menu{
  float: left;
  background: #234;
  width: 15%;
  min-height: 230px;
  height: 100%;
}
.Container {
  width: 100%;
  min-width: 1300px;
  min-height: 100%;
  height: 100%;
}

</style>>
