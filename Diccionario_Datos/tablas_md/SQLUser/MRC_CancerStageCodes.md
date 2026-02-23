# SQLUser.MRC_CancerStageCodes

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANSTC_RowId | bigint | PK |  | NO | - |
| CANSTC_Code | varchar |  |  | NO | Code |
| CANSTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANSTC_CreatedDate | date |  |  | SI | Created Date |
| CANSTC_CreatedTime | time |  |  | SI | Created Time |
| CANSTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANSTC_DateFrom | date |  |  | SI | Date From |
| CANSTC_DateTo | date |  |  | SI | Date To |
| CANSTC_Desc | varchar |  |  | NO | Description |
| CANSTC_Owner | varchar |  |  | SI | Owner |
| CANSTC_StageType | varchar |  |  | SI | Cancer Stage Type |
| CANSTC_UpdatedDate | date |  |  | SI | Updated Date |
| CANSTC_UpdatedTime | time |  |  | SI | Updated Time |
| CANSTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Identificación |
| Q01Q2 | - |  |  | SI | Estado de Salud |
| Q01Q3 | - |  |  | SI | Destino |
| Q01Q4 | - |  |  | SI | Alimentacion (al egreso) |
| Q01Q5 | - |  |  | SI | Peso al egreso (grs.) |
| Q01Q6 | - |  |  | SI | Comentarios |
| Q01Q7 | - |  |  | SI | Fecha de Egreso |
| Q01Q8 | - |  |  | SI | Alimentación (durante estadía) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*