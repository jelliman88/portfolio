// get a tag inside form, get parent and give class (django imageField can't be changed)
const imageField = document.getElementById("id_thumbnail").parentElement
imageField.classList.add('image-field')

// clone image upload button and append to form
const form = document.getElementById('form-inputs')
const imageButton = document.getElementById('id_thumbnail')
let buttonClone = imageButton.cloneNode()
buttonClone.id = 'id_thumbnail_clone'
let clonedP = document.createElement('p').appendChild(buttonClone)
clonedP.classList.add('image-field-clone')
form.insertBefore(clonedP, form.children[5]);

const addTagMobile = () => {
    const input = document.getElementById('searchbar').value
    let span = document.createElement('span')
    span.innerHTML = input.toLowerCase()
    span.classList.add('tag')
    span.setAttribute("onclick", "tagDelete(this)")
    p.appendChild(span)
}