# SQLUser.SS_UserDefWinGroupItems

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WINGRPITM_ParRef | bigint | PK |  | NO | SS_UserDefWinGroup Parent Reference |
| WINGRPITM_Childsub | double |  |  | NO | Childsub |
| WINGRPITM_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| WINGRPITM_CreatedDate | date |  |  | SI | Created Date |
| WINGRPITM_CreatedTime | time |  |  | SI | Created Time |
| WINGRPITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WINGRPITM_DateFrom | date |  |  | SI | Date From |
| WINGRPITM_DateTo | date |  |  | SI | Date To |
| WINGRPITM_RowId | varchar |  |  | NO | - |
| WINGRPITM_UpdatedDate | date |  |  | SI | Updated Date |
| WINGRPITM_UpdatedTime | time |  |  | SI | Updated Time |
| WINGRPITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WINGRPITM_Window_DR | bigint |  | FK | SI | Des Ref Window |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*