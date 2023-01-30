function ops_radar_chart(labels1, defaultData1) {
    console.log('defaultData1', defaultData1);
    console.log('labels1', labels1);
	//radar chart
	var ctx = document.getElementById( "radarChart" );
	ctx.height = 160;
	var myChart = new Chart( ctx, {
		type: 'radar',
		data: {
			labels: [ [ "Recon" ], [ "Weaponization" ], "Delivery", [ "Exploitation" ], "Installation", "C&C", "AOO" ],
			datasets: [
				{
					label: "Red Team",
					data: defaultData1,
					borderColor: "rgba(0, 123, 255, 0.6)",
					borderWidth: "1",
					backgroundColor: "rgba(0, 123, 255, 0.4)"
                            },
				{
					label: "Blue Team",
					data: [ 28, 12, 40, 19, 63, 27, 87 ],
					borderColor: "rgba(0, 123, 255, 0.7",
					borderWidth: "1",
					backgroundColor: "rgba(0, 123, 255, 0.5)"
                            }
                        ]
		},
		options: {
			legend: {
				position: 'top'
			},
			scale: {
				ticks: {
					beginAtZero: true
				}
			}
		}
  });
}

(function generate_radar_chart() {
  $(document).ready(function () {
    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];
    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function (data) {
        labels1 = data.ops_radar_chart_labels;
        defaultData1 = data.ops_radar_chart_default_items;
        ops_radar_chart(labels1, defaultData1);
      },
      error: function (error_data) {
        console.log('error');
        console.log(error_data);
        alert(data);
      },
    });
  });
})();