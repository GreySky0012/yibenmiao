import HelloWorld from '@/components/Test/HelloWorld'
import Debug from '@/components/Test/Debug'

export const TestRoutes = [
  {
    path: '',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: 'debug',
    name: 'Debug',
    component: Debug
  }
]
