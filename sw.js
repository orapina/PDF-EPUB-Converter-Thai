const CACHE='catto-v2';
const ASSETS=[
  './',
  './index.html',
  './translate.html',
  './rainflow.png',
  './manifest.json',
  'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Sarabun:wght@300;400;500;600&family=JetBrains+Mono:wght@400&display=swap'
];

self.addEventListener('install',e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()));
});

self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));
});

self.addEventListener('fetch',e=>{
  /* Network-first for API calls, cache-first for static assets */
  if(e.request.url.includes('api.opentyphoon.ai')||e.request.url.includes('generativelanguage.googleapis.com')||e.request.url.includes('visitorbadge.io')){
    return;
  }
  e.respondWith(
    caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{
      if(res.ok&&res.type==='basic'){
        var clone=res.clone();
        caches.open(CACHE).then(c=>c.put(e.request,clone));
      }
      return res;
    }).catch(()=>caches.match('./index.html')))
  );
});
