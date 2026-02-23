# SQLUser.LB_DynamicFunctionTest

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDFT_RowID | bigint | PK |  | NO | - |
| ChildQ64DR | - |  |  | SI | Child Reference: EMBARAZOS |
| LBDFT_CloseDate | date |  |  | SI | The date the DFT was closed |
| LBDFT_CloseTime | time |  |  | SI | The time the DFT was closed |
| LBDFT_CloseUser_DR | bigint |  | FK | SI | The user that closed the DFT |
| LBDFT_Comments_DR | bigint |  | FK | SI | Comments
Link to a websys.Document that stores th... |
| LBDFT_DynamicFunctionTestRevision_DR | bigint |  | FK | NO | Link to the code table DFT |
| LBDFT_OpenDate | date |  |  | SI | The date the DFT was opened |
| LBDFT_OpenTime | time |  |  | SI | The time the DFT was opened |
| LBDFT_OpenUser_DR | bigint |  | FK | SI | The user that opened the DFT |
| LBDFT_Patient_DR | bigint |  | FK | SI | Link to the patient |
| LBDFT_Subject_DR | bigint |  | FK | SI | Link to the lab subject (replacing the patient for... |
| Q46Q1 | - |  |  | SI | Hallazgo |
| Q46Q2 | - |  |  | SI | Intensidad |
| Q46Q3 | - |  |  | SI | Ubicación |
| Q46Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*