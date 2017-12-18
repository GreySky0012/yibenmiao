<template>
  <div id="app">
    <button @click=myOnClick()>{{button}}</button>
  </div>
</template>

<script>
  export default {
    name: 'Debug',
    data () {
      return {
        button: 'This is a button'
      }
    },
    methods: {
      myOnClick () {
        alert('This button is onclick!!!')
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
