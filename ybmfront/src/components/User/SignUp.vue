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
            <button @click = check_username() type="button" class="btn btn-primary" id="sign_up_button">Create an account</button>
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
            console.debug('get sign up response success')
            return response.json()
          }, response => {
            let respData = response.json()
            console.debug('get sign up response failed : ' + respData.error)
            alert(respData.error)
          }).then(data => {
            console.debug('sign up  response result: ' + data.result)
            alert('sign up success')
          })
      },
      check_username_and_sign_up () {
        console.debug('enter function')
        let request = {
          method: 'POST',
          header: {
            'Content-Type': 'application/json'
          }
        }
        fetch('http://127.0.0.1:8000/api/v1/user/check_username/?username=' + this.new_user.username, request)
          .then(response => {
            console.debug('get check username response success')
            return response.json()
          }, response => {
            let respData = response.json()
            console.debug('get check username response failed : ' + respData.error)
            alert(respData.error)
          }).then(data => {
            let res = data.result
            console.debug('check username response result: ' + res)
            if (res === 'OK') {
              console.debug('start to sign in')
              this.user_sign_up()
            } else {
              console.debug('check username failed : ' + res)
              alert('username already exist')
            }
          })
      }
    }
  }
</script>

<style scoped>

</style>

