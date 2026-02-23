# SQLUser.LBC_TestSetRevisionDocumentation

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRD_ParRef | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Plan de Interveción Consesuado |
| LBCTSRD_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCTSRD_CreatedDate | date |  |  | SI | Created Date |
| LBCTSRD_CreatedTime | time |  |  | SI | Created Time |
| LBCTSRD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSRD_Details | longvarchar |  |  | SI | Reagent |
| LBCTSRD_RowID | varchar |  |  | NO | - |
| LBCTSRD_Title | varchar |  |  | SI | Last day the record is active |
| LBCTSRD_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSRD_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSRD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q35Q1 | - |  |  | SI | Fecha |
| Q35Q2 | - |  |  | SI | Normas o reglas observadas en la familia |
| Q35Q3 | - |  |  | SI | Roles significativos |
| Q35Q4 | - |  |  | SI | Comunicación |
| Q35Q5 | - |  |  | SI | Límites |
| Q35Q6 | - |  |  | SI | Coaliciones o alianzas |
| Q35Q7 | - |  |  | SI | Comportamiento del poder, autoridad y jerarquías e... |
| Q35Q8 | - |  |  | SI | Otros subsistemas observados |
| Q35Q9 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*