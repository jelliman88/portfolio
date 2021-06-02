import showStats  from './modules/onLoad.js'



function getWeather() {
  
    //fetch('http://localhost:3000/weather')
    
  fetch('http://api.openweathermap.org/data/2.5/weather?q=Copenhagen&units=metric&appid=99eda32a191cd31baeb1c251003f25e2')
.then(response => response.json())
.then(data => showStats(data))

}

//getWeather()




