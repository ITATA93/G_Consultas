# lab.PR_ReportDestination

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRPRD_ParRef | double | PK |  | NO | PR_Report Parent Reference |
| PRPRD_Childsub | double |  |  | NO | Childsub |
| PRPRD_Date | date |  |  | SI | Date of printing |
| PRPRD_Destination_DR | varchar |  | FK | SI | Des Ref Print Destination |
| PRPRD_FaxNumber | varchar |  |  | SI | Fax Number |
| PRPRD_FaxRecipient | varchar |  |  | SI | Fax Recipient |
| PRPRD_NumberOfCopies | double |  |  | SI | Number Of Copies |
| PRPRD_RowId | varchar |  |  | NO | - |
| PRPRD_Status | varchar |  |  | SI | Status |
| PRPRD_Time | time |  |  | SI | Time of printing |
| PRPRD_WordIndex | varchar |  |  | SI | Word Index |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*