# SQLUser.PAC_ContServiceRec2

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTSERREC2_RowId | bigint | PK |  | NO | - |
| CONTSERREC2_Code | varchar |  |  | NO | Code |
| CONTSERREC2_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTSERREC2_CreatedDate | date |  |  | SI | Created Date |
| CONTSERREC2_CreatedTime | time |  |  | SI | Created Time |
| CONTSERREC2_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTSERREC2_DateFrom | date |  |  | SI | Date From |
| CONTSERREC2_DateTo | date |  |  | SI | Date To |
| CONTSERREC2_Desc | varchar |  |  | NO | Description |
| CONTSERREC2_Owner | varchar |  |  | SI | Owner |
| CONTSERREC2_UpdatedDate | date |  |  | SI | Updated Date |
| CONTSERREC2_UpdatedTime | time |  |  | SI | Updated Time |
| CONTSERREC2_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ22DR | - |  |  | SI | Child Reference: Drainage assessment |
| Q21Q1 | - |  |  | SI | Need daily assessment |
| Q21Q2 | - |  |  | SI | Care |
| Q21Q3 | - |  |  | SI | Site details |
| Q21Q4 | - |  |  | SI | Dressing type / appearance |
| Q21Q5 | - |  |  | SI | Peripheral intravenous patency |
| Q21Q6 | - |  |  | SI | Assessment date and time |
| Q21Q7 | - |  |  | SI | Assessment time |
| Q21Q8 | - |  |  | SI | Assessing care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*