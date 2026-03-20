function ops_sales_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
  //Sales chart
  var ctx = document.getElementById('sales-chart');
  ctx.height = 150;
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
      type: 'line',
      defaultFontFamily: 'Montserrat',
      datasets: [
        {
          label: 'Red Team',
          data: defaultData1,
          backgroundColor: 'transparent',
          borderColor: 'rgba(220,53,69,0.75)',
          borderWidth: 3,
          pointStyle: 'circle',
          pointRadius: 5,
          pointBorderColor: 'transparent',
          pointBackgroundColor: 'rgba(220,53,69,0.75)',
        },
        {
          label: 'Blue Team',
          data: [0, 50, 40, 80, 40, 79, 120],
          backgroundColor: 'transparent',
          borderColor: 'rgba(40,167,69,0.75)',
          borderWidth: 3,
          pointStyle: 'circle',
          pointRadius: 5,
          pointBorderColor: 'transparent',
          pointBackgroundColor: 'rgba(40,167,69,0.75)',
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
        text: 'Normal Legend',
      },
    },
  });
}

(function generate_sales_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_sales_chart_labels;
        defaultData1 = data.ops_sales_chart_default_items;
        ops_sales_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();
