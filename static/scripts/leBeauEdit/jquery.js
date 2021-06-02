var delayTimer;
const autoComBox = document.getElementById('autocom-box')
const searchbar = document.getElementById('searchbar')
const p = document.getElementById('tags')
const lebeauCode = document.getElementById('lebeau_code').value
counter = -1
$('#searchbar').keypress(function(e) {
    console.log('goi')
    document.onkeydown = checkKey;
    autoComBox.innerHTML = ""
    clearTimeout(delayTimer);
    delayTimer = setTimeout(function() {
        var text = $('#searchbar').val();
        $('#searchbar').on('keydown', function() {
            var key = event.keyCode || event.charCode;
            if (key == 8 || key == 46)
                autoComBox.style.display = 'none'
            autoComBox.style.display = 'none'
        });
        $.ajax({
            url: '/leBeau%5Etags',
            data: {
                'search': text,
            },
            dataType: 'json',
            success: function(data) {
                const tags = data['response']
                tags.forEach(element => {
                    autoComBox.style.display = 'block'
                    const li = document.createElement('li')
                    li.innerHTML = element
                    li.onclick = function() {
                        addTag(element)
                    }
                    autoComBox.appendChild(li)
                });
            }
        })
    }, 100)
})
document.addEventListener('mouseup', function(e) {
    if (!autoComBox.contains(e.target)) {
        autoComBox.style.display = 'none';
    }
});
const tagDelete = (tag) => {
    tag.remove()
}
const addTag = (element) => {
    let span = document.createElement('span')
    span.innerHTML = element.toLowerCase()
    span.classList.add('tag')
    span.setAttribute("onclick", "tagDelete(this)")
    p.appendChild(span)
}
const onSave = () => {
    // check code
    const code = document.getElementById('code').value
    if (code != lebeauCode) {
        alert('Access Denied, Wrong Code')
        return false
    }
    // create str rep of list for backend
    const tags = document.getElementsByClassName('tag')
    const payload = []
    for (const element of Object.values(tags)) {
        const tag = element.innerHTML
        payload.push("'" + tag.trim() + "'")
    }
    const payloadInput = document.getElementById('id_tags')
    payloadInput.value = ""
    payloadInput.value = "[" + payload + "]"
    // change any uppercase chars to lowercase
    const item = document.getElementById('id_item')
    item.value = item.value.toLowerCase()
}
const confirmDelete = () => {
    // check code
    const code = document.getElementById('code').value
    if (code != lebeauCode) {
        alert('Access Denied, Wrong Code')
        return false
    }
    // confirm
    const form = document.getElementById('form')
    if (!confirm('Are you sure you wish to delete?')) {
        return false
    } else {
        form.submit()
    }
}

function checkKey(e) {
    const previous = document.getElementById('hovered-li')
    if (previous != null) {
        previous.style.background = '#fff'
        previous.removeAttribute("id")
    }
    e = e || window.event;
    try {
        // up
        if (e.keyCode == '38' && searchbar === document.activeElement) {
            counter--
            try {
                setTag(counter)
            } catch {
                console.log('error')
            }
        }
        // down
        else if (e.keyCode == '40' && searchbar === document.activeElement) {
            counter++
            try {
                setTag(counter)
            } catch {
                autoComBox.style.display = 'block'
            }
        }
        //delete
        else if (e.keyCode == '8') {
            counter = -1
        } else if (e.keyCode == '13' && searchbar.value.length != 0) {
            counter = -1
            e.preventDefault()
            addTag(searchbar.value)
            autoComBox.style.display = 'none'
            searchbar.value = ''
            return false
        }
    } catch (err) {
        counter = -1
        console.log(err.message)
        checkKey
    }
}

function setTag(counter) {
    let x = autoComBox.children[counter]
    console.log(x)
    const current = autoComBox.children[counter]
    current.setAttribute("id", "hovered-li")
    current.style.background = '#DEB3EB'
    searchbar.value = current.innerHTML
    autoComBox.style.display = 'block'
}