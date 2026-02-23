# SQLUser.PHC_Cat

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCC_RowId | bigint | PK |  | NO | - |
| PHCC_Code | varchar |  |  | NO | Category Code |
| PHCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCC_CreatedDate | date |  |  | SI | Created Date |
| PHCC_CreatedTime | time |  |  | SI | Created Time |
| PHCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCC_Desc | varchar |  |  | NO | Description |
| PHCC_Owner | varchar |  |  | SI | Owner |
| PHCC_UpdatedDate | date |  |  | SI | Updated Date |
| PHCC_UpdatedTime | time |  |  | SI | Updated Time |
| PHCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*