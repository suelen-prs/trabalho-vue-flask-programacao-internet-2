import Vue from 'vue'
import VueRouter from 'vue-router'

import BoasVindas from './components/BoasVindas.vue'
import Proposta from './components/Proposta.vue'
import CadastroCarros from './components/CadastroCarros.vue'
import FormCarros from './components/FormCarros.vue'
import FormLogin from './components/FormLogin.vue'
import GraficoCarrosMarcas from './components/GraficoCarrosMarcas.vue'
import GraficoCarrosCores from './components/GraficoCarrosCores.vue'
import GraficoCadastros from './components/GraficoCadastros.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: BoasVindas },
        { path: '/proposta', component: Proposta },
        { path: '/cadcarros', component: CadastroCarros},
        { path: '/formcarros', component: FormCarros},
        { path: '/grafcarrosmarcas', component: GraficoCarrosMarcas},
        { path: '/grafcarroscores', component: GraficoCarrosCores},
        { path: '/grafcadastros', component: GraficoCadastros},
        { path: '/login', component: FormLogin},
    ]
})