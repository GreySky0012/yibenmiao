import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Test from '@/components/Test/Test'
import User from '@/components/User/User'
import {UserRoutes} from './User'
import {TestRoutes} from './Test'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: HelloWorld
    },
    {
      path: '/user',
      component: User,
      children: UserRoutes
    },
    {
      path: '/test',
      component: Test,
      children: TestRoutes
    }
  ]
})
