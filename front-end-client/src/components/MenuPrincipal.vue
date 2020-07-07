<template>
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  
  <!-- Brand -->
  <img src="herbie.png" alt="Herbie" class="mx-3">
  <router-link class="navbar-brand" to="/">Revenda Herbie</router-link>

  <!-- Links -->
  <ul class="navbar-nav">

    <!-- Dropdown -->
    <li class="nav-item">
          <router-link class="nav-link" to="/cadcarros">Inicio</router-link>
        </li>
      
      <li class="nav-item">
          <router-link class="nav-link" to="/cadcarros">Empresa</router-link>
        </li>
      
      <li class="nav-item">
          <router-link class="nav-link" to="/cadcarros">Contato</router-link>
        </li>
      </ul>

      <ul class="navbar-nav ml-auto">
        <!-- Dropdown -->
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
            <i class="fas fa-user mr-1"></i>
            <span v-if="user">{{user}}</span>
            <span v-else>Área Restrita</span>
          </a>
          <div class="dropdown-menu">
            <router-link class="dropdown-item" to="/login">Login</router-link>
            <a class="dropdown-item" href="#" @click="sair">Logout</a>
          </div>
        </li>
      </ul>
</nav>    
</template>

<script>
export default {
  props: {
    user: String
  },
  methods: {
    sair() {
      localStorage.removeItem('token')
      this.$parent.mudaUser(null)
    }
  }
}
</script>

<style scoped>
img {
    width: 60px;
    height: 40px;
}
</style>