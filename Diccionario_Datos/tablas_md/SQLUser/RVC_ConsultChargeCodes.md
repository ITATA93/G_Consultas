# SQLUser.RVC_ConsultChargeCodes

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_RowId | bigint | PK |  | NO | - |
| CONS_ARCIM_DR | varchar |  | FK | NO | Des Ref ARCIM |
| CONS_CreatedDate | date |  |  | SI | Created Date |
| CONS_CreatedTime | time |  |  | SI | Created Time |
| CONS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONS_UpdatedDate | date |  |  | SI | Updated Date |
| CONS_UpdatedTime | time |  |  | SI | Updated Time |
| CONS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*