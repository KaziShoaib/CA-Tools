document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#create-user-button').addEventListener('click', showLoadButton)
})

const showLoadButton = () => {
  const ca = document.querySelector('#ca-name').value
  const username = document.querySelector('#username').value
  const email = document.querySelector('#email').value
  if(ca!=='' && username!=='' && email !== '')
    document.querySelector('#loading-button').style.display = 'block'
}