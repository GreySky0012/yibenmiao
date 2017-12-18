<!--user register components-->
<template>
    <div class="setup-wrapper">
      <div class="header">
        <p class="header_content">Join ybm blog</p>
      </div>
      <div class="setup-main">
        <div class="setup-form-container">
          <form accept-charset="UTF-8" class="setup-form js-signup-form" id="signup-form" method="post">
            <h2 class="f2-light mb-1">
              Create your account
            </h2>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Email</label>
              </dt>
              <dd>
                <input type="text" name="email"/>
              </dd>
            </dl>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Username</label>
              </dt>
              <dd>
                <input type="text" name="username"/>
              </dd>
            </dl>
            <dl class="form-group" >
              <dt class="input-label">
                <label >Password</label>
              </dt>
              <dd>
                <input type="password" name="password"/>
              </dd>
            </dl>
            <button type="submit" class="btn btn-primary" id="sign_up_button">Create an account</button>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: 'sign-up'
  }
</script>

<style scoped>

</style>

