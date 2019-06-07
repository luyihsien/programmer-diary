/**
 * Created by luyih on 2019/6/5.
 */
window.onload=function a() {
    var name = document.getElementById('name').textContent = "I am steven";
    var mail = document.getElementById('mail').textContent = "luyihsien@gmail.com"
    var data = {
        name: name.textContent,
        mail: mail.textContent
    }
    var jsonstr=JSON.stringify(data)
    fetch('${window.origin}/test/create-entry', {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(function(response) {
    if (response.status !== 200) {
      console.log('Looks like there was a problem. Status code: ${response.status}');
      return;
    }
    response.json().then(function(data) {
      console.log(data);
    });
  })
  .catch(function(error) {
    console.log("Fetch error: " + error);
})
