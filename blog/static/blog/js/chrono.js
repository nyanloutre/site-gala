/*
* @Author: klmp200
* @Date:   2016-07-09 21:50:07
* @Last Modified by:   klmp200
* @Last Modified time: 2016-07-10 19:01:02
*/

'use strict';

function SetChrono(file) {

	var now = new Date();
	var gala = new Date();
	var diff = 0;

	$.getJSON(file, function(data) {

		gala.setFullYear(data.year, data.month - 1, data.day);
		diff = gala.getTime() - now.getTime();
		// Il faut retirer 1 au mois puisque l'indice commence à 0
		diff = Math.floor(diff / (1000 * 60 * 60 * 24));
		if (diff < 0){
			diff = 0;
		}

		$(".days").html(diff);

	});

}