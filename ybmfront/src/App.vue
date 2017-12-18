<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <router-link to="/User">
      <Button>User</Button>
    </router-link>
    <router-link to="/Test">
      <Button>Test</Button>
    </router-link>
    <router-link to="/">
      <Button>HelloWorld</Button>
    </router-link>
    <router-view></router-view>
    <p class="copyright">Copyright © 2017 ybm. All rights reserved.</p>
  </div>
</template>

<script>
  export default {
    name: 'app'
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
  p.copyright {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    text-align: center;
  }
</style>
