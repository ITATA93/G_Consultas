# SQLUser.PA_DischargeSummaryDoc

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| ChildQ72DR | - |  |  | SI | Child Reference: Wound Bed |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_Doc_DR | varchar |  | FK | SI | Des Ref Doc |
| DOC_PrimaryRecipient | varchar |  |  | SI | Primary Recipient |
| DOC_RowId | varchar |  |  | NO | - |
| Q71Q1 | - |  |  | SI | Type |
| Q71Q2 | - |  |  | SI | Number |
| Q71Q3 | - |  |  | SI | Length (cm) |
| Q71Q4 | - |  |  | SI | O'Clock position |
| Q71Q5 | - |  |  | SI | Comments |
| Q71Q6 | - |  |  | SI | Entered by |
| Q71Q7 | - |  |  | SI | Date |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*