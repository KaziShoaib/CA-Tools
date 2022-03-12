document.addEventListener('DOMContentLoaded', ()=> {
  document.querySelector('#add-service-button').addEventListener('click', addMoreService)
  document.querySelector('#remove-service-button').addEventListener('click', removeLastService)
})

const createInputField = (fieldType, fieldName, className, placeHolder) => {
  let inputField = document.createElement('input')
  inputField.setAttribute('type', fieldType)
  inputField.setAttribute('name', fieldName)
  inputField.className = className
  inputField.setAttribute('placeholder', placeHolder)
  return inputField
}

const addMoreService = () => {
  const integrationInformationFieldSet = document.querySelector('#integration-information')
  const serviceRow = document.createElement('div')
  serviceRow.className = 'form-group row service-row'
  const inputFieldAttributes = [
    {fieldType: 'text', fieldName:'digital-service-name', placeHolder:'Digital Service Name'},
    {fieldType: 'text', fieldName:'digital-service-organization-name', placeHolder:'Organization Name'},
    {fieldType: 'number', fieldName:'digital-service-electronic-signature-number', placeHolder:'Number of Electronic Signatures'}
  ]
  for(let i=0; i<inputFieldAttributes.length; i++){
    const serviceColumn = document.createElement('div')
    serviceColumn.className = 'col'
    const inputField = createInputField(inputFieldAttributes[i].fieldType, inputFieldAttributes[i].fieldName, 'form-control', inputFieldAttributes[i].placeHolder)
    serviceColumn.appendChild(inputField)
    serviceRow.appendChild(serviceColumn)
  }
  integrationInformationFieldSet.appendChild(serviceRow)
  document.querySelector('#remove-service-button').style.display = 'grid'
}

const removeLastService = () => {
  let serviceRows = document.getElementsByClassName('service-row')
  serviceRows[serviceRows.length-1].remove()
  if(serviceRows.length === 1)
    document.querySelector('#remove-service-button').style.display = 'none'
}