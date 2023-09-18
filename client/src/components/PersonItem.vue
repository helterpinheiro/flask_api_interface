<template>
  <div class="pessoa">
    <div class="img">
      <img :src="require('@/assets/user.png')" alt="imagem de um funcionário" />
    </div>
    <div class="details">
      <h4>Nome: {{ pessoa.nome.split(" ")[0] }}</h4>
    </div>
    <div class="footer">
      <span class="funcao"
        >Adimissão: {{ formatarData(pessoa.data_admissao) }}</span
      >
      <span class="funcao">{{ pessoa.funcao }}</span>
    </div>
    <button @click="editarPessoa(pessoa.id_pessoa)">Editar</button>
    <button @click="excluirPessoa(pessoa.id_pessoa)">Excluir</button>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["pessoa"],
  methods: {
    formatarData(data) {
      const options = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(data).toLocaleDateString("pt-BR", options);
    },

    editarPessoa(id) {
      this.$router.push({ name: "editar", params: { id } });
    },
  },
};
</script>

<!-- Estilizacao da pagina -->
<style lang="scss">
body {
  background: #e8e8e8;
  padding: 20px;
}
.pessoa {
  padding: 5px;
  flex-basis: 0;
  background: #ffffff;
  margin-bottom: 10px;
  box-shadow: 1px 4px 4px rgba(0, 0, 0, 0.24);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.pessoa .img {
  text-align: center;
}

.pessoa .img img {
  height: 297px;
  width: 210px;
  align-self: center;
  object-fit: cover;
}

.pessoa p {
  text-align: justify;
  padding: 4px;
}

.pessoa .footer {
  padding: 5px 10px;
  display: flex;
  justify-content: center;
  flex: 1;
}

.pessoa .funcao {
  background: #f0f0f0;
  padding: 5px;
}

.pessoa .details span {
  font-weight: 300;
}
</style>
