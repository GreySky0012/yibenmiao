var data = '1'

new Vue({
  el :  '#app',
  data : {
    message: '111'
  }
})

fetch("http://127.0.0.1:8000/api/v1/user/user_list",{method:'GET'}).then(function(response){
  data = response.json()
  console.log(data)
})