import SignIn from '@/components/User/SignIn'
import SignUp from '@/components/User/SignUp'

export const UserRoutes = [
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
