<script>
  export default {
    name: 'Request',
    data () {
      return {
        server: 'http://127.0.0.1:8000/api/v1/'
      }
    },
    sign_in_request (body) {
      let request = {
        credentials: 'include',
        method: 'POST',
        header: {
          'Content-Type': 'multipart/form-data'
        },
        body: JSON.stringify(body)
      }
      return fetch(this.data().server + 'user/sign_in/', request)
    },
    sign_up_request (body) {
      let request = {
        credentials: 'include',
        method: 'POST',
        header: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      }
      return fetch(this.data().server + 'user/', request)
    },
    check_username (username) {
      let request = {
        credentials: 'include',
        method: 'POST',
        header: {
          'Content-Type': 'application/json'
        }
      }
      return fetch(this.data().server + 'user/check_username/?username=' + username, request)
    }
  }
</script>

<style scoped>

</style>
