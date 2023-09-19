<template>
  <div class="editar-pessoa">
    <!-- Card de edição de pessoa -->
    <div class="card">
      <h2>Editar {{ pessoaEditada.nome }}</h2>
      <form @submit.prevent="salvarEdicao">
        <!-- Campos do formulário aqui -->
        <div>
          <label class="label" for="nome">Nome:</label>
          <input type="text" id="nome" v-model="pessoaEditada.nome" required />
        </div>
        <div>
          <label class="label" for="funcao">Função:</label>
          <input
            type="text"
            id="funcao"
            v-model="pessoaEditada.funcao"
            required
          />
        </div>
        <div>
          <label class="label" for="rg">RG:</label>
          <input type="text" id="rg" v-model="pessoaEditada.rg" />
        </div>
        <div>
          <label class="label" for="cpf">CPF:</label>
          <input type="text" id="cpf" v-model="pessoaEditada.cpf" />
        </div>
        <div>
          <label class="label" for="data_admissao">Data de Admissão:</label>
          <input
            type="date"
            id="data_admissao"
            v-model="pessoaEditada.data_admissao"
          />
        </div>
        <div>
          <label class="label" for="data_nascimento">Data de Nascimento:</label>
          <input
            type="date"
            id="data_nascimento"
            v-model="pessoaEditada.data_nascimento"
          />
        </div>
        <!-- Outros campos do formulário -->
        <button type="submit">Salvar</button>
        <button @click="voltarParaHome">Cancelar</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pessoaEditada: {
        nome: "",
        funcao: "",
        rg: "",
        cpf: "",
        data_admissao: "",
        data_nascimento: "",
        // Outros campos da pessoa aqui
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
      return `${ano}-${mes}-${dia}`;
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
          this.pessoaEditada = data.pessoa;
          console.log(this.pessoaEditada);
        });
    },
    salvarEdicao() {
      const pessoaId = this.$route.params.id;
      const apiUrl = `http://localhost:5000/api/v1/pessoas/${pessoaId}`;
      console.log("PESSOA EDITADA->", this.pessoaEditada);
      fetch(apiUrl, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.pessoaEditada),
      })
        .then((response) => {
          console.log(this.pessoaEditada);
          if (response.ok) {
            this.$router.push({ name: "home" });
          } else {
            console.error("Erro ao atualizar a pessoa.");
          }
        })
        .catch((error) => {
          console.error("Erro ao enviar a solicitação de edição", error);
        });
    },
    voltarParaHome() {
      this.$router.push({ name: "home" }); // Navegue de volta para a página inicial
    },
  },
};
</script>

<style lang="scss">
.editar-pessoa {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Centraliza verticalmente na tela inteira */
}

.label {
  width: 120px;
  display: inline-block;
}

.card {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 400px; /* Largura do card de edição */
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

label {
  margin-bottom: 5px;
}

input,
button {
  margin: 5px 0;
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background: #007bff;
  color: #fff;
  cursor: pointer;
}
</style>
