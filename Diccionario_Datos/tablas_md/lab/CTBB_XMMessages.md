# lab.CTBB_XMMessages

**Schema:** lab
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBXMM_RowID | varchar | PK |  | NO | - |
| BBXMM_BBNS_Error | varchar |  |  | SI | Error Message for non BBSUpervisor |
| BBXMM_BBNS_Events | varchar |  |  | SI | Events for non BBSUpervisor |
| BBXMM_BBNS_Info | varchar |  |  | SI | Info Message for non BBSUpervisor |
| BBXMM_BBNS_PIN | varchar |  |  | SI | PIN request for non BBSUpervisor |
| BBXMM_BBNS_Select | varchar |  |  | SI | Select Message for non BBSUpervisor |
| BBXMM_BBNS_VBMessages | varchar |  |  | SI | VB Messages for non BBSUpervisor |
| BBXMM_BBS_Error | varchar |  |  | SI | Error Message for BBSUpervisor |
| BBXMM_BBS_Events | varchar |  |  | SI | Events for BBSUpervisor |
| BBXMM_BBS_Info | varchar |  |  | SI | Info Message for BBSUpervisor |
| BBXMM_BBS_PIN | varchar |  |  | SI | PIN request for BBSUpervisor |
| BBXMM_BBS_Select | varchar |  |  | SI | Select Message for BBSUpervisor |
| BBXMM_BBS_VBMessages | varchar |  |  | SI | VB Messages for BBSUpervisor |
| BBXMM_Code | varchar |  |  | NO | Code |
| BBXMM_Sequence | varchar |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*