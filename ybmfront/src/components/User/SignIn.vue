<template>
  <div>
    <input v-model="user.username" type="text" name="username"/>
    <input v-model="user.password" type="password" name="password"/>
    <button @click="sign_in()">sign in</button>
    <p>{{msg}}</p>
  </div>
</template>

<script>
  import Request from '@/http/Request'
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
        Request.sign_in_request(this.user).then(response => {
          if (response.ok) {
            response.json().then(data => {
              this.msg = data.username
            })
          } else {
            response.json().then(data => {
              this.msg = data.detail
            })
          }
        }).catch(error => {
          this.msg = error
        })
      }
    }
  }
</script>

<style scoped>

</style>
