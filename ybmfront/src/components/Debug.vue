<template>
  <div id="Debug">
    <!--<img src="./assets/logo.png">-->
    <router-view>s</router-view>
    <p id="message" >{{msg}}</p>
    <button @click=myOnClick()>{{button}}</button>
  </div>
</template>

<script>
  export default {
    name: 'Debug',
    data () {
      return {
        button: 'This is a button',
        msg: 'Show the message'
      }
    },
    methods: {
      myOnClick () {
        alert('enter thr function')
        this.$http.get('http://127.0.0.1:8000/api/v1/debug/').then((response) => {
          document.getElementById('message').innerHTML = response.data
        })
      }
    }
  }
</script>

<style>


</style>
