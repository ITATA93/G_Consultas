# SQLUser.LBC_TestSetRevisionSpecialHandling

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRSH_ParRef | bigint | PK |  | NO | Parent Reference to LBCTestSetRevision |
| ChildQ42DR | - |  |  | SI | Child Reference: Examen Cardiaco |
| LBCTSRSH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRSH_Converted | bit |  |  | SI | Converted Flag
Cannot be set via the UI |
| LBCTSRSH_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRSH_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBCTSRSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBCTSRSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBCTSRSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBCTSRSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBCTSRSH_RowID | varchar |  |  | NO | - |
| LBCTSRSH_Sequence | integer |  |  | SI | Sequence |
| LBCTSRSH_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| Q38Q1 | - |  |  | SI | Percusión |
| Q38Q2 | - |  |  | SI | Auscultación |
| Q38Q3 | - |  |  | SI | Localización |
| Q38Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*