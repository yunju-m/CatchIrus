
const ctx = document.getElementById("myChart").getContext('2d');

// chart 호출(Get)
crateChart();

// chart 생성
async function crateChart() {
  const predict_model = await fetchDataFromModel();
  const text = predict_model.proba
  const result = predict_model.result
  let backgroundColor;
  if (result == "Benign") {
    backgroundColor = ['#9DCEFF', '#F2F3F6'];
  } else if (result == "Malware") {
    backgroundColor = ['#FF0000', '#F2F3F6'];
  }

  const data = {
    datasets: [{
      data: [100, 0],
      backgroundColor: backgroundColor,
      scaleBeginAtZero: true,
      borderWidth:0,
      hoverOffset: 2,
    }]
  };

  const options = {
    cutout: '80%',
  };

  const centerText = {
    id: 'centerText',
    afterDatasetsDraw(chart, args, pluginOptions){
      const { ctx, data } = chart;

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
}

// 모델 결과 값 불러오는 함수
async function fetchDataFromModel() {
  const apiUrl = '/file/chart';
  try {
      const response = await fetch(apiUrl);
      if (response.ok){
        const data = await response.json();
        return data;
      } else{
        console.error('Error fetching chart data:', response.status);
      }
  } catch (error) {
      console.error('Error fetching data from the model:', error);
      return null;
  }
}