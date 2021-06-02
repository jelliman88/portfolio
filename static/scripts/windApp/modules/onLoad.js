
// converts object data to array
const toArray = (obj) => {
    let myArray = Object.values(obj)
    return myArray

}
// sorts wind data
const getWind = (wind) => {
    const windData = toArray(wind)
    const speed = document.getElementById('wind-speed')
    speed.innerHTML = windData[0]
    document.getElementById('wind-direction').innerHTML = windData[1]
}

// sorts main weather
const getMain = (main) => {
    // get ul
    const ul = document.getElementById('weather-list')
    // alt names for fields
    const textObj = {
        temp : 'Temp',
        feels_like : 'Feel', 
        temp_min : 'Min',
        temp_max : 'Max',
        humidity : 'Humid',
    }
    
    // loop through weather data
    for(let [key, value] of Object.entries(main)) {
        // skip over pressure
        if(key === "pressure") {
            continue
        }
        // create li
        const li = document.createElement("li")
        // create data
        const dataDiv = document.createElement("div")
        //check for humidity or temp
        if(key === 'humidity'){
            dataDiv.appendChild(document.createTextNode(`${Math.round(value)}%`))
        }else {
            dataDiv.appendChild(document.createTextNode(`${Math.round(value)}˚`))
        }
        // create text
        const textDiv = document.createElement("div")
        textDiv.innerHTML = textObj[key]
        // add class
        li.classList.add('circle')
        textDiv.classList.add('text')
        dataDiv.classList.add("stat")
        // append to DOM
        li.appendChild(textDiv)
        li.appendChild(dataDiv)
        ul.appendChild(li)
}
}

// get weather icon
const getForcast = (forcast) => {
    // icons object
    const forcastIcons = {
        Clouds: '<i class="fas fa-cloud"></i>',
        Clear: '<i class="fas fa-sun"></i>',
        Rain: '<i class="fas fa-cloud-rain"></i>'
    }
    // get ul, make li
    const ul = document.getElementById('forcast-list')
    const li = document.createElement("li")
    // make divs
    const textDiv = document.createElement("div")
    const iconDiv = document.createElement("div")
    // save inner html
    const text = forcast[0].main
    const icon = forcastIcons[text]
    // set
    textDiv.innerHTML = text
    iconDiv.innerHTML = icon
    //add classes
    textDiv.classList.add('text')
    li.classList.add('circle')
    // append to DOM
    li.appendChild(iconDiv)
    li.appendChild(textDiv)
    ul.appendChild(li)
}

// Google maps Api
let map;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 55.6459, lng: 12.5655 },
    zoom: 10,
  });
}


export default function showStats(data){
    getWind(data.wind)
    getMain(data.main)
    getForcast(data.weather)
    initMap()
    
    }
