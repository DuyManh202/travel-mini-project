<template>
   <div class="login d-flex align-center fill-height">
        <v-row cols="12" md="3">
        <v-card width="500" class="mx-auto mt-13">
          <v-card-title>Đăng Ký</v-card-title>
          <v-card-text>
            <v-text-field label="Nickname" prepend-icon="mdi-account-circle"/>
            <v-text-field 
            label="Password" 
            :type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"/>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions class="d-flex justify-end">
          
            
       <v-btn color="white" style="background-color:deepskyblue">Đăng Ký</v-btn>
            <v-btn color="white" style="background-color:red">Đăng Nhập</v-btn>
          
          </v-card-actions>
        </v-card>
        </v-row>
    </div>

</template>
<script>
export default {

  name: "Login",
  
    data()

  {
    return{
      showPassword:false
    }
  },
  mounted() {
    
  },
}
</script>
<style scoped>
  .login{
    background-image: url(https://afar.brightspotcdn.com/dims4/default/a69e584/2147483647/strip/true/crop/1357x720+41+0/resize/1440x764!/quality/90/?url=https%3A%2F%2Fafar-media-production-web.s3.amazonaws.com%2Fbrightspot%2Fcf%2F8a%2F20b4a2c544a58be93512ad67084c%2Fbohler-japankk-4006.jpg);
  
  background-size: cover;
  };
  ::v-show .btn-login{
    margin-right: 0 !important;
    margin-left: auto !important;
}
  
</style>