<template>
  <div>
    <h3>Home</h3>
    <button @click="toUsers">Usersのページに行く</button>
    <p> {{ doublecount }}</p>
  </div>
</template>


<script>
export default {
  computed: {
    doublecount() {
      return this.$store.getters.doubleCount;
    }
  },
  methods: {
    toUsers() {
      this.$router.push("users/1");
    }
  }
};
</script>