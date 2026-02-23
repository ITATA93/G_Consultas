# TC_hmf_Lib.BaseSection

**Schema:** TC_hmf_Lib
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFBASESEC_ParRef | bigint | PK |  | NO | Message Format Parent Reference |
| HMFBASESEC_Code | varchar |  |  | NO | Used by Perforce for generated xml file name |
| HMFBASESEC_DateFrom | date |  |  | SI | Date From |
| HMFBASESEC_DateTo | date |  |  | SI | Date To |
| HMFBASESEC_Enabled | bit |  |  | SI | Enabled flag |
| HMFBASESEC_SectionDR | bigint |  | FK | NO | Des Ref to supported message section |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*