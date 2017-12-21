<!--user register components-->
<template>
    <div class="setup-wrapper">
      <div class="header">
        <p class="header_content">Join ybm blog. Be a cat</p>
      </div>
      <div class="setup-main">
        <div class="setup-form-container">
          <form accept-charset="UTF-8" action="" class="setup-form js-signup-form" id="signup-form">
            <h2 class="f2-light mb-1">
              Create your account
            </h2>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Email</label>
              </dt>
              <dd>
                <input type="text" v-model="new_user.email" name="email"/>
              </dd>
            </dl>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Phone number</label>
              </dt>
              <dd>
                <input type="text" v-model="new_user.phone_number" name="email"/>
              </dd>
            </dl>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Username</label>
              </dt>
              <dd>
                <input type="text" v-model="new_user.username" name="username"/>
              </dd>
            </dl>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Password</label>
              </dt>
              <dd>
                <input type="password" v-model="new_user.password" name="password"/>
              </dd>
            </dl>
            <button @click = user_sign_up() type="button" class="btn btn-primary" id="sign_up_button">Create an account</button>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: 'sign-up',
    data () {
      return {
        new_user: {
          username: '',
          password: '',
          email: '',
          phone_number: ''
        }
      }
    },
    methods: {
      user_sign_up () {
        let request = {
          method: 'POST',
          header: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.new_user)
        }
        fetch('http://127.0.0.1:8000/api/v1/user/', request)
          .then(response => {
            return response.text()
          }, response => {
            console.log(response.text())
          }).then(data => {
            console.log(data)
          })
      }
    }
  }
</script>

<style scoped>

</style>

