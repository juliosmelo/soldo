var ctx = document.getElementById("chart_sales_month_line").getContext("2d")
var data = {
    labels: ["01", "02", "03", "04", "05", "06", "07"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [65, 59, 80, 81, 56, 55, 40]
        },
    ]
};

var options = {
	bezierCurve: true
}
var myLineChart = new Chart(ctx).Line(data, options);