const CACHE = 'medwiki-v7';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './cases/index.html',
  './cases/index_AID.html',
  './cases/index_cSLE.html',
  './cases/index_IgAV.html',
  './cases/index_ITP.html',
  './cases/index_JDM.html',
  './cases/index_KD.html',
  './cases/index_PID.html',
  './cases/index_SLE.html',
  './cases/index_Uveitis.html',
  './cases/index_sJIA.html',
  './cases/case_AID_CAPS.html',
  './cases/case_AID_FMF.html',
  './cases/case_AID_NLRC4.html',
  './cases/case_AID_SAVI.html',
  './cases/case_AID_TRAPS.html',
  './cases/case_cSLE_AIHA_LAHPS.html',
  './cases/case_cSLE_CAPS.html',
  './cases/case_cSLE_infantile_LN_PE.html',
  './cases/case_cSLE_MAS_neuro.html',
  './cases/case_cSLE_pancreatitis_MAS.html',
  './cases/case_cSLE_recurrent_MAS.html',
  './cases/case_cSLE_refractory_NPSLE.html',
  './cases/case_cSLE_LN.html',
  './cases/case_IgAV_CNS.html',
  './cases/case_IgAV_GI.html',
  './cases/case_IgAV_nephritis.html',
  './cases/case_IgAV_pulmonary.html',
  './cases/case_IgAV_special.html',
  './cases/case_ITP_acute.html',
  './cases/case_ITP_chronic.html',
  './cases/case_ITP_Evans.html',
  './cases/case_ITP_secondary.html',
  './cases/case_ITP_TPO.html',
  './cases/case_JDM_calcinosis.html',
  './cases/case_JDM_ILD.html',
  './cases/case_JDM_refractory.html',
  './cases/case_JDM_special.html',
  './cases/case_JDM_typical.html',
  './cases/case_JIA_polyarticular.html',
  './cases/case_JIA_biologics.html',
  './cases/case_KD_giant_CAL.html',
  './cases/case_KD_incomplete.html',
  './cases/case_KD_infant.html',
  './cases/case_KD_IVIG_resistant.html',
  './cases/case_KD_shock.html',
  './cases/case_PID_ALPS.html',
  './cases/case_PID_CGD.html',
  './cases/case_PID_CVID.html',
  './cases/case_PID_SCID.html',
  './cases/case_PID_XLA.html',
  './cases/case_sJIA_biologic_MAS.html',
  './cases/case_sJIA_early_MAS.html',
  './cases/case_sJIA_MAS.html',
  './cases/case_sJIA_MAS_new.html',
  './cases/case_sJIA_refractory.html',
  './cases/case_sJIA_typical.html',
  './cases/case_SLE_APLS.html',
  './cases/case_SLE_drug_induced.html',
  './cases/case_SLE_lupus_nephritis.html',
  './cases/case_SLE_macrophage.html',
  './cases/case_SLE_neuropsychiatric.html',
  './cases/case_Uveitis_Behcet.html',
  './cases/case_Uveitis_infectious.html',
  './cases/case_Uveitis_JIA.html',
  './cases/case_Uveitis_TINU.html',
  './cases/case_Uveitis_Vogt.html',
  './cases/case_FMF_colchicine.html',
  './drugs/MTX.html',
  './drugs/glucocorticoids.html',
  './drugs/corticosteroids_IV.html',
  './drugs/NSAIDs.html',
  './drugs/IVIG.html',
  './drugs/cyclosporine.html',
  './drugs/tacrolimus.html',
  './drugs/mycophenolate.html',
  './drugs/azathioprine.html',
  './drugs/anakinra.html',
  './drugs/tocilizumab.html',
  './drugs/biologics.html',
  './drugs/calcium_vitd.html',
  './drugs/hydroxychloroquine.html',
  './drugs/cyclophosphamide.html',
  './drugs/rituximab.html',
  './drugs/etanercept.html',
  './drugs/adalimumab.html',
  './drugs/infliximab.html',
  './drugs/tofacitinib.html',
  './drugs/belimumab.html',
  './drugs/colchicine.html',
  './tools/JADAS27.html',
  './tools/JADAS71.html',
  './tools/CHAQ.html',
  './tools/DAS28.html',
  './tools/CDAI.html',
  './tools/SDAI.html',
  './tools/BSA.html',
  './tools/BMI_Zscore.html',
  './tools/MTX_dose.html',
  './tools/ESR_CRP.html',
  './tools/SLE2K.html',
  './tools/SLE2K_original.html',
  './tools/SLE_2019_EULAR_ACR.html',
  './tools/APS_2023_ACR_EULAR.html',
  './tools/TMA.html',
  './tools/autoantibodies.html',
  './tools/liver_kidney.html',
  './tools/followup.html',
  './tools/vaccine.html',
  './tools/vaccine_decision.html',
  './tools/KD_CA_Zscore.html',
  './tools/KD_IVIG_resistance.html',
  './tools/MAS_HLH_screening.html',
  './tools/drug_risk_assessment.html',
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
  './topics/ANCA_vasculitis.html',
  './topics/APS.html',
  'evidence/index.html',
  'evidence/ev_KD_01.html',
  'evidence/ev_KD_02.html',
  'evidence/ev_KD_03.html',
  'evidence/ev_sJIA_MAS_01.html',
  'evidence/ev_sJIA_MAS_02.html',
  'evidence/ev_cSLE_01.html',
  'evidence/ev_cSLE_02.html',
  'evidence/ev_APS_01.html',
  'evidence/ev_JDM_01.html',
  'evidence/ev_JDM_02.html',
  'evidence/ev_JIA_01.html',
  'evidence/ev_JIA_02.html',
  'evidence/ev_uveitis_01.html',
  'evidence/ev_ITP_01.html',
  'evidence/ev_ITP_02.html',
  'evidence/ev_IgAV_01.html',
  'evidence/ev_IgAV_02.html',
  'evidence/ev_PID_01.html',
  'evidence/ev_PID_02.html',
  'evidence/ev_AID_01.html',
  'evidence/ev_ANCA_01.html',
  'evidence/ev_Behcet_01.html',
  'evidence/ev_jSSc_01.html',
  'evidence/ev_Evans_01.html',
  'evidence/ev_NLE_01.html',
  'evidence/ev_DADA2_01.html',
  'evidence/ev_FMF_01.html',
  'evidence/ev_SAVI_01.html',
  'evidence/ev_GIO_01.html',
  'evidence/ev_Takayasu_01.html',
  'evidence/ev_PAN_01.html',
  'evidence/ev_MCTD_01.html',
  'evidence/ev_pSS_01.html',
  'evidence/ev_CANDLE_01.html',
  'evidence/ev_VEXAS_01.html',
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Network-first for HTML, cache-first for other assets
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  const isHTML = e.request.headers.get('accept')?.includes('text/html');
  
  if (isHTML) {
    // Network-first: try network, fall back to cache
    e.respondWith(
      fetch(e.request)
        .then(resp => {
          const clone = resp.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
          return resp;
        })
        .catch(() => caches.match(e.request))
    );
  } else {
    // Cache-first for CSS/JS/images
    e.respondWith(
      caches.match(e.request).then(r => r || fetch(e.request))
    );
  }
});
