var delayTimer;
const autoComBox = document.getElementById('autocom-box')
const searchbar = document.getElementById('searchbar')
counter = -1
$('#searchbar').keypress(function() {
    document.onkeydown = checkKey;
    autoComBox.innerHTML = ""
    clearTimeout(delayTimer);
    delayTimer = setTimeout(function() {
        var text = $('#searchbar').val();
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
                        document.getElementById('searchbar').value = element
                        autoComBox.style.display = 'none'
                    }
                    autoComBox.appendChild(li)
                });
            },
        })
    }, 100)
})
document.addEventListener('mouseup', function(e) {
    if (!autoComBox.contains(e.target)) {
        autoComBox.style.display = 'none';
    }
});

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
            const current = autoComBox.children[counter]
            current.setAttribute("id", "hovered-li")
            current.style.background = '#DEB3EB'
            searchbar.value = current.innerHTML
            autoComBox.style.display = 'block'
        }
        // down
        else if (e.keyCode == '40' && searchbar === document.activeElement) {
            counter++
            const current = autoComBox.children[counter]
            current.setAttribute("id", "hovered-li")
            current.style.background = '#DEB3EB'
            searchbar.value = current.innerHTML
            autoComBox.style.display = 'block'
        }
        //delete
        else if (e.keyCode == '8') {
            counter = -1
        }
        // enter
        else if (e.keyCode == '13') {
            e.preventDefault()
            if ($(searchbar).is(':focus')) {
                if (searchbar.value.length == 0) {
                    console.log('empty')
                }
                autoComBox.style.display = 'none'
                searchbar.blur()
                return false
            } else {
                document.getElementById('tag-form').submit()
            }
        }
    } catch (err) {
        counter = -1
        console.log(err.message)
        checkKey
    }
}