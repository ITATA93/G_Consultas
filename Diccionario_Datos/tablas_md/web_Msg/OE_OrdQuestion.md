# web_Msg.OE_OrdQuestion

**Schema:** web_Msg
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CurrentMLAnswer | varchar |  |  | SI | - |
| DefaultMLAnswer | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBSOIQ_RowID | varchar |  |  | SI | - |
| LBTestSetMsg_DR | varchar |  | FK | SI | - |
| Mandatory | varchar |  |  | SI | - |
| MaxLength | varchar |  |  | SI | - |
| QA_ARCItmMast_DR | varchar |  | FK | SI | - |
| QA_Answer | varchar |  |  | SI | Answer |
| QA_AnswerAtSpecCollect | varchar |  |  | SI | AnsweredAtSpecimenCollection  |
| QA_Childsub | double |  |  | SI | Childsub |
| QA_Date | date |  |  | SI | Date |
| QA_Displayed | bit |  |  | SI | Displayed |
| QA_ParRef | varchar |  |  | SI | OE_OrdItem Parent Reference
Required by User.OEOr... |
| QA_Question_DR | bigint |  | FK | SI | Des Ref Question |
| QA_RowId | varchar |  |  | SI | - |
| QA_SubjectOrdItem_DR | bigint |  | FK | SI | - |
| QA_Time | time |  |  | SI | Time |
| ReadOnly | bit |  |  | SI | - |
| RowCount | integer |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*