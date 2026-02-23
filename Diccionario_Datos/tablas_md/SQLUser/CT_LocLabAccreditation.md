# SQLUser.CT_LocLabAccreditation

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LABACC_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| LABACC_Accreditation_DR | bigint |  | FK | SI | Des Ref Accreditation |
| LABACC_Childsub | double |  |  | NO | Childsub |
| LABACC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LABACC_CreatedDate | date |  |  | SI | Created Date |
| LABACC_CreatedTime | time |  |  | SI | Created Time |
| LABACC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LABACC_DateFrom | date |  |  | SI | Date  From |
| LABACC_DateTo | date |  |  | SI | Date To |
| LABACC_RowId | varchar |  |  | NO | - |
| LABACC_UpdatedDate | date |  |  | SI | Updated Date |
| LABACC_UpdatedTime | time |  |  | SI | Updated Time |
| LABACC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q42Q1 | - |  |  | SI | Date |
| Q42Q2 | - |  |  | SI | Time |
| Q42Q3 | - |  |  | SI | Length of ETT after repositioning (cm) |
| Q42Q4 | - |  |  | SI | ETT measured at |
| Q42Q5 | - |  |  | SI | Position confirmed by x-ray |
| Q42Q6 | - |  |  | SI | Repositioned by |
| Q42Q7 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*