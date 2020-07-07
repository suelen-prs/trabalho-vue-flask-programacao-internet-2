<template>
  <div>
    <div class="container">
      <p class="lead">Confira os veículos destaques da semana</p>
      <hr class="my-4" />
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
              style="height: 200px; width: 100%; display: block;"
              v-bind:src="carro.foto"
              alt="Card image"
            />
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

    <form>
      <fieldset>
        <legend>Proposta</legend>
        <div class="form-group">
          <label for="exampleInputNome">Nome</label>
          <input type="text" class="form-control" id="exampleInputNome" />
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">Email</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="seu_email@exemplo.com"/>
          <small id="emailHelp" class="form-text text-muted">Nunca compartilharemos seu email com mais ninguém.</small>
        </div>
        <div class="form-group">
          <label for="exampleInputContato">Contato</label>
          <input type="text" class="form-control" id="exampleInputContato" />
        </div>
        <div class="form-group">
          <label for="exampleTextarea">Proposta</label>
          <textarea class="form-control" id="exampleTextarea" rows="3"></textarea>
        </div>
      </fieldset>
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
</style>