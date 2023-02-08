function ops_polar_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
	//polar chart
	var ctx = document.getElementById( "polarChart" );
	ctx.height = 150;
	var myChart = new Chart( ctx, {
		type: 'polarArea',
		data: {
			datasets: [ {
				data: [ 15, 18, 9, 6, 19 ],
				backgroundColor: [
                                    "rgba(0, 123, 255,0.9)",
                                    "rgba(0, 123, 255,0.8)",
                                    "rgba(0, 123, 255,0.7)",
                                    "rgba(0,0,0,0.2)",
                                    "rgba(0, 123, 255,0.5)"
                                ]

                            } ],
			labels: [
                            "Exploit Kits",
                            "Exfiltration",
                            "Metasploit",
                            "Atomic Red",
                            "Custom"
                        ]
		},
		options: {
			responsive: true
		}
  });
}

(function generate_polar_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_polar_chart_labels;
        defaultData1 = data.ops_polar_chart_default_items;
        ops_polar_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();