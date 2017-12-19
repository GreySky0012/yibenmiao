<template>
  <div>
    <title>User Page</title>
    <router-link to="/user/sign_in">
      <Button>SignIn</Button>
    </router-link>
    <router-link to="/user/sign_up">
      <Button>SignUp</Button>
    </router-link>
    <router-link to="/user">
      <Button>index</Button>
    </router-link>
    <h1>{{msg}}</h1>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'User',
    data () {
      return {
        msg: 'User Pages'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
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
