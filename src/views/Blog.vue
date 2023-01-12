<template>
  <div>
   <v-card class="banner" >
    <v-row>
      <v-col class="style1" >
    
     <v-carousel
      cycle
      hide-delimiter-background
      :show-arrows="'hover'"
      cover
     >

     <v-carousel-item
        cycle
        v-for="(items,i) in items" 
        :key="i"
        :src="items.src"
       cover
      >
      </v-carousel-item>
    </v-carousel>
    
   </v-col> 
  
    <v-col >
            <v-card           >
              <div class="d-flex flex-no-wrap justify">
                <v-avatar
                  class="mx-4"
                  size="140"
                  rounded="0">
    <!-- <v-img 
    
  ></v-img> -->
  </v-avatar>
                <div>
                  <v-card-title class="text-h5">
                    Supermodel
                  </v-card-title>
  
                  <v-card-subtitle> Foster the People</v-card-subtitle>
                  <v-card-actions  >
                    <v-btn
                      rounded="lg"
                      color="red"               
                      variant="outlined"
                      size="small"
                    >
                      Xem them
                    </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
    </v-col>       
  </v-row>
</v-card>
  </div>
  <v-spacer class="blog d-flex justify-space-around">
    <v-btn class="red" rounded>KHÁCH SẠN</v-btn>
    <v-btn class="red" rounded>Phương tiện</v-btn>
    <v-btn class="red" rounded>Ẩm thực</v-btn>
  </v-spacer>
  <v-spacer  class="blog d-flex justify-space-around">
<v-card >
 <v-col cols="12" >
  
   <div class="d-flex flex-no-wrap justify-space-between">
        <v-avatar
                  class="ma-3"
                  size="125"
                  rounded="0"
                >
                  <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                </v-avatar>
     
     <div >
        <v-card-title class="text-h5">Supermodel</v-card-title>
            <v-card-subtitle>Foster the People</v-card-subtitle>
              <v-card-actions>
                    <v-btn
                      class="ml-2"
                      variant="outlined"
                      size="small"
                    >
                      START RADIO
                    </v-btn>
                  </v-card-actions>
                </div>
           
              </div>
          </v-col>
    
    </v-card>

</v-spacer>

   </template>

<style scoped>
.blog {
  margin-top: 21px;
}
.red {
  background-color: rgb(255, 102, 0);
}

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
.style1{
  border: 2px;
  border-radius: 25px;
  padding: 0 !important;
  overflow: hidden;
  height: 400px;

}
.banner{
  padding: 20px;
  background-color: rgb(32, 31, 31);
  height: auto;
  width: auto;
}
.test{
  width: 250px;
  height: 150px;
}

</style>
<script>
export default {
  data: () => ({
     items: [
        {
          src: 'https://tourdanangcity.vn/wp-content/uploads/2020/11/tour-nhat-ban-tu-da-nang-2-1.jpg',
        },
        {
          src: 'https://cdn3.ivivu.com/2019/06/giao-lo-noi-hang-trieu-nguoi-qua-duong-mot-ngay-o-tokyo-ivivu-2.jpg',
        },
        {
          src: 'https://wallpaperaccess.com/full/16223.jpg',
          
        },
      
        
  ]

  }),
};
</script>
