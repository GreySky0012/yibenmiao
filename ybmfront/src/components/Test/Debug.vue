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
        let request = {
          credentials: 'include',
          method: 'GET',
          header: {
            'Content-Type': 'application/json'
          }
        }
        fetch('http://127.0.0.1:8000/api/v1/debug/', request)
          .then((response) => {
            if (response.ok) {
              response.json().then(json => {
                this.msg = json.result
              })
            } else {
              response.json().then(json => {
                alert(json.error)
              })
            }
          }).catch(error => {
            alert(error)
          })
      }
    }
  }
</script>

<style>


</style>
