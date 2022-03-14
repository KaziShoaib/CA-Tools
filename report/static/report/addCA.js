document.addEventListener('DOMContentLoaded', ()=> {
  document.querySelector('#add-personnel-button').addEventListener('click', addPersonnel)
  document.querySelector('#remove-personnel-button').addEventListener('click', removePersonnel)
})

const createInputField = (fieldType, fieldName, className, placeHolder) => {
  let inputField = document.createElement('input')
  inputField.setAttribute('type', fieldType)
  inputField.setAttribute('name', fieldName)
  inputField.className = className
  inputField.setAttribute('placeholder', placeHolder)
  return inputField
}


const createServiceRow = () => {
  const serviceRow = document.createElement('div')
  serviceRow.className = 'form-group row service-row'
  return serviceRow
}


const addPersonnel = () => {
  const CAOPerationsPersonnelInformationGroup = document.querySelector('#CA-operations-personnel-information')
  
  const inputFieldAttributes = [
    [
      {fieldType: 'text', fieldName:'operations-personnel-name', placeHolder:'Name'},
      {fieldType: 'text', fieldName:'operations-personnel-designation', placeHolder:'Designation'}
    ],
    [
      {fieldType: 'text', fieldName:'operations-personnel-phone', placeHolder:'Phone'},
      {fieldType: 'text', fieldName:'operations-personnel-email', placeHolder:'Email'}
    ]
  ]

  const personnelCount = document.getElementsByClassName('personnel-label').length
  const personnelLabel = document.createElement('label')
  personnelLabel.className = 'personnel-label'
  personnelLabel.innerHTML = `Personnel ${personnelCount + 1}`
  CAOPerationsPersonnelInformationGroup.appendChild(personnelLabel)
  
  for(let i=0; i<inputFieldAttributes.length; i++){
    const serviceRow = createServiceRow()
    for(let j=0; j<inputFieldAttributes[i].length; j++){
      const serviceColumn = document.createElement('div')
      serviceColumn.className = 'col'
      const inputField = createInputField(inputFieldAttributes[i][j].fieldType, inputFieldAttributes[i][j].fieldName, 'form-control', inputFieldAttributes[i][j].placeHolder)
      serviceColumn.appendChild(inputField)
      serviceRow.appendChild(serviceColumn)
    }
    CAOPerationsPersonnelInformationGroup.appendChild(serviceRow)    
  }
  
  const hr = document.createElement('hr')
  CAOPerationsPersonnelInformationGroup.appendChild(hr)
  document.querySelector('#remove-personnel-button').style.display = 'grid'
}

const removePersonnel = () => {
  let personnelLabels = document.getElementsByClassName('personnel-label')
  personnelLabels[personnelLabels.length - 1].remove()
  
  for(let i=0; i<2; i++){
    let serviceRows = document.getElementsByClassName('service-row')
    serviceRows[serviceRows.length-1].remove()
  }
  if(document.getElementsByClassName('service-row').length === 2)
    document.querySelector('#remove-personnel-button').style.display = 'none'
}