<template>
  <div class="pessoas">
    <person-item
      v-for="pessoa in pessoas"
      :key="pessoa.id_pessoa"
      :pessoa="pessoa"
    />
  </div>
</template>

<script>
import PersonItem from "@/components/PersonItem.vue";

export default {
  name: "PersonList",
  props: ["pessoas"],
  components: {
    PersonItem,
  },
};
</script>

<style lang="scss">
.pessoas {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr;
  gap: 20px 20px;
  grid-template-areas: ". . . .";
}
</style>
