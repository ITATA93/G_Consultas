# SQLUser.LBC_Specimen

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSP_RowID | bigint | PK |  | NO | - |
| LBCSP_Code | varchar |  |  | NO | Code |
| LBCSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSP_CodeTranslated | varchar |  |  | SI | Code Translated |
| LBCSP_CreatedDate | date |  |  | SI | Created Date |
| LBCSP_CreatedTime | time |  |  | SI | Created Time |
| LBCSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSP_DateFrom | date |  |  | SI | Date Active From |
| LBCSP_DateTo | date |  |  | SI | Date Active To |
| LBCSP_Desc | varchar |  |  | NO | Description |
| LBCSP_DescTranslated | varchar |  |  | SI | Desc Translated |
| LBCSP_Group_DR | bigint |  | FK | SI | Specimen Group |
| LBCSP_Owner | varchar |  |  | SI | Owner |
| LBCSP_Sequence | double |  |  | SI | Sequence |
| LBCSP_SuitableForPooling | varchar |  |  | SI | Suitable for pooling |
| LBCSP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*