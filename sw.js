// 2026-09-19: 旧缓存SW已废弃（inject.py 已批量移除各页 serviceWorker 注册）。
// 本文件仅作注销器：让仍安装了旧 SW 的浏览器在下次访问时自动注销并清空缓存。
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function () {
  self.registration.unregister();
  if (self.caches && caches.keys) {
    caches.keys().then(function (ks) { ks.forEach(function (k) { caches.delete(k); }); });
  }
  self.clients.claim();
});
