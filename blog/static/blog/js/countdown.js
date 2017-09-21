function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
    days    = parseInt(timer / (60 * 60 * 24), 10);
    hours   = parseInt(timer / (60 * 60) % 24, 10);
    minutes = parseInt((timer / 60) % 60, 10);
    seconds = parseInt(timer % 60, 10);
    
    display.innerHTML = '<div class="col-lg-3 col-6 text-center">' + '<span class="countdown-amount">' + days + '</span><span class="countdown-word">' + 'Jours' + '</span></div>' +
                        '<div class="col-lg-3 col-6 text-center">' + '<span class="countdown-amount">' + hours + '</span><span class="countdown-word">' + "Heures" + '</span></div>' +
                        '<div class="col-lg-3 col-6 text-center">' + '<span class="countdown-amount">' + minutes + '</span><span class="countdown-word">' + "Minutes" + '</span></div>' +
                        '<div class="col-lg-3 col-6 text-center">' + '<span class="countdown-amount">' + seconds + '</span><span class="countdown-word">' + "Secondes" + '</span></div>';

    if (--timer < 0) {
        timer = 0;
    }
    }, 1000);
}

window.onload = function () {
    var today = new Date();
    
    //Attention les mois commencent à 0 en Js
    var date_gala = new Date(2017, 10, 18, 19);
    
    var seconds = Math.round((date_gala - today) / 1000),
        display = document.querySelector('#gala-countdown');
    startTimer(seconds, display);
};
