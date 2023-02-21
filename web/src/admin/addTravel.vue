<template>
<v-app>
  <div class="Content">
    <div class="box-menu"><commentMagement></commentMagement></div>
    <div class="title-content" style="color: #eee">
      <i style="margin-right: 5px" class="fas fa-plus-square"></i>
      Thêm travel viết mới
    </div>
    <v-content>
      <v-row>
        <div class="col-9">
          <h2 class="copyright">Thêm travel</h2>
          <QuillEditor theme="snow" />
        </div>
        <div class="col-7">
          
            <tbody>
              <tr>
                <td>
                  <i class="fas fa-plus-square"></i>
                  <span style="font-weight: 600">Các thành phần</span>
                </td> 
              </tr>
              <tr>
                <td style="background: #f2f2f2">
                  <table style="border: none; width: 100%">
                    <tbody>
                      <tr style="border: none; width: 100%">
                        <td style="border: none; width: 50%; padding: 15px">
                          <label style="color: #000; font-weight: 500" for=""
                            >Tiêu đề bài viết</label
                          >
                          <input
                            type="text"
                            style="width: 70%"
                            class="form-control"
                            id="password"
                            required=""
                            placeholder="enter post title"
                            name="title"
                          />
                          <br />
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Ảnh Carousel 1</label
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
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Ảnh Carousel 2</label
                            ><br />
                            <img
                              id="blah2"
                              src=""
                              alt="Ảnh đại diện"
                              style="height: 140px; width: 200px"
                            /><br /><br />
                            <input
                              type="file"
                              style="font-size: 12px"
                              name="imgInp2"
                              id="imgInp2"
                            />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Ảnh Carousel 3</label
                            ><br />
                            <img
                              id="blah3"
                              src=""
                              alt="Ảnh đại diện"
                              style="height: 140px; width: 200px"
                            /><br /><br />
                            <input
                              type="file"
                              style="font-size: 12px"
                              name="imgInp3"
                              id="imgInp3"
                            />
                          </div>
                        </td>
                        <td style="border: none; width: 50%; padding: 15px">
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Mã du lịch</label
                            ><br />
                            <input
                              type="text"
                              placeholder="DTFHFDS-76HG"
                              name="code"
                            />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Ngày khởi hành</label
                            ><br />
                            <input type="date" name="Dday" />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Thời gian</label
                            ><br />

                            <input
                              type="time"
                              id="appt"
                              name="appt"
                              min="09:00"
                              max="18:00"
                              required
                            />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Địa điểm xuất phát</label
                            ><br />
                            <input
                              type="text"
                              placeholder="Ha noi"
                              name="startingplace"
                            />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Địa điểm đến</label
                            ><br />
                            <input
                              type="text"
                              placeholder=""
                              name="ToLocation"
                            />
                          </div>
                          <div class="form-group">
                            <label style="color: #000; font-weight: 500" for=""
                              >Số lượng hành khách tối đa</label
                            ><br />
                            <input
                              type="number"
                              value="15"
                              name="Numberofseats"
                            />
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <br /><br />
                  <div style="width: 100%; text-align: center">
                    <button class="btn btn-danger">Tải lên địa điểm</button>
                  </div>
                  <br />
                </td>
              </tr></tbody
          > 
        </div>
      </v-row>
    </v-content>
  </div>
</v-app>
</template>
<script>
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import commentMagement from '../admin/commentMagement.vue'
export default {
   components: {
     QuillEditor,
     commentMagement
     }
    };
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
  max-width: 64%;
  padding: 20px;
}
.col-7 {
  -ms-flex: 0 0 25%;
  flex: 0 0 25%;
  max-width: 33%;
margin-top: 20px;
margin-left: -20px;

}
.copyright {
  background-color: #070e0f;
  color: #fff;
  margin-left: -20px;
  margin-top: -10px;
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
.form-group {
  margin-bottom: 1rem;
}
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
