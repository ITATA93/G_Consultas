# SQLUser.LB_SubjectOrdItemQuestion

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSOIQ_ParRef | bigint | PK |  | NO | - |
| ChildQ08DR | - |  |  | SI | Child Reference: Factores de Riesgo y Protectores |
| LBSOIQ_Answer | varchar |  |  | SI | Answer |
| LBSOIQ_AnswerAtSpecCollect | varchar |  |  | SI | AnsweredAtSpecimenCollection  |
| LBSOIQ_AnswerMultiline | varchar |  |  | SI | Answer Multiline |
| LBSOIQ_Date | date |  |  | SI | Date |
| LBSOIQ_Displayed | bit |  |  | SI | Displayed |
| LBSOIQ_Question_DR | bigint |  | FK | SI | Des Ref Question |
| LBSOIQ_RowID | varchar |  |  | NO | - |
| LBSOIQ_Time | time |  |  | SI | Time |
| Q21Q1 | - |  |  | SI | Inclusión social |
| Q21Q2 | - |  |  | SI | Trabajo |
| Q21Q3 | - |  |  | SI | Escuela |
| Q21Q4 | - |  |  | SI | Grupos sociales |
| Q21Q5 | - |  |  | SI | Organizaciones |
| Q21Q6 | - |  |  | SI | Otras organzaciones |
| Q21Q7 | - |  |  | SI | Fecha |
| Q21Q8 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*