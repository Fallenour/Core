function ops_singlebar_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
	// single bar chart
	var ctx = document.getElementById( "singelBarChart" );
	ctx.height = 150;
	var myChart = new Chart( ctx, {
		type: 'bar',
		data: {
			labels: [ "Sun", "Mon", "Tu", "Wed", "Th", "Fri", "Sat" ],
			datasets: [
				{
					label: "Instances per Day",
					data: defaultData1,
					borderColor: "rgba(0, 123, 255, 0.9)",
					borderWidth: "0",
					backgroundColor: "rgba(0, 123, 255, 0.5)"
                            }
                        ]
		},
		options: {
			scales: {
				yAxes: [ {
					ticks: {
						beginAtZero: true
					}
                                } ]
			}
		}
  });
}

(function generate_singlebar_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_singlebar_chart_labels;
        defaultData1 = data.ops_singlebar_chart_default_items;
        ops_singlebar_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();
