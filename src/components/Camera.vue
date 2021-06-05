<template>
  <div id="app">

    <!-- <img src="../../temporary_images/img_1.png" :width="width" :height="height" /> -->
    <img v-cloak :src="image" :width="width" :height="height" />
    <br>
    <a class="btn btn-primary" href="#" role="button" v-on:click="show">Implement</a>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
<script src="../main.js"></script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

export default {
  name: 'Camera',
  props: {
    msg: String
  },
  data: function() {
    return {
      // image: "../../temporary_images/img_1.png",
      image: "",
      width: 1280 / 2,
      height: 960 / 2,
      d: {
        key: "string"
      }
    };
  },
  methods: {
    // sleep: (msec) => await new Promise(resolve => setTimeout(resolve, msec)),
    show: async function() {
      const url = 'http://127.0.0.1:8000/pet_camera'
      const data = JSON.stringify(this.d)

      Vue.prototype.$axios = axios

      while(1){
        await axios.post(url, data)
          .then(async response => {
            // console.log(response.data["Image"])
            // console.log(__filename);
            // console.log(__dirname);
            await Vue.set(this, "image", response.data["Image"])
            await console.log(this.image)
           })
           .then(async () => {
             // await console.log("スリープに入るよ")
             await new Promise(resolve => setTimeout(resolve, 100))
             // await console.log("出たよ")
           })
          .catch(error => console.log(error.response));
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
[v-cloak] {
  display: none;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
