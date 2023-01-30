function ops_doughut_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
	//doughut chart
	var ctx = document.getElementById( "doughutChart" );
	ctx.height = 150;
	var myChart = new Chart( ctx, {
		type: 'doughnut',
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
                            "Metasploit",
                            "Atomic Red Canary",
                            "Custom Code",
                            "Custom Scripts"
                        ]
		},
		options: {
			responsive: true
		}
  });
}

(function generate_doughut_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_doughut_chart_labels;
        defaultData1 = data.ops_doughut_chart_default_items;
        ops_doughut_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();