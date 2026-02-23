# TC_hmf_Adapter.InterfaceMessageSection

**Schema:** TC_hmf_Adapter
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFADAPSEC_ParRef | varchar | PK |  | NO | Interface Parent Reference |
| HMFADAPINT_System | varchar |  |  | SI | System |
| HMFADAPSEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HMFADAPSEC_DateFrom | date |  |  | SI | Date From |
| HMFADAPSEC_DateTo | date |  |  | SI | Date To |
| HMFADAPSEC_Enabled | bit |  |  | SI | Enabled flag |
| HMFADAPSEC_SectionDR | varchar |  | FK | SI | Section Lib DesRef |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*