# TC_hmf_Adapter_Interface.CustomHost

**Schema:** TC_hmf_Adapter_Interface
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFADAPHOST_ParRef | varchar | PK |  | NO | Adapter Interface Parent Reference |
| HMFADAPHOST_EnableCustomClass | bit |  |  | SI | Enable Custom Class flag - if checked custom host ... |
| HMFADAPHOST_Type | varchar |  |  | SI | Business Host Class Type |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*