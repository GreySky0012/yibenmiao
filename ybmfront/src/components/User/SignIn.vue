<template>
  <div>
    <form>
      <input v-model="user.username" type="text" name="username"/>
      <input v-model="user.password" type="password" name="password"/>
      <input type="button" @click="sign_in()"/>
    </form>
    <p>{{msg}}</p>
  </div>
</template>

<script>
  export default {
    name: 'sign-in',
    data () {
      return {
        msg: 'Welcome to Blog',
        user: {
          username: '',
          password: ''
        }
      }
    },
    methods: {
      sign_in () {
        this.$http.post('http://127.0.0.1:8000/api/v1/user/sign_in/', JSON.stringify(this.user)).then((response) => {
          this.msg.set(response.toString())
        }, (response) => {
          this.msg.set('request error')
        })
      }
    }
  }
</script>

<style scoped>

</style>
