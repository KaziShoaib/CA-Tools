document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#change-password-form').onsubmit = handlePasswordChange
})


const getCookie = (c_name) => {
  if (document.cookie.length > 0)
  {
    c_start = document.cookie.indexOf(c_name + "=");
      if (c_start != -1)
      {
        c_start = c_start + c_name.length + 1;
        c_end = document.cookie.indexOf(";", c_start);
        if (c_end == -1) c_end = document.cookie.length;
          return unescape(document.cookie.substring(c_start,c_end));
      }
    }
  return "";
}


const clearFields = () => {
  document.querySelector('#current-password').value = ""
  document.querySelector('#new-password').value = ""
  document.querySelector('#retype-new-password').value = ""
}


function launch_modal(text_color, message_heading, message_content){
  document.querySelector('#message-heading').className =  text_color;
  document.querySelector('#message-heading').innerHTML = message_heading;
  document.querySelector('#message-body').className = text_color;
  document.querySelector('#message-body').innerHTML = message_content;
  $('#message-modal').modal();
}


const handlePasswordChange = (e) => {
  e.preventDefault()
  const oldPassword = document.querySelector('#current-password').value
  const newPassword = document.querySelector('#new-password').value
  const retypedNewPassword = document.querySelector('#retype-new-password').value
      
    fetch('/ChangePassword', {
      method: 'POST',
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      body: JSON.stringify({
        oldPassword: oldPassword,
        newPassword: newPassword,
        retypedNewPassword: retypedNewPassword
      })
    })
    .then(response => response.json())
    .then(result => {      
      if(result.message === 'success'){
        clearFields()
        launch_modal('text-success', 'SUCCESS', 'password reset successful')
      }        
      else
        launch_modal('text-danger', 'EROOR', 'incorrect old password')
    })
  
}