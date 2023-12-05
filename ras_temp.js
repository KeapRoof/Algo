const fetch = require('node-fetch'); // You may need to install the 'node-fetch' package

function convertKelvinToCelsius(temp) {
    return temp - 273.15;
}

async function getWeatherData(lat, lon, key) {
    const apilinkCurrent = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`;
    const apilinkForecast = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${key}`;

    const responseForecast = await fetch(apilinkForecast);
    const responseCurrent = await fetch(apilinkCurrent);

    const jsonFor = await responseForecast.json();
    const jsonCur = await responseCurrent.json();

    const globalWeatherCur = jsonCur.weather[0].main;
    const tempCur = convertKelvinToCelsius(jsonCur.main.temp_max);

    console.log("Le minimum du jour : " + getMinDay(jsonFor) + "*C");
    console.log("Le maximum du jour : " + getMaxDay(jsonFor) + "*C");
    console.log("Le temps actuel : " + globalWeatherCur);
    console.log("La temperature actuelle : " + tempCur + "*C");
    
    return {
        "min": getMinDay(jsonFor),
        "max": getMaxDay(jsonFor),
        "current": tempCur,
        "weather": globalWeatherCur
    };
}

function getMinDay(jsonFor) {
    let minDay = -100000;
    for (let i = 0; i < 12; i++) {
        if (jsonFor.list[i].main.temp_min > minDay) {
            minDay = jsonFor.list[i].main.temp_min;
        }
    }
    return parseInt(convertKelvinToCelsius(minDay));
}

function getMaxDay(jsonFor) {
    let maxDay = 100000;
    for (let i = 0; i < 12; i++) {
        if (jsonFor.list[i].main.temp_max < maxDay) {
            maxDay = jsonFor.list[i].main.temp_max;
        }
    }
    return parseInt(convertKelvinToCelsius(maxDay));
}

const lat = 45.764671;
const lon = 4.8804;
const language = "en";
const key = "bdeb8474ac275502254ef9113a922598";

getWeatherData(lat, lon, key);

//Make the api call every 10 minutes
setInterval(function () {
    getWeatherData(lat, lon, key);
}, 600000);

