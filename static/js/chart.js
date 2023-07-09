
const ctx = document.getElementById("myChart").getContext('2d');
const data = {
  datasets: [{
    data: [80, 20],
    backgroundColor: [
      '#9DCEFF',
      '#F2F3F6'
    ],
    scaleBeginAtZero: true,
    borderWidth:0,
    hoverOffset: 2,
  }]
}
const options = {
  cutout: '80%',
}

const centerText = {
  id: 'centerText',
  afterDatasetsDraw(chart, args, pluginOptions){
    const { ctx, data } = chart;
    const text = '80%';

    ctx.save();
    const x = chart.getDatasetMeta(0).data[0].x;
    const y = chart.getDatasetMeta(0).data[0].y;
  
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = 'bold 25px sans-serif';
    ctx.fillText(text, x, y)
  }
}

const myChart = new Chart(ctx, {
    type: 'doughnut',
    data,
    options,
    plugins: [centerText]
});

