( function ops_team_chart( $ ) {
	"use strict";

	//Team chart
	var ctx = document.getElementById( "team-chart" );
	ctx.height = 150;
	var myChart = new Chart( ctx, {
		type: 'line',
		data: {
			labels: [ "2010", "2011", "2012", "2013", "2014", "2015", "2016" ],
			type: 'line',
			defaultFontFamily: 'Montserrat',
			datasets: [ {
				data: [ 10, 7, 3, 5, 2, 10, 7 ],
				label: "Expense",
				backgroundColor: 'rgba(0,103,255,.15)',
				borderColor: 'rgba(0,103,255,0.5)',
				borderWidth: 3.5,
				pointStyle: 'circle',
				pointRadius: 5,
				pointBorderColor: 'transparent',
				pointBackgroundColor: 'rgba(0,103,255,0.5)',
                    }, ]
		},
		options: {
			responsive: true,
			tooltips: {
				mode: 'index',
				titleFontSize: 12,
				titleFontColor: '#000',
				bodyFontColor: '#000',
				backgroundColor: '#fff',
				titleFontFamily: 'Montserrat',
				bodyFontFamily: 'Montserrat',
				cornerRadius: 3,
				intersect: false,
			},
			legend: {
				display: false,
				position: 'top',
				labels: {
					usePointStyle: true,
					fontFamily: 'Montserrat',
				},


			},
			scales: {
				xAxes: [ {
					display: true,
					gridLines: {
						display: false,
						drawBorder: false
					},
					scaleLabel: {
						display: false,
						labelString: 'Month'
					}
                        } ],
				yAxes: [ {
					display: true,
					gridLines: {
						display: false,
						drawBorder: false
					},
					scaleLabel: {
						display: true,
						labelString: 'Value'
					}
                        } ]
			},
			title: {
				display: false,
			}
		}
    })(jQuery);
