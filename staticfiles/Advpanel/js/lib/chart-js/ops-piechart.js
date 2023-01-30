function ops_pie_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
	//pie chart
	var ctx = document.getElementById( "pieChart" );
	ctx.height = 300;
	var myChart = new Chart( ctx, {
		type: 'pie',
		data: {
			datasets: [ {
				data: defaultData1,
				backgroundColor: [
                                    "rgba(0, 123, 255,0.9)",
                                    "rgba(0, 123, 255,0.7)",
                                    "rgba(0, 123, 255,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ],
				hoverBackgroundColor: [
                                    "rgba(0, 123, 255,0.9)",
                                    "rgba(0, 123, 255,0.7)",
                                    "rgba(0, 123, 255,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ]

                            } ],
			labels: [
                            "BR 1",
                            "BR 2",
                            "BR 3",
                            "BR 4"
                        ]
		},
		options: {
			responsive: true
		}
  });
}

(function generate_pie_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_pie_chart_labels;
        defaultData1 = data.ops_pie_chart_default_items;
        ops_pie_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();
