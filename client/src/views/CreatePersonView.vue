<template>
  <div class="editar-pessoa">
    <!-- Card de edição de pessoa -->
    <div class="card">
      <h2>Criar funcionário</h2>
      <form @submit.prevent="salvarPessoa">
        <!-- Campos do formulário aqui -->
        <div>
          <label class="label" for="nome">Nome:</label>
          <input type="text" id="nome" v-model="pessoaCriada.nome" required />
        </div>
        <div>
          <label class="label" for="funcao">Função:</label>
          <input
            type="text"
            id="funcao"
            v-model="pessoaCriada.funcao"
            required
          />
        </div>
        <div>
          <label class="label" for="rg">RG:</label>
          <input type="text" id="rg" v-model="pessoaCriada.rg" required />
        </div>
        <div>
          <label class="label" for="cpf">CPF:</label>
          <input type="text" id="cpf" v-model="pessoaCriada.cpf" required />
        </div>
        <div>
          <label class="label" for="data_admissao">Data de Admissão:</label>
          <input
            type="date"
            id="data_admissao"
            v-model="pessoaCriada.data_admissao"
            required
          />
        </div>
        <div>
          <label class="label" for="data_nascimento">Data de Nascimento:</label>
          <input
            type="date"
            id="data_nascimento"
            v-model="pessoaCriada.data_nascimento"
            required
          />
        </div>
        <!-- Outros campos do formulário -->
        <button class="butao" type="submit">Salvar</button>
        <button class="butao" @click="voltarParaHome">Cancelar</button>
        <!-- Alerta de erro -->
        <div v-if="erro" class="alert alert-danger">
          {{ erro }}
        </div>
        <div v-if="sucesso" class="alert alert-success">
          {{ sucesso }}
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sucesso: null,
      erro: null,
      pessoaCriada: {
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
  methods: {
    formatarData(data) {
      const dataPessoa = new Date(data);
      const dia = String(dataPessoa.getDate()).padStart(2, "0");
      const mes = String(dataPessoa.getMonth() + 1).padStart(2, "0");
      const ano = dataPessoa.getFullYear();
      return `${ano}-${mes}-${dia}`;
    },
    salvarPessoa() {
      const apiUrl = `http://localhost:5000/api/v1/pessoas`;
      fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.pessoaCriada),
      })
        .then((response) => {
          console.log(this.pessoaCriada);
          if (response.ok) {
            this.erro = null;
            this.sucesso = "Funcionário criado com sucesso!";
            this.$router.push({ name: "home" });
          } else {
            console.error("Erro ao criar a pessoa.");
            this.sucesso = null;
            this.erro = "Erro ao criar a pessoa";
          }
        })
        .catch((error) => {
          console.error("Erro ao enviar a solicitação de criação", error);
          this.sucesso = null;
          this.erro = "Erro ao criar a pessoa";
        });
    },
    voltarParaHome() {
      this.$router.push({ name: "home" });
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
.butao {
  margin: 5px 0;
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.butao {
  background: #007bff;
  color: #fff;
  cursor: pointer;
}

.alert {
  background-color: #f44336; /* Vermelho */
  color: white;
  padding: 10px;
  margin-top: 20px;
  border-radius: 4px; /* Borda arredondada */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra */
  text-align: center; /* Centralizar texto */
}

.alert-danger {
  background-color: #f44336; /* Vermelho */
}

.alert-success {
  background-color: #4caf50; /* Verde */
}

.alert-info {
  background-color: #2196f3; /* Azul */
}

.alert-warning {
  background-color: #ff9800; /* Laranja */
}
</style>
