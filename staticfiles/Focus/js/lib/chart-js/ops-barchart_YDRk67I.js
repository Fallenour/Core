function ops_bar_chart(labels1, defaultData1) {
  //bar chart
  var canvas = document.getElementById('barChart');
  var ctx = canvas.getContext('2d');
  //    ctx.height = 200;
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
        {
          label: '2020 Total Attempted',
          data: defaultData1,
          borderColor: 'rgba(0, 123, 255, 0.9)',
          borderWidth: '0',
          backgroundColor: 'rgba(0, 123, 255, 0.5)',
        },
        {
          label: '2021 Total Completed',
          data: [28, 48, 40, 19, 86, 27, 90],
          borderColor: 'rgba(0,0,0,0.09)',
          borderWidth: '0',
          backgroundColor: 'rgba(0,0,0,0.07)',
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    },
  });
}

(function generate_bar_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_team_chart_labels;
        defaultData1 = data.ops_team_chart_default_items;
        ops_bar_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();