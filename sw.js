const CACHE_NAME = 'medwiki-v1';
const ASSETS = [
  './',
  './index.html',
  './clinical_tools/web_tools/aps_classification.html',
  './clinical_tools/web_tools/index.html',
  './clinical_tools/web_tools/sle_2019_eular_acr.html',
  './clinical_tools/web_tools/sledai_2000.html',
  './clinical_tools/web_tools/tma_card.html',
  './drugs/anakinra.html',
  './drugs/azathioprine.html',
  './drugs/biologics.html',
  './drugs/calcium_vitd.html',
  './drugs/corticosteroids_IV.html',
  './drugs/cyclosporine.html',
  './drugs/glucocorticoids.html',
  './drugs/IVIG.html',
  './drugs/MTX.html',
  './drugs/mycophenolate.html',
  './drugs/NSAIDs.html',
  './drugs/tacrolimus.html',
  './drugs/tocilizumab.html',
  './tools/APS_2023_ACR_EULAR.html',
  './tools/autoantibodies.html',
  './tools/BMI_Zscore.html',
  './tools/BSA.html',
  './tools/CDAI.html',
  './tools/CHAQ.html',
  './tools/DAS28.html',
  './tools/ESR_CRP.html',
  './tools/followup.html',
  './tools/JADAS27.html',
  './tools/JADAS71.html',
  './tools/liver_kidney.html',
  './tools/MTX_dose.html',
  './tools/SDAI.html',
  './tools/SLE_2019_EULAR_ACR.html',
  './tools/SLE2K.html',
  './tools/TMA.html',
  './tools/vaccine.html',
  './topics/AID.html',
  './topics/IgAV.html',
  './topics/ITP.html',
  './topics/JDM.html',
  './topics/JIA.html',
  './topics/JSLE.html',
  './topics/KD.html',
  './topics/MAS.html',
  './topics/PID.html',
  './topics/SLE.html',
  './topics/Uveitis.html',
  './manifest.json'
];

// Install: cache all assets
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Fetch: cache-first strategy
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
