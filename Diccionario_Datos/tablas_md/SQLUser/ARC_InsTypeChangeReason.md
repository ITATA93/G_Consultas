# SQLUser.ARC_InsTypeChangeReason

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCHR_RowId | bigint | PK |  | NO | - |
| INCHR_Code | varchar |  |  | NO | Code |
| INCHR_CreatedDate | date |  |  | SI | Created Date |
| INCHR_CreatedTime | time |  |  | SI | Created Time |
| INCHR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCHR_Desc | varchar |  |  | NO | Description |
| INCHR_UpdatedDate | date |  |  | SI | Updated Date |
| INCHR_UpdatedTime | time |  |  | SI | Updated Time |
| INCHR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q04Q1 | - |  |  | SI | Hallazgo |
| Q04Q2 | - |  |  | SI | Ubicación |
| Q04Q3 | - |  |  | SI | Sensibilidad |
| Q04Q4 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*