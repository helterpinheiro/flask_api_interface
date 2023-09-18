<template>
  <div>
    <PersonList :pessoas="pessoas" />
    <div class="">
      <button @click="anteriorPagina" :disabled="page === 1">Anterior</button>
      <button @click="proximaPagina" :disabled="page === totalPages">
        Próxima
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
  },
  mounted() {
    this.carregarPessoas();
  },
};
</script>
