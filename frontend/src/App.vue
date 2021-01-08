<template>
  <div>
    <nav>
      <router-link
          to="/"
          active-class="link--active"
          exact
          class="link"
      >Home
      </router-link>
      <router-link
          to="users"
          active-class="link--active"
          exact
          class="link"
      >Users
      </router-link>
      <button @click="tasu">+1</button>
      <button @click="hiku">+1</button>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  methods: {
    tasu: function () {
      this.$store.state.count++;
    },
    hiku: function () {
      this.$store.state.count--;
    }
  }
};
</script>

<style scoped>
.link {
  margin-right: 10px;
}

.link--active {
  font-size: 20px
}
</style>