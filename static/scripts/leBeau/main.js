const lebeauCode = document.getElementById('lebeau_code').value
console.log(lebeauCode)

const showForm = () => {
    const form = document.getElementById('leBeauForm')
    const button = document.getElementById('lebeau-show-button')
    form.style.display = 'block'
    button.style.display = 'none'
}
const hideForm = () => {
    const form = document.getElementById('leBeauForm')
    const button = document.getElementById('lebeau-show-button')
    form.style.display = 'none'
    button.style.display = 'unset'
}
const onSave = () => {
    const code = document.getElementById('code').value
    if (code != lebeauCode ) {
        alert('Access Denied, Wrong Code')
        return false
    }
    const item = document.getElementById('id_item')
    item.value = item.value.toLowerCase()
}
const showTagForm = () => {
    const form = document.getElementById('tag-form')
    const button = document.getElementById('tag-form-show-button')
    form.style.display = 'block'
    button.style.display = 'none'
}
const hideTagForm = () => {
    const form = document.getElementById('tag-form')
    const button = document.getElementById('tag-form-show-button')
    form.style.display = 'none'
    button.style.display = 'unset'
}