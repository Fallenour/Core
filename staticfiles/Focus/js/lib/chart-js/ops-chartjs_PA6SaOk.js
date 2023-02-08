function ops_team_chart(labels1, defaultData1) {
  'use strict';

  //Team chart
  var ctx = document.getElementById('team-chart');
  ctx.height = 150;
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
      type: 'line',
      defaultFontFamily: 'Montserrat',
      datasets: [
        {
          data: [10, 7, 3, 5, 2, 10, 7],
          label: 'Adversary',
          backgroundColor: 'rgba(0,103,255,.15)',
          borderColor: 'rgba(0,103,255,0.5)',
          borderWidth: 3.5,
          pointStyle: 'circle',
          pointRadius: 5,
          pointBorderColor: 'transparent',
          pointBackgroundColor: 'rgba(0,103,255,0.5)',
        },
      ],
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
        xAxes: [
          {
            display: true,
            gridLines: {
              display: false,
              drawBorder: false,
            },
            scaleLabel: {
              display: false,
              labelString: 'Month',
            },
          },
        ],
        yAxes: [
          {
            display: true,
            gridLines: {
              display: false,
              drawBorder: false,
            },
            scaleLabel: {
              display: true,
              labelString: 'Value',
            },
          },
        ],
      },
      title: {
        display: false,
      },
    },
  });
}

(function generate_line_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_team_chart_labels;
        defaultData1 = data.ops_team_chart_default_items;
        ops_team_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();

