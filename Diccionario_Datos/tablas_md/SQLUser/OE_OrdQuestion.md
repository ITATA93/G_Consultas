# SQLUser.OE_OrdQuestion

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QA_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ62DR | - |  |  | SI | Child Reference: Test Movement Describe Effect on ... |
| Q61Q1 | - |  |  | SI | Movement |
| Q61Q2 | - |  |  | SI | Major |
| Q61Q3 | - |  |  | SI | Pain |
| Q61Q4 | - |  |  | SI | Muscle Power /5 |
| Q61Q5 | - |  |  | SI | Moderate |
| Q61Q6 | - |  |  | SI | Minimum |
| Q61Q7 | - |  |  | SI | Nil |
| Q61Q8 | - |  |  | SI | Deviation |
| QA_Answer | varchar |  |  | SI | Answer |
| QA_AnswerAtSpecCollect | varchar |  |  | SI | AnsweredAtSpecimenCollection  |
| QA_AnswerMultiline | varchar |  |  | SI | Answer Multiline |
| QA_Childsub | double |  |  | NO | Childsub |
| QA_Date | date |  |  | SI | Date |
| QA_Displayed | bit |  |  | SI | Displayed |
| QA_Question_DR | bigint |  | FK | SI | Des Ref Question |
| QA_RowId | varchar |  |  | NO | - |
| QA_Time | time |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*