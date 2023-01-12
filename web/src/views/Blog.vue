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
  
    <v-col>
            <v-card 
             v-for ="(Blogs,i) in Blog"
            
            :key="i"
                >
              <div 
              class="d-flex flex-no-wrap justify">
                <v-avatar
                  class="mx-4"
                  size="140px"
                  rounded="0"
                  
               >
               <v-img  :src="Blogs.src"></v-img>
               </v-avatar>
                <div>
                  <v-card-title class="text-h5">
                    {{Blogs.title}}
                  </v-card-title>
  
                  <v-card-subtitle>{{Blogs.subtitle}}</v-card-subtitle>
                  <v-card-actions  >
                    <v-btn
                      rounded="lg"
                      color="red"               
                      variant="outlined"
                      size="small"
                      max-width="30%"
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
  <v-spacer class="blog d-flex justify-space-around">
    <v-btn class="red" rounded>KHÁCH SẠN</v-btn>
    <v-btn class="red" rounded>Phương tiện</v-btn>
    <v-btn class="red" rounded>Ẩm thực</v-btn>
  </v-spacer>
<div>
<h2>{{Title}}</h2>
</div>
  </div>
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

     items:[
        {
          src: 'https://tourdanangcity.vn/wp-content/uploads/2020/11/tour-nhat-ban-tu-da-nang-2-1.jpg',
        },
        {
          src: 'https://cdn3.ivivu.com/2019/06/giao-lo-noi-hang-trieu-nguoi-qua-duong-mot-ngay-o-tokyo-ivivu-2.jpg',
        },
        {
          src: 'https://wallpaperaccess.com/full/16223.jpg',
          
        },
  ],
 Blog:[
    {
      src:'https://wallpaperaccess.com/full/16223.jpg',
    title:"test2",
    subtitle:"bai viet"
  }
  
  ,{
    title:"noi dung",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test"
  }
],
Title:[
{
  title:"Blog cuisine 1",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "cuisine",
    comment_number: 2,
  
},
{
  title:"Blog travel 2",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "travel",
    comment_number: 2,
},
{
  title:"Blog cuisine 2",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "cuisine",
    comment_number: 3,
},

{
  title:"Blog hotel 1",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "hotel",
    comment_number: 7,
},
{
  title:"Blog travel 1",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "travel",
    comment_number: 1,
},
{
  title:"Blog hotel 2",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "hotel",
    comment_number: 7,
},

{
  title:"Blog hotel 3",
    src:'https://wallpaperaccess.com/full/16223.jpg',
    subtitle:"test",
    type: "hotel",
    comment_number: 7,
},],computed:{
   Title(){
       title.filter(item => item.type === "hotel")
      return 
   },
   
}
})};
</script>