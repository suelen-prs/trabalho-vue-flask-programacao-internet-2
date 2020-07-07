<template>
  <div class="container">
    <h2>Gráfico Relacionando Nº de Veículos por Marca</h2>
    <GChart
       type="PieChart"
       :data="carrosMarcas"
    />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import axios from 'axios'

export default {
  components: {
    GChart
  },
  data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      carrosMarcas: [['Marca', 'Nº Veículos']]
     }
  },
  mounted() {
      axios.get(this.$urlAPI + '/marcas')
           .then(response => {
               const marcas = response.data;
               marcas.forEach(marca => {
                  if (marca.num_carros > 0) {
                      this.carrosMarcas.push([marca.nome, marca.num_carros])                    
                  }
               });
           });
  }
};
</script>

<style scoped>
</style>