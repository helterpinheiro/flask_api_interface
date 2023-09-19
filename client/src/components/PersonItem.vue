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
    <div class="button">
      <button class="edit" @click="editarPessoa(pessoa.id_pessoa)">
        <ion-icon name="create-outline"></ion-icon>Editar
      </button>
      <button class="vermais" @click="exibirInfo(pessoa.id_pessoa)">
        <ion-icon name="eye-outline"></ion-icon>Ver mais
      </button>
      <button class="delete" @click="excluirPessoa(pessoa.id_pessoa)">
        <ion-icon name="trash-outline"></ion-icon>Excluir
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["pessoa"],
  data() {
    return { exibirDetalhes: false };
  },
  methods: {
    formatarData(data) {
      const options = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(data).toLocaleDateString("pt-BR", options);
    },

    editarPessoa(id) {
      this.$router.push({ name: "editar", params: { id } });
    },

    excluirPessoa(id) {
      const apiUrl = `http://localhost:5000/api/v1/pessoas/${id}`;
      fetch(apiUrl, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.ok) {
            this.$router.go();
          } else {
            console.error("Erro ao excluir pessoa.");
          }
        })
        .catch((error) => {
          console.error(
            "Erro ao enviar solicitação para excluir pessoa",
            error
          );
        });
    },
    exibirInfo(id) {
      this.$router.push({ name: "info", params: { id } });
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

.pessoa .button {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.pessoa .edit {
  background: #05c3dd;
  color: white;
  border: none;
  font-size: 17px;
  display: inline-block;
  border-radius: 5px 5px 5px 5px;
  cursor: pointer;
}

.pessoa .delete {
  background: #d10808;
  color: white;
  border: none;
  font-size: 17px;
  display: inline-block;
  border-radius: 5px 5px 5px 5px;
  cursor: pointer;
}

.pessoa .vermais {
  background: #e4d50d;
  color: white;
  border: none;
  font-size: 17px;
  display: inline-block;
  border-radius: 5px 5px 5px 5px;
  cursor: pointer;
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
