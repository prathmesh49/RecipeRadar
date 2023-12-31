import { createApp, Vue } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import './index.css'


createApp(App).use(router).mount('#app')

import 'flowbite';
