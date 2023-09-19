<template>
  <div class="detalhes-pessoa-view">
    <div class="card">
      <button class="voltar" @click="voltarParaHome">Voltar</button>
      <h2>Nome: {{ pessoa.nome }}</h2>
      <p>Função: {{ pessoa.funcao }}</p>
      <p>RG: {{ pessoa.rg }}</p>
      <p>CPF: {{ pessoa.cpf }}</p>
      <p>Data de Admissão{{ pessoa.data_admissao }}</p>
      <p>Data de Nascimento {{ pessoa.data_nascimento }}</p>
      <div class="button">
        <button class="edit" @click="editarPessoa(pessoa.id_pessoa)">
          <ion-icon name="create-outline"></ion-icon>Editar
        </button>
        <button class="delete" @click="excluirPessoa(pessoa.id_pessoa)">
          <ion-icon name="trash-outline"></ion-icon>Excluir
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pessoa: {
        nome: "",
        funcao: "",
        rg: "",
        cpf: "",
        data_admissao: "",
        data_nascimento: "",
      },
    };
  },
  mounted() {
    this.carregarPessoa();
  },
  methods: {
    formatarData(data) {
      const dataPessoa = new Date(data);
      const dia = String(dataPessoa.getDate()).padStart(2, "0");
      const mes = String(dataPessoa.getMonth() + 1).padStart(2, "0");
      const ano = dataPessoa.getFullYear();
      return `${dia}/${mes}/${ano}`;
    },
    carregarPessoa() {
      const pessoaId = this.$route.params.id;
      const apiUrl = `http://localhost:5000/api/v1/pessoas/${pessoaId}`;
      fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
          // this.pessoaEditada = data.pessoa;
          data.pessoa.data_admissao = this.formatarData(
            data.pessoa.data_admissao
          );
          data.pessoa.data_nascimento = this.formatarData(
            data.pessoa.data_nascimento
          );
          this.pessoa = data.pessoa;
        });
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
    voltarParaHome() {
      this.$router.push({ name: "home" }); // Navegue de volta para a página inicial
    },
  },
};
</script>

<style scoped>
.detalhes-pessoa-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Altura total da janela de visualização */
}

.card {
  background: #fff;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Sombra suave */
  border-radius: 5px;
  text-align: center;
}

.voltar {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  font-weight: bold;
}

.button {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.button .edit {
  background: #05c3dd;
  color: white;
  border: none;
  font-size: 17px;
  display: inline-block;
  border-radius: 5px 5px 5px 5px;
  cursor: pointer;
}

.button .delete {
  background: #d10808;
  color: white;
  border: none;
  font-size: 17px;
  display: inline-block;
  border-radius: 5px 5px 5px 5px;
  cursor: pointer;
}
.voltar:hover {
  background-color: #0056b3;
}
</style>
