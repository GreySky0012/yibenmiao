import SignIn from '@/components/User/SignIn'
import SignUp from '@/components/User/SignUp'
import HelloWorld from '@/components/User/HelloWorld'

export const UserRoutes = [
  {
    path: '',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: 'sign_up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: 'sign_in',
    name: 'SignIn',
    component: SignIn
  }
]
