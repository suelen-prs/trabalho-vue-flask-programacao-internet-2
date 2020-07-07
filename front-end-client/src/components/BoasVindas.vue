<template>
  <!--Carousel-->
  <div>
    <div id="demo" class="carousel slide" data-ride="carousel">
      <ul class="carousel-indicators">
        <li data-target="#demo" data-slide-to="0" class="active"></li>
        <li data-target="#demo" data-slide-to="1"></li>
        <li data-target="#demo" data-slide-to="2"></li>
      </ul>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="herbie.jpg" alt="Brinde" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Clássicos</h3>
            <p>Aqui você encontra modelos antigos com qualidade de zero</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="seminovos.jpg" alt="Chicago" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Seminovos</h3>
            <p>Aceitamos seu usado na troca</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="novos.jpg" alt="New York" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Novos</h3>
            <p>Encontre aqui o carro dos seus sonhos</p>
          </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#demo" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </a>
      <a class="carousel-control-next" href="#demo" data-slide="next">
        <span class="carousel-control-next-icon"></span>
      </a>
    </div>

    <!--Pesquisar-->

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-5">
      <div class="container">
        <input class="form-control mr-sm-2" type="text" v-model="filtro" placeholder="Pesquise por modelo" />
        <button class="btn btn-secondary my-2 my-sm-0" @click.prevent="pesquisar">Pesquisar</button>
      </div>
    </nav>

    <span v-if="filtro">
                        [Filtro: '{{filtro}}']
                    </span>

<!--Carros-->
 
<div class="container">
  <p class="lead">Confira os veículos destaques da semana</p>
  <hr class="my-4">
</div>

    <div class="container mb-5">
      <div class="row">

        <div class="col-sm-4" v-for="carro in carros" v-bind:key="carro.id">
          <div class="card mb-3">
            <h3 class="card-header card text-white bg-secondary">{{carro.modelo}}</h3>
            <div class="card-body bg-light">
              <h5 class="card-title">{{carro.marca}}</h5>
              <h6 class="card-subtitle text-muted">{{carro.ano}}</h6>
            </div>
            <img
              style="height: 200px; width: 100%; display: block;" v-bind:src="carro.foto" alt="Card image"/>
            <div class="card-body bg-light">
              <p class="card-text">R${{carro.preco | estiloMoeda}}</p>
            </div>
            <div class="card-body card-footer bg-secondary">
              <router-link to="/proposta" class="card-link">Faça sua proposta</router-link>
            </div>
          </div>
        </div>
      </div>
        </div>

        
  </div>
</template>



<script>
import axios from 'axios'

export default {
    data() {
        return {
            carros: []
        }
    },
    methods: {
        listar() {
            axios.get(this.$urlAPI+'/carros/destaque')
                 .then(response => this.carros = response.data) 
        },
        pesquisar() {
            axios.get(this.$urlAPI+'/carros/filtro/<modelo>')
                 .then(response => this.car = response.data) 
        }
    },
    mounted() {
        this.listar()
        this.pesquisar()
    },
    filters: {
        estiloMoeda(value) {
            return value.toLocaleString('pt-br', {minimumFractionDigits: 2})
        }
    }
}
</script>

<style scoped>
img {
  width: 120px;
  height: 60px;
}
.carousel-inner img {
  width: 1550px;
  height: 400px;
}


</style>