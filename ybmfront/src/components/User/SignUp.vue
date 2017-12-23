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
            <button @click = check_username_and_sign_up() type="button" class="btn btn-primary" id="sign_up_button">Create an account</button>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
  import Request from '@/http/Request'
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
        Request.sign_up_request(this.new_user).then(response => {
          if (response.ok) {
            console.debug('get sign up response success')
            response.json().then(json => {
              console.debug('sign up  response result: ' + json.result)
              alert(json.result)
            })
          } else {
            response.json().then(json => {
              console.debug('get sign up response failed : ' + json.detail)
              alert(json.detail)
            })
          }
        }).catch(error => {
          alert(error)
        })
      },
      check_username_and_sign_up () {
        Request.check_username(this.new_user.username).then(response => {
          if (response.ok) {
            console.debug('get check username response success')
            response.json().then(data => {
              let res = data.result
              console.debug('check username response result: ' + res)
              if (res === 'OK') {
                console.debug('start to sign up')
                this.user_sign_up()
              } else {
                console.debug('check username failed : ' + res)
                alert('username already exist')
              }
            })
          } else {
            response.json().then(data => {
              console.debug('get check username response failed : ' + data.detail)
              alert(data.detail)
            })
          }
        }).catch(error => {
          console.debug(error)
          alert(error)
        })
      }
    }
  }
</script>

<style scoped>

</style>

