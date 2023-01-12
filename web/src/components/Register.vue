<template class="login">
  <div class="box">
<v-car>
    <v-content class="container">
            <header>
                 
              
            </header>
        <div class="input-field">
            <input type="text" class="input" placeholder="Username" id="">
            <i class='bx bx-user' ></i>
        </div>
        <div class="input-field">
            <input type="Password" class="input" placeholder="Password" id="">
            <i class='bx bx-lock-alt'></i>
        </div>
        <div class="two-col">
            <div class="one">

               <input type="checkbox" name="" id="check">
               <label for="check"> Remember Me</label>
            </div>
            <div class="two">
                <label><a href="#">Forgot password?</a></label>
            </div>
        </div>

        <div class="input-field">
          
            <v-spacer>
                <v-btn
            rounded=""
            class="ma-2 pa-2">
             Đăng ký 

            </v-btn>
        
             <v-btn
             :to='{name: "register"}'
            rounded=""
            > Đăng nhập
            </v-btn>
        
            </v-spacer>
            
           </div>
        
        
    </v-content>
  </v-car>
</div>  

</template>

<script>
export default {setup() {
    const goTo = (to) => {
      console.log(to)
    }
    return {goTo}
 
}

}
</script>

<style scoped>
.box{
  background-image: url("https://wallpaperaccess.com/full/2346347.jpg");
background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 92vh;
}
.container{
    width: 350px;
    display: flex;
    flex-direction: column;
    padding: 0 15px 0 15px;
    background-color: rgba(0, 0, 0, 0.136);
    
}
span{
    color: #fff;
    font-size: small;
    display: flex;
    justify-content: center;
    padding: 10px 0 10px 0;
}
header{
    color: #fff;
    font-size: 30px;
    display: flex;
    justify-content: center;
    padding: 10px 0 10px 0;
}
.input-field .input{
    height: 45px;
    width: 99%;
    border: none;
    border-radius: 30px;
    color: #fff;
    font-size: 15px;
    padding: 0 0 0 45px;
    background: rgba(255,255,255,0.1);
    outline: none;
    margin: 2px;
}
i{
    position: relative;
    top: -33px;
    left: 17px;
    color: rgb(207, 10, 10);
}
::-webkit-input-placeholder{
    color: #fff;
}
.submit{
    border: none;
    border-radius: 30px;
    font-size: 15px;
    height: 45px;
    outline: none;
    width:40%;
    color: black;
    background: rgba(255,255,255,0.7);
    cursor: pointer;
    transition: .3s ;
}
.submit:hover{
    box-shadow: 1px 5px 7px 1px rgba(0, 0, 0, 0.2);
}
.two-col{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    color: #fff;
    font-size: small;
    margin-top: 10px;
}
.one{
    display: flex;
}
label a{
    text-decoration: none;
    color: #fff;
}

</style>