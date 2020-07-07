<template>
    <div class="container">
        <h2>Gráfico Relacionando Carros x Cores</h2>
        <GChart
            type="PieChart"
            :data="carrosCores"
        />

    </div>
</template>

<script>
import axios from 'axios'
import { GChart } from 'vue-google-charts'

export default {
  components: {
    GChart
  },
  data () {
    return {
        carrosCores: [['Cor', 'Nº Veículos']]
    }
  },
  mounted() {
      axios.get(this.$urlAPI+'/carros_cores')
           .then(response => {
               const carros = response.data
               carros.forEach(carro => {
                    this.carrosCores.push([carro.cor, carro.num])
               }) 
           })
  }  
}
</script>

<style scoped>

</style>