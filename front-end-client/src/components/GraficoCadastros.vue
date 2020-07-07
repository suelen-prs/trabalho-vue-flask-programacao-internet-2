<template>
  <div id='app' class="container">
  <GChart
    :settings="{packages: ['bar']}"    
    :data="chartData"
    :options="chartOptions"
    :createChart="(el, google) => new google.charts.Bar(el)"
    @ready="onChartReady"
  />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    GChart
  },
  data () {
    return {
      chartsLib: null, 
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [['Meses', 'Nº Veículos']]
    }
  },
  mounted() {
      axios.get(this.$urlAPI+'/cadastros')
           .then(response => {
               const carros = response.data
               carros.forEach(carro => {
                    this.chartData.push([carro.anomes, carro.num])
               }) 
           })
  },
  computed: {
    chartOptions () {
      if (!this.chartsLib) return null
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Gráfico Relacionando Cadastro de Veículos',
          subtitle: 'Últimos 6 meses'
        },
        bars: 'horizontal', // Required for Material Bar Charts.
        hAxis: { format: 'decimal' },
        height: 380,
        colors: ['#1b9e77', '#d95f02']
      })
    }
  },
  methods: {
    onChartReady (chart, google) {
      this.chartsLib = google
    }
  }
}
</script>
