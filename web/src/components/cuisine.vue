<template>
  <div class="blog d-flex justify-space-around">
    <v-row>
      <v-col
        ><div class="text-center">
          <v-btn :to='{name:"blogs1"}' class="red" rounded>KHÁCH SẠN</v-btn>
        </div>

        <v-card v-for="(hotel, i) in hotels" :key="i">
          <div class="d-flex flex-no-wrap justify">
            <v-avatar class="mx-4" size="140px" rounded="0">
              <v-img :src="hotel.src"></v-img>
            </v-avatar>
            <div>
              <v-card-title class="text-h5">
                {{ hotel.title }}
              </v-card-title>
              <v-card-subtitle>{{ hotel.subtitle }}</v-card-subtitle>
              <v-card-actions>
                <v-btn
                  rounded="lg"
                  color="red"
                  variant="outlined"
                  size="small"
                  max-width="60%"
                >
                  Xem them
                </v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
      <v-col>
        <div class="text-center">
          <v-btn :to='{name:"blogs2"}' class="red" rounded>Phương tiện</v-btn>
        </div>

        <v-card v-for="(travel, i) in travels" :key="i">
          <div class="d-flex flex-no-wrap justify">
            <v-avatar class="mx-4" size="140px" rounded="0">
              <v-img :src="travel.src"></v-img>
            </v-avatar>
            <div>
              <v-card-title class="text-h5">
                {{ travel.title }}
              </v-card-title>
              <v-card-subtitle>{{ travel.subtitle }}</v-card-subtitle>
              <v-card-actions>
                <v-btn
                  rounded="lg"
                  color="red"
                  variant="outlined"
                  size="small"
                  max-width="60%"
                >
                  Xem them
                </v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
      <v-col>
        <div class="text-center">
          <v-btn :to='{name:"blogs3"}' class="red" rounded>Ẩm thực</v-btn>
        </div>
        <v-card v-for="(cuisine, i) in cuisines" :key="i">
          <div class="d-flex flex-no-wrap justify">
            <v-avatar class="mx-4" size="140px" rounded="0">
              <v-img :src="cuisine.src"></v-img>
            </v-avatar>
            <div>
              <v-card-title class="text-h5">
                {{ cuisine.title }}
              </v-card-title>
              <v-card-subtitle>{{ cuisine.subtitle }}</v-card-subtitle>
              <v-card-actions>
                <v-btn
                  rounded="lg"
                  color="red"
                  variant="outlined"
                  size="small"
                  max-width="60%"
                >
                  Xem them
                </v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: "cuisine",
  props: {
    hotels: Array,
    travels: Array,
    cuisines: Array,
  },
};
</script>

<style scoped>
.blog {
  padding: 12px;
  margin-top: 21px;
}
.red {
  background-color: rgb(255, 102, 0);
  text-align: center;
}
</style>
