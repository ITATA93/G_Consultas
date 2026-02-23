# SQLUser.PA_DischargeSummaryIntDoc

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTDOC_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| INTDOC_Childsub | double |  |  | NO | Childsub |
| INTDOC_Doc_DR | varchar |  | FK | SI | Des Ref Doc |
| INTDOC_RowId | varchar |  |  | NO | - |
| Q72Q1 | - |  |  | SI | Date |
| Q72Q10 | - |  |  | SI | Signs of Infection |
| Q72Q2 | - |  |  | SI | Tissue at base |
| Q72Q3 | - |  |  | SI | Tissue at base comments |
| Q72Q4 | - |  |  | SI | Exudate |
| Q72Q5 | - |  |  | SI | Signs of infection |
| Q72Q6 | - |  |  | SI | Swab taken? |
| Q72Q7 | - |  |  | SI | Wound bed comments |
| Q72Q8 | - |  |  | SI | Entered by |
| Q72Q9 | - |  |  | SI | Overall trend	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*