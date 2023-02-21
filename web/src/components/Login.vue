<template class="login">
  <div class="box">
    <v-car>
      <v-content class="container">
        <header>
          <h4>Đăng nhập</h4>
        </header>
        <div class="input-field">
          <v-card-text>
            <v-text-field
              label="Email"
              prepend-icon="mdi-account-circle"
              v-model="logins.email"
              required
            />
            <v-text-field
              label="Password"
              v-model="logins.password"
              type="password"
              prepend-icon="mdi-lock"
            />
          </v-card-text>
        </div>
        <div class="two-col">
            <v-alert class="alert"
                   v-if="showAlert"
                   type="error"
          >
            Invalid Email or Password!
          </v-alert>
          <v-card-actions>
            <v-btn type="submit" @click="login()" color="info">Login</v-btn>
          </v-card-actions>
        </div>
      </v-content>
    </v-car>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      logins: {
        email: "",
        password: "",
      },
      showAlert: false,
      error: "",
    };
  },
  methods: {
    login() {
      try {
        axios.post("/login", this.logins).then((response) => {
          console.log(response);
          if (response.data.code === 200) {
            localStorage.name = response.data.data[0].username;
            localStorage.email = response.data.data[0].email;
            localStorage.phone_number = response.data.data[0].phone;
            localStorage.id = response.data.data[0].id;
            localStorage.password = response.data.data[0].password;
            localStorage.address = response.data.data[0].address;
            this.$router.push("/");
          } else {
            this.showAlert = true;
            this.error = "Invalid email/password!";
          }
        });
      } catch (e) {
        this.error = "Invalid email/password!";
      }
    },
  },
};
</script>

<style scoped>
.box {
  background-image: url("https://wallpaperaccess.com/full/2346347.jpg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;

  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.container {
  width: 423px;
  display: flex;
  flex-direction: column;
  padding: 0 15px 0 15px;
  background-color: rgba(0, 0, 0, 0.136);
}
span {
  color: #fff;
  font-size: small;
  display: flex;
  justify-content: center;
  padding: 10px 0 10px 0;
}
header {
  color: #fff;
  font-size: 30px;
  display: flex;
  justify-content: center;
  padding: 10px 0 10px 0;
}
.input-field .input {
  height: 45px;
  width: 99%;
  border: none;
  border-radius: 30px;
  color: #e0e0e0;
  font-size: 15px;
  padding: 0 0 0 45px;
  background: rgba(255, 255, 255, 0.1);
  outline: none;
  margin: 2px;
}
i {
  position: relative;
  top: -33px;
  left: 17px;
  color: rgb(207, 10, 10);
}
::-webkit-input-placeholder {
  color: #fff;
}
.submit {
  border: none;
  border-radius: 30px;
  font-size: 15px;
  height: 45px;
  outline: none;
  width: 40%;
  color: black;
  background: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  transition: 0.3s;
}
.submit:hover {
  box-shadow: 1px 5px 7px 1px rgba(0, 0, 0, 0.2);
}
.two-col {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  color: #fff;
  font-size: small;
  margin-top: 10px;
}
.one {
  display: flex;
}
label a {
  text-decoration: none;
  color: #fff;
}
</style>
