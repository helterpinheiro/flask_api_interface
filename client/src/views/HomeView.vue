<template>
  <div>
    <PersonList :pessoas="pessoas" />
    <div class="">
      <button @click="criarFuncionario">Criar funcionário</button>
      <button @click="anteriorPagina" :disabled="page === 1">
        Página Anterior
      </button>
      <button @click="proximaPagina" :disabled="page === totalPages">
        Próxima Página
      </button>
    </div>
  </div>
</template>

<script>
import PersonList from "@/components/PersonList.vue";

export default {
  name: "HomeView",
  components: {
    PersonList,
  },
  data() {
    return {
      pessoas: [],
      page: 1,
      perPage: 8,
      totalPages: 3,
      exibirModal: false,
    };
  },
  methods: {
    anteriorPagina() {
      if (this.page > 1) {
        this.page--;
        this.carregarPessoas();
      }
    },

    proximaPagina() {
      if (this.page < this.totalPages) {
        this.page++;
        this.carregarPessoas();
      }
    },

    carregarPessoas() {
      const apiUrl = `http://localhost:5000/api/v1/pessoas?page=${this.page}&per_page=${this.perPage}`;
      fetch(apiUrl).then((response) =>
        response.json().then((json) => {
          this.pessoas = json.pessoas;
          console.log(this.pessoas);
        })
      );
    },

    criarFuncionario() {
      this.$router.push({ name: "create" });
    },
  },
  mounted() {
    this.carregarPessoas();
  },
};
</script>
