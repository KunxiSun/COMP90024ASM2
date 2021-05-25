import Layout from '@/layout/index.vue'

const mapRouter = {
  path: '/map',
  name: 'australia.vue',
  meta: {
    title: 'Map'
  },
  component: Layout,
  children: [
    {
      path: 'australia',
      name: 'australia',
      meta: {
        title: 'Australia'
      },
      component: () => import('@/views/map/australia')
    }
  ]
}
export default mapRouter
