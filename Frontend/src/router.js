// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import PortfolioSite from './components/PortfolioSite.vue';
import PortfolioDemo from './components/Portfolio-demo.vue';
import LandingDemo from './components/LandingDemo.vue';
import AIToolDemo from './components/AIToolDemo.vue';

const routes = [
  { path: '/', component: PortfolioSite },
{ path: '/portfolio-demo', component: PortfolioDemo },
{ path: '/landing-demo', component: LandingDemo },
{ path: '/ai-tool-demo', component: AIToolDemo }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
