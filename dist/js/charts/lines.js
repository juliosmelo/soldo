$(function () {
    $('#chart_sales_month_line').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Vendas por dia Maio 2015'
        },
        xAxis: {
            categories: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        },
        yAxis: {
            title: {
                text: 'Temperature (°C)'
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: [{
            name: 'Maio',
            data: [100, 77, 70, 105, 90, 80, 40, 20, 18, 56, 80, 10]
        },
        ]
    });
});