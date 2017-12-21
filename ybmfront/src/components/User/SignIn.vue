<template>
  <div>
    <input v-model="user.username" type="text" name="username"/>
    <input v-model="user.password" type="password" name="password"/>
    <button @click="sign_in()">sign in</button>
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
        let request = {
          method: 'POST',
          header: {
            'Content-Type': 'multipart/form-data'
          },
          body: JSON.stringify(this.user)
        }
        fetch('http://127.0.0.1:8000/api/v1/user/sign_in/', request)
          .then(response => {
            if (response.ok) {
              response.json().then(data => {
                this.msg = data.username
              })
            } else {
              response.json().then(data => {
                this.msg = data.error
              })
            }
          }).catch(error => {
            this.msg = error
          }
        )
      }
    }
  }
</script>

<style scoped>

</style>
