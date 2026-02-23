# web_Msg.DocumentUpload

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AttachToEPR | bit |  |  | SI | Attach to EPR |
| Chunks | longvarbinary |  |  | SI | Encoded data chunks
Array of seperatly uploaded p... |
| Comments | varchar |  |  | SI | Comments |
| Data | longvarbinary |  |  | SI | Final decoded document data |
| DocumentRowID | varchar |  |  | SI | Corresbonding websys.Document RowID |
| ID | varchar |  |  | NO | - |
| Name | varchar |  |  | NO | Document name |
| ParRef | varchar |  |  | SI | Corresbonding ParRef RowID |
| ParRefClass | varchar |  |  | SI | ParRef class |
| ReadOnly | bit |  |  | SI | - |
| RowID | varchar |  |  | SI | Corresbonding  RowID |
| SessionId | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | Status |
| TestSetID | varchar |  |  | SI | TestSet RowID for linking from Worksheet |
| Type | varchar |  |  | NO | Document type / Original File Extention |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*