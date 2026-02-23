# SQLUser.INC_SterileItems

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STER_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q35Q1 | - |  |  | SI | Deformidad |
| Q35Q2 | - |  |  | SI | Expansión respiratória asimétrica |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| STER_Childsub | double |  |  | NO | Childsub |
| STER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STER_CreatedDate | date |  |  | SI | Created Date |
| STER_CreatedTime | time |  |  | SI | Created Time |
| STER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STER_INCI_DR | bigint |  | FK | SI | Des Ref to INCI |
| STER_RowId | varchar |  |  | NO | - |
| STER_UpdatedDate | date |  |  | SI | Updated Date |
| STER_UpdatedTime | time |  |  | SI | Updated Time |
| STER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*