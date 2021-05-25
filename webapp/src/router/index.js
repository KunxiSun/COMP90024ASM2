/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import scenarioRouter from './module/scenario'
import mapRouter from './module/map'

Vue.use(Router)

const router = new Router({
  mode: 'hash',
  routes: [
    scenarioRouter,
    mapRouter
  ]
})

router.beforeEach((to, from, next) => {
  if (true) {
    if (to.path === '/') {
      next('/overview/scenario')
    } else {
      next()
    }
  }
})

export default router
