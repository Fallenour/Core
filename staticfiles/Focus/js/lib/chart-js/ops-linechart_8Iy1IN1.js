function ops_line_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
  var ctx = document.getElementById('lineChart');
  ctx.height = 150;
  console.log($);
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
        {
          label: 'Attempted',
          borderColor: 'rgba(0,0,0,.09)',
          borderWidth: '1',
          backgroundColor: 'rgba(0,0,0,.07)',
          data: defaultData1,
        },
        {
          label: 'Completed',
          borderColor: 'rgba(0, 123, 255, 0.9)',
          borderWidth: '1',
          backgroundColor: 'rgba(0, 123, 255, 0.5)',
          pointHighlightStroke: 'rgba(26,179,148,1)',
          data: [16, 32, 18, 26, 42, 33, 44],
        },
      ],
    },
    options: {
      responsive: true,
      tooltips: {
        mode: 'index',
        intersect: false,
      },
      hover: {
        mode: 'nearest',
        intersect: true,
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
        labels1 = data.ops_line_chart_labels;
        defaultData1 = data.ops_line_chart_default_items;
        ops_line_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();
