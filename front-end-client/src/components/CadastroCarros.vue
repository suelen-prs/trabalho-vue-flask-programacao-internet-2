<template>
    <div class="container">
        <h2>Cadastro de Veículos
            <router-link to="/formcarros" class="btn btn-success float-right">
                <i class="fas fa-plus-circle"></i> Adicionar
            </router-link>
        </h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Modelo</th>
                    <th>Marca</th>
                    <th>Cor</th>
                    <th>Ano</th>
                    <th>Preço R$</th>
                    <th>Foto</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="carro in carros" v-bind:key="carro.id">
                    <td>{{carro.modelo}}</td>
                    <td>{{carro.marca}}</td>
                    <td>{{carro.cor}}</td>
                    <td class="text-center">{{carro.ano}}</td>
                    <td class="text-right">{{carro.preco | estiloMoeda}}</td>
                    <td class="text-center"><img v-bind:src="carro.foto" alt="Foto do Carro"></td>
                    <td class="text-center">
                        <a href="#" class="btn btn-sm btn-warning" title="Alterar">
                            <i class="far fa-edit"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-danger mx-1" title="Excluir">
                            <i class="fas fa-minus-circle"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-info" title="Destacar">
                            <i class="far fa-star"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
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
            axios.get(this.$urlAPI+'/carros')
                 .then(response => this.carros = response.data) 
        }
    },
    mounted() {
        this.listar()
    },
    filters: {
        estiloMoeda(value) {
            return value.toLocaleString('pt-br', {minimumFractionDigits: 2})
        }
    }
}
</script>

<style scoped>
table img {
    width: 100px;
    height: 60px;
}
</style>